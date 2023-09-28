# -*- coding: utf-8 -*-
from modbe.internal.module.ItemBase import ItemBase
from modbe.internal.module.ModBE import ModBE
from modbe.internal.enum.Log import LogLevel, LogType
from modbe.internal.constant.Component import *
from modbe.internal.module.Tag import *
from modbe.public.module.Block import Block


class Item(ItemBase):

    def __init__(self, fullName, aux=0):
        super(Item, self).__init__(fullName, aux)
        if ModBE.isServer():
            if self.isBlock():
                self._block = Block(self._convertBlockItemIdentifier(fullName), aux)
        elif ModBE.isClient():
            pass

    def __eq__(self, other):
        if isinstance(other, Item):
            return self.getItemIdentifier() == other.getItemIdentifier() and self.getAuxValue() == other.getAuxValue()
        elif isinstance(other, str):
            if self.getAuxValue() == 0:
                return self.getItemIdentifier() == other
            else:
                return self.getItemIdentifier() + ":" + str(self.getAuxValue()) == other
        else:
            return NotImplemented

    def __ne__(self, other):
        if not isinstance(other, Item) or not isinstance(other, str):
            return NotImplemented
        return not self.__eq__(other)

    def _getItemBasicDict(self):
        return _item_.GetItemBasicInfo(self._fullName, self._aux)

    def _getBlockBasicDict(self):
        """
        仅服务端
        """
        if ModBE.isServer():
            return _blockInfo_.GetBlockBasicInfo(self._fullName)
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE",
                      "Item._getBlockBasicDict: Client not supported for this method.")

    @staticmethod
    def _convertBlockItemIdentifier(itemIdentifier):
        blockName = itemIdentifier.split(":")[1]
        if blockName.startswith("item."):
            blockName = blockName[5:]
        return itemIdentifier.split(":")[0] + ":" + blockName

    def getBlockIdentifier(self):
        """
        仅服务端
        """
        if ModBE.isServer():
            if self.isBlock():
                return self._convertBlockItemIdentifier(self._fullName)
            return None
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE",
                      "Item.getBlockIdentifier: Client not supported for this method.")

    def isBlock(self):
        """
        仅服务端
        """
        if ModBE.isServer():
            loadedBlocks = _blockInfo_.GetLoadBlocks()
            if self._convertBlockItemIdentifier(self._fullName) in loadedBlocks:
                return True
            return False
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE", "Item.isBlock: Client not supported for this method.")

    def getBlock(self):
        """
        仅服务端
        """
        if ModBE.isServer():
            if self.isBlock():
                return self._block
            return None
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE", "Item.getBlock: Client not supported for this method.")

    def getIdAux(self):
        return self._getItemBasicDict()["id_aux"]

    def getAttackDamage(self):
        return self._getItemBasicDict()["weaponDamage"]

    def getMaxDamage(self):
        return self._getItemBasicDict()["maxDurability"]

    def getCreativeCategory(self):
        return self.categoryFromString[self._getItemBasicDict()["itemCategory"]]

    def getTierLevel(self):
        return self._getItemBasicDict()["itemTierLevel"]

    def getArmorValue(self):
        return self._getItemBasicDict()["armorDefense"]

    def getToughnessValue(self):
        return self._getItemBasicDict()["armorToughness"]

    def getKnockbackResistance(self):
        return self._getItemBasicDict()["armorKnockbackResistance"]

    def getMaxStackSize(self):
        return self._getItemBasicDict()["maxStackSize"]

    def getFurnaceBurnInterval(self):
        return self._getItemBasicDict()["fuelDuration"]

    def getFoodNutrition(self):
        return self._getItemBasicDict()["foodNutrition"]

    def getFoodSaturation(self):
        return self._getItemBasicDict()["foodSaturation"]

    def getName(self):
        return self._getItemBasicDict()["itemName"]


class ItemStack(object):
    TAG_ENCHANTS = "ench"

    def __init__(self, fullName, count=1, aux=0, _userData=None):
        self._item = Item(fullName)
        self._block = None
        self._aux = aux
        self._count = count
        self._userData = CompoundTag()
        if _userData is not None:
            if isinstance(_userData, dict):
                self._userData = CompoundTag.fromObject(_userData)
            elif isinstance(_userData, CompoundTag):
                self._userData = _userData
        if ModBE.isServer():
            self._block = self._item.getBlock()
        elif ModBE.isClient():
            pass

    def __eq__(self, other):
        if not isinstance(other, ItemStack):
            return NotImplemented
        return self.getItem() == other.getItem() and self.get() == other.get() and self.getAuxValue() == other.getAuxValue() and self.getUserData() == other.getUserData()

    def __ne__(self, other):
        if not isinstance(other, ItemStack):
            return NotImplemented
        return self.getItem() != other.getItem() or self.get() != other.get() or self.getAuxValue() != other.getAuxValue() or self.getUserData() != other.getUserData()

    @staticmethod
    def fromDict(itemDict):
        identifier = itemDict["newItemName"]
        aux = itemDict["newAuxValue"]
        count = itemDict["count"]
        _userData = "userData" in itemDict and itemDict["userData"] or None
        return ItemStack(identifier, count, aux, _userData)

    def _getItemBasicDict(self):
        return _item_.GetItemBasicInfo(self.getItemIdentifier(), self.getAuxValue(), self.isEnchanted())

    def getItem(self):
        return self._item

    def isBlock(self):
        """
        仅服务端
        """
        if ModBE.isServer():
            return self.getItem().isBlock()
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE",
                      "ItemStack.isBlock: Client not supported for this method.")

    def getBlock(self):
        """
        仅服务端
        """
        if ModBE.isServer():
            if self.isBlock():
                return self._block
            return None
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE", "ItemStack.getBlock: Client not supported for this method.")

    def get(self):
        return self._count

    def set(self, inCount):
        if inCount <= self.getMaxStackSize():
            self._count = inCount >= 0 and inCount or 0
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE",
                      "ItemStack.set: inCount > maxStackSize.")

    def add(self, addCount):
        self.set(self.get() + addCount)

    def remove(self, removeCount):
        self.set(self.get() - removeCount)

    def increase(self):
        self.add(1)

    def decrease(self):
        self.remove(1)

    def getUserData(self):
        return self._userData

    def getItemIdentifier(self):
        return self.getItem().getItemIdentifier()

    def getBlockIdentifier(self):
        """
        仅服务端
        """
        if ModBE.isServer():
            if self.isBlock():
                return self.getItem().getBlockIdentifier()
            return None
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE",
                      "ItemStack.getBlockIdentifier: Client not supported for this method.")

    def getAuxValue(self):
        return self._aux

    def isEnchanted(self):
        return self.getUserData().contains(self.TAG_ENCHANTS)

    def getIdAux(self):
        return self._getItemBasicDict()["id_aux"]

    def getAttackDamage(self):
        return self._getItemBasicDict()["weaponDamage"]

    def getMaxDamage(self):
        return self._getItemBasicDict()["maxDurability"]

    def getCreativeCategory(self):
        return Item.categoryFromString[self._getItemBasicDict()["itemCategory"]]

    def getTierLevel(self):
        return self._getItemBasicDict()["itemTierLevel"]

    def getArmorValue(self):
        return self._getItemBasicDict()["armorDefense"]

    def getToughnessValue(self):
        return self._getItemBasicDict()["armorToughness"]

    def getKnockbackResistance(self):
        return self._getItemBasicDict()["armorKnockbackResistance"]

    def getMaxStackSize(self):
        return self._getItemBasicDict()["maxStackSize"]

    def getFurnaceBurnInterval(self):
        return self._getItemBasicDict()["fuelDuration"]

    def getFoodNutrition(self):
        return self._getItemBasicDict()["foodNutrition"]

    def getFoodSaturation(self):
        return self._getItemBasicDict()["foodSaturation"]

    def getDamageValue(self):
        return self.getUserData().getInt("Damage")

    def isFullStack(self):
        return self.get() >= self.getMaxStackSize()

    def isEmptyStack(self):
        return self.get() <= 0

    def getHoverName(self):
        """
        仅客户端
        """
        if ModBE.isClient():
            return _item_.GetItemHoverName(self.getItemIdentifier(), self.getAuxValue(), self.getUserData().toObject())
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE", "ItemStack.getHoverName: Server not supported for this method.")

    def getCustomName(self):
        if ModBE.isServer():
            return _item_.GetCustomName({"userData": self.getUserData().toObject()})
        elif ModBE.isClient():
            userData = self.getUserData()
            display = userData.getCompound("display")
            if display is not None:
                return display.getString("Name")

    def getName(self):
        return self._getItemBasicDict()["itemName"]

    def getFormattedHovertext(self, showCategory):
        """
        仅客户端
        """
        if ModBE.isClient():
            return _item_.GetItemFormattedHoverText(self.getItemIdentifier(), self.getAuxValue(), showCategory, self.getUserData().toObject())
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE", "ItemStack.getFormattedHovertext: Server not supported for this method.")

    def getEffectName(self):
        """
        仅客户端
        """
        if ModBE.isClient():
            return _item_.GetItemEffectName(self.getItemIdentifier(), self.getAuxValue(), self.getUserData().toObject())
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE", "ItemStack.getEffectName: Server not supported for this method.")