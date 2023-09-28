# -*- coding: utf-8 -*-
import server.extraServerApi as extraServerApi
import client.extraClientApi as extraClientApi
import common.game as game
server = game.GetServer()
client = game.GetClient()

from modbe.internal.module.ModBE import ModBE

import functools

__all__ = [
    "_achievement",
    "_action",
    "_actorCollidable",
    "_actorLoot",
    "_actorMotion",
    "_actorOwner",
    "_actorPushable",
    "_actorRender",
    "_armorSlot",
    "_attr",
    "_auxValue",
    "_biome",
    "_block",
    "_blockEntityData",
    "_blockGeometry",
    "_blockInfo",
    "_blockState",
    "_blockUseEventWhiteList",
    "_breath",
    "_brightness",
    "_buff",
    "_bulletAttributes",
    "_camera",
    "_carried",
    "_chatExtension",
    "_chestBlock",
    "_chunkSource",
    "_cloudMusic",
    "_collisionBox",
    "_command",
    "_controlAi",
    "_customAudio",
    "_customItem",
    "_deathCount",
    "_device",
    "_dimension",
    "_effect",
    "_effectInfo",
    "_engineEffectBindControl",
    "_engineType",
    "_entityComponent",
    "_entityEvent",
    "_exp",
    "_explosion",
    "_extraData",
    "_feature",
    "_fly",
    "_fog",
    "_frameAniControl",
    "_frameAniEntityBind",
    "_frameAniNativeEntityBoneBind",
    "_frameAniSkeletonBind",
    "_frameAniTrans",
    "_game",
    "_gravity",
    "_health",
    "_httpToServer",
    "_hurt",
    "_interact",
    "_inventory",
    "_item",
    "_itembanned",
    "_itemInfo",
    "_lobbyGood",
    "_lv",
    "_miniMap",
    "_mobSpawn",
    "_modAttr",
    "_model",
    "_mouseHook",
    "_moveTo",
    "_msg",
    "_name",
    "_neApi",
    "_offHand",
    "_operation",
    "_particleControl",
    "_particleEntityBind",
    "_particleNativeEntityBoneBind",
    "_particleSkeletonBind",
    "_particleSystem",
    "_particleTrans",
    "_path",
    "_persistence",
    "_pet",
    "_player",
    "_playeranim",
    "_playerView",
    "_playerKillCount",
    "_portal",
    "_pos",
    "_postprocess",
    "_queryVariable",
    "_projectile",
    "_recipe",
    "_redStone",
    "_research",
    "_ride",
    "_rot",
    "_scale",
    "_seasonMod",
    "_shareables",
    "_Shop",
    "_sign",
    "_simpleMsg",
    "_skyRender",
    "_spawn",
    "_speed",
    "_storyline",
    "_systemAudio",
    "_tag",
    "_tame",
    "_team",
    "_teamId",
    "_textBoard",
    "_textNotifyClient",
    "_time",
    "_totalKillCount",
    "_type",
    "_vDeliverComp",
    "_virtualWorld",
    "_weather",
    "_achievement_",
    "_action_",
    "_actorCollidable_",
    "_actorLoot_",
    "_actorMotion_",
    "_actorOwner_",
    "_actorPushable_",
    "_actorRender_",
    "_armorSlot_",
    "_attr_",
    "_auxValue_",
    "_biome_",
    "_block_",
    "_blockEntityData_",
    "_blockGeometry_",
    "_blockInfo_",
    "_blockState_",
    "_blockUseEventWhiteList_",
    "_breath_",
    "_brightness_",
    "_buff_",
    "_bulletAttributes_",
    "_camera_",
    "_carried_",
    "_chatExtension_",
    "_chestBlock_",
    "_chunkSource_",
    "_cloudMusic_",
    "_collisionBox_",
    "_command_",
    "_controlAi_",
    "_customAudio_",
    "_customItem_",
    "_deathCount_",
    "_device_",
    "_dimension_",
    "_effect_",
    "_effectInfo_",
    "_engineEffectBindControl_",
    "_engineType_",
    "_entityComponent_",
    "_entityEvent_",
    "_exp_",
    "_explosion_",
    "_extraData_",
    "_feature_",
    "_fly_",
    "_fog_",
    "_frameAniControl_",
    "_frameAniEntityBind_",
    "_frameAniNativeEntityBoneBind_",
    "_frameAniSkeletonBind_",
    "_frameAniTrans_",
    "_game_",
    "_gravity_",
    "_health_",
    "_httpToServer_",
    "_hurt_",
    "_interact_",
    "_inventory_",
    "_item_",
    "_itembanned_",
    "_itemInfo_",
    "_lobbyGood_",
    "_lv_",
    "_miniMap_",
    "_mobSpawn_",
    "_modAttr_",
    "_model_",
    "_mouseHook_",
    "_moveTo_",
    "_msg_",
    "_name_",
    "_neApi_",
    "_offHand_",
    "_operation_",
    "_particleControl_",
    "_particleEntityBind_",
    "_particleNativeEntityBoneBind_",
    "_particleSkeletonBind_",
    "_particleSystem_",
    "_particleTrans_",
    "_path_",
    "_persistence_",
    "_pet_",
    "_player_",
    "_playeranim_",
    "_playerView_",
    "_playerKillCount_",
    "_portal_",
    "_pos_",
    "_postprocess_",
    "_queryVariable_",
    "_projectile_",
    "_recipe_",
    "_redStone_",
    "_research_",
    "_ride_",
    "_rot_",
    "_scale_",
    "_seasonMod_",
    "_shareables_",
    "_Shop_",
    "_sign_",
    "_simpleMsg_",
    "_skyRender_",
    "_spawn_",
    "_speed_",
    "_storyline_",
    "_systemAudio_",
    "_tag_",
    "_tame_",
    "_team_",
    "_teamId_",
    "_textBoard_",
    "_textNotifyClient_",
    "_time_",
    "_totalKillCount_",
    "_type_",
    "_vDeliverComp_",
    "_virtualWorld_",
    "_weather_"
]

# partial component
_achievement = None
_action = None
_actorCollidable = None
_actorLoot = None
_actorMotion = None
_actorOwner = None
_actorPushable = None
_actorRender = None
_armorSlot = None
_attr = None
_auxValue = None
_biome = None
_block = None
_blockEntityData = None
_blockGeometry = None
_blockInfo = None
_blockState = None
_blockUseEventWhiteList = None
_breath = None
_brightness = None
_buff = None
_bulletAttributes = None
_camera = None
_carried = None
_chatExtension = None
_chestBlock = None
_chunkSource = None
_cloudMusic = None
_collisionBox = None
_command = None
_controlAi = None
_customAudio = None
_customItem = None
_deathCount = None
_device = None
_dimension = None
_effect = None
_effectInfo = None
_engineEffectBindControl = None
_engineType = None
_entityComponent = None
_entityEvent = None
_exp = None
_explosion = None
_extraData = None
_feature = None
_fly = None
_fog = None
_frameAniControl = None
_frameAniEntityBind = None
_frameAniNativeEntityBoneBind = None
_frameAniSkeletonBind = None
_frameAniTrans = None
_game = None
_gravity = None
_health = None
_httpToServer = None
_hurt = None
_interact = None
_inventory = None
_item = None
_itembanned = None
_itemInfo = None
_lobbyGood = None
_lv = None
_miniMap = None
_mobSpawn = None
_modAttr = None
_model = None
_mouseHook = None
_moveTo = None
_msg = None
_name = None
_neApi = None
_offHand = None
_operation = None
_particleControl = None
_particleEntityBind = None
_particleNativeEntityBoneBind = None
_particleSkeletonBind = None
_particleSystem = None
_particleTrans = None
_path = None
_persistence = None
_pet = None
_player = None
_playeranim = None
_playerView = None
_playerKillCount = None
_portal = None
_pos = None
_postprocess = None
_queryVariable = None
_projectile = None
_recipe = None
_redStone = None
_research = None
_ride = None
_rot = None
_scale = None
_seasonMod = None
_shareables = None
_Shop = None
_sign = None
_simpleMsg = None
_skyRender = None
_spawn = None
_speed = None
_storyline = None
_systemAudio = None
_tag = None
_tame = None
_team = None
_teamId = None
_textBoard = None
_textNotifyClient = None
_time = None
_totalKillCount = None
_type = None
_vDeliverComp = None
_virtualWorld = None
_weather = None

# level specific component
_achievement_ = None
_action_ = None
_actorCollidable_ = None
_actorLoot_ = None
_actorMotion_ = None
_actorOwner_ = None
_actorPushable_ = None
_actorRender_ = None
_armorSlot_ = None
_attr_ = None
_auxValue_ = None
_biome_ = None
_block_ = None
_blockEntityData_ = None
_blockGeometry_ = None
_blockInfo_ = None
_blockState_ = None
_blockUseEventWhiteList_ = None
_breath_ = None
_brightness_ = None
_buff_ = None
_bulletAttributes_ = None
_camera_ = None
_carried_ = None
_chatExtension_ = None
_chestBlock_ = None
_chunkSource_ = None
_cloudMusic_ = None
_collisionBox_ = None
_command_ = None
_controlAi_ = None
_customAudio_ = None
_customItem_ = None
_deathCount_ = None
_device_ = None
_dimension_ = None
_effect_ = None
_effectInfo_ = None
_engineEffectBindControl_ = None
_engineType_ = None
_entityComponent_ = None
_entityEvent_ = None
_exp_ = None
_explosion_ = None
_extraData_ = None
_feature_ = None
_fly_ = None
_fog_ = None
_frameAniControl_ = None
_frameAniEntityBind_ = None
_frameAniNativeEntityBoneBind_ = None
_frameAniSkeletonBind_ = None
_frameAniTrans_ = None
_game_ = None
_gravity_ = None
_health_ = None
_httpToServer_ = None
_hurt_ = None
_interact_ = None
_inventory_ = None
_item_ = None
_itembanned_ = None
_itemInfo_ = None
_lobbyGood_ = None
_lv_ = None
_miniMap_ = None
_mobSpawn_ = None
_modAttr_ = None
_model_ = None
_mouseHook_ = None
_moveTo_ = None
_msg_ = None
_name_ = None
_neApi_ = None
_offHand_ = None
_operation_ = None
_particleControl_ = None
_particleEntityBind_ = None
_particleNativeEntityBoneBind_ = None
_particleSkeletonBind_ = None
_particleSystem_ = None
_particleTrans_ = None
_path_ = None
_persistence_ = None
_pet_ = None
_player_ = None
_playeranim_ = None
_playerView_ = None
_playerKillCount_ = None
_portal_ = None
_pos_ = None
_postprocess_ = None
_queryVariable_ = None
_projectile_ = None
_recipe_ = None
_redStone_ = None
_research_ = None
_ride_ = None
_rot_ = None
_scale_ = None
_seasonMod_ = None
_shareables_ = None
_Shop_ = None
_sign_ = None
_simpleMsg_ = None
_skyRender_ = None
_spawn_ = None
_speed_ = None
_storyline_ = None
_systemAudio_ = None
_tag_ = None
_tame_ = None
_team_ = None
_teamId_ = None
_textBoard_ = None
_textNotifyClient_ = None
_time_ = None
_totalKillCount_ = None
_type_ = None
_vDeliverComp_ = None
_virtualWorld_ = None
_weather_ = None

if ModBE.isServer():
    _factory = extraServerApi.GetEngineCompFactory()
    _achievement = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "achievement"})
    _action = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "action"})
    _actorCollidable = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "actorCollidable"})
    _actorLoot = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "actorLoot"})
    _actorMotion = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "actorMotion"})
    _actorOwner = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "actorOwner"})
    _actorPushable = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "actorPushable"})
    _armorSlot = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "armorSlot"})
    _attr = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "attr"})
    _auxValue = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "auxValue"})
    _biome = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "biome"})
    _block = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "block"})
    _blockEntityData = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "blockEntityData"})
    _blockInfo = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "blockInfo"})
    _blockState = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "blockState"})
    _blockUseEventWhiteList = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "blockUseEventWhiteList"})
    _breath = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "breath"})
    _buff = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "buff"})
    _bulletAttributes = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "bulletAttributes"})
    _carried = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "carried"})
    _chatExtension = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "chatExtension"})
    _chestBlock = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "chestBlock"})
    _chunkSource = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "chunkSource"})
    _collisionBox = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "collisionBox"})
    _command = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "command"})
    _controlAi = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "controlAi"})
    _customItem = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "customItem"})
    _deathCount = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "deathCount"})
    _dimension = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "dimension"})
    _effect = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "effect"})
    _engineType = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "engineType"})
    _entityComponent = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "entityComponent"})
    _entityEvent = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "entityEvent"})
    _exp = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "exp"})
    _explosion = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "explosion"})
    _extraData = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "extraData"})
    _feature = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "feature"})
    _fly = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "fly"})
    _game = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "game"})
    _gravity = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "gravity"})
    _health = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "health"})
    _httpToServer = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "httpToServer"})
    _hurt = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "hurt"})
    _interact = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "interact"})
    _inventory = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "inventory"})
    _item = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "item"})
    _itembanned = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "itembanned"})
    _itemInfo = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "itemInfo"})
    _lobbyGood = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "lobbyGood"})
    _lv = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "lv"})
    _mobSpawn = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "mobSpawn"})
    _modAttr = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "modAttr"})
    _model = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "model"})
    _moveTo = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "moveTo"})
    _msg = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "msg"})
    _name = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "name"})
    _neApi = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "neApi"})
    _offHand = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "offHand"})
    _persistence = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "persistence"})
    _pet = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "pet"})
    _player = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "player"})
    _playerKillCount = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "playerKillCount"})
    _portal = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "portal"})
    _pos = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "pos"})
    _projectile = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "projectile"})
    _recipe = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "recipe"})
    _redStone = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "redStone"})
    _ride = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "ride"})
    _rot = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "rot"})
    _scale = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "scale"})
    _seasonMod = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "seasonMod"})
    _shareables = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "shareables"})
    _sign = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "sign"})
    _simpleMsg = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "simpleMsg"})
    _spawn = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "spawn"})
    _speed = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "speed"})
    _storyline = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "storyline"})
    _systemAudio = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "systemAudio"})
    _tag = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "tag"})
    _tame = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "tame"})
    _team = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "team"})
    _teamId = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "teamId"})
    _time = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "time"})
    _totalKillCount = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "totalKillCount"})
    _type = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "type"})
    _vDeliverComp = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "vDeliverComp"})
    _weather = functools.partial(server.CreateComponent, **{"nameSpace": "Minecraft", "name": "weather"})

    _achievement_ = _achievement(extraServerApi.GetLevelId())
    _action_ = _action(extraServerApi.GetLevelId())
    _actorCollidable_ = _actorCollidable(extraServerApi.GetLevelId())
    _actorLoot_ = _actorLoot(extraServerApi.GetLevelId())
    _actorMotion_ = _actorMotion(extraServerApi.GetLevelId())
    _actorOwner_ = _actorOwner(extraServerApi.GetLevelId())
    _actorPushable_ = _actorPushable(extraServerApi.GetLevelId())
    _armorSlot_ = _armorSlot(extraServerApi.GetLevelId())
    _attr_ = _attr(extraServerApi.GetLevelId())
    _auxValue_ = _auxValue(extraServerApi.GetLevelId())
    _biome_ = _biome(extraServerApi.GetLevelId())
    _block_ = _block(extraServerApi.GetLevelId())
    _blockEntityData_ = _blockEntityData(extraServerApi.GetLevelId())
    _blockInfo_ = _blockInfo(extraServerApi.GetLevelId())
    _blockState_ = _blockState(extraServerApi.GetLevelId())
    _blockUseEventWhiteList_ = _blockUseEventWhiteList(extraServerApi.GetLevelId())
    _breath_ = _breath(extraServerApi.GetLevelId())
    _buff_ = _buff(extraServerApi.GetLevelId())
    _bulletAttributes_ = _bulletAttributes(extraServerApi.GetLevelId())
    _carried_ = _carried(extraServerApi.GetLevelId())
    _chatExtension_ = _chatExtension(extraServerApi.GetLevelId())
    _chestBlock_ = _chestBlock(extraServerApi.GetLevelId())
    _chunkSource_ = _chunkSource(extraServerApi.GetLevelId())
    _collisionBox_ = _collisionBox(extraServerApi.GetLevelId())
    _command_ = _command(extraServerApi.GetLevelId())
    _controlAi_ = _controlAi(extraServerApi.GetLevelId())
    _customItem_ = _customItem(extraServerApi.GetLevelId())
    _deathCount_ = _deathCount(extraServerApi.GetLevelId())
    _dimension_ = _dimension(extraServerApi.GetLevelId())
    _effect_ = _effect(extraServerApi.GetLevelId())
    _engineType_ = _engineType(extraServerApi.GetLevelId())
    _entityComponent_ = _entityComponent(extraServerApi.GetLevelId())
    _entityEvent_ = _entityEvent(extraServerApi.GetLevelId())
    _exp_ = _exp(extraServerApi.GetLevelId())
    _explosion_ = _explosion(extraServerApi.GetLevelId())
    _extraData_ = _extraData(extraServerApi.GetLevelId())
    _feature_ = _feature(extraServerApi.GetLevelId())
    _fly_ = _fly(extraServerApi.GetLevelId())
    _game_ = _game(extraServerApi.GetLevelId())
    _gravity_ = _gravity(extraServerApi.GetLevelId())
    _health_ = _health(extraServerApi.GetLevelId())
    _httpToServer_ = _httpToServer(extraServerApi.GetLevelId())
    _hurt_ = _hurt(extraServerApi.GetLevelId())
    _interact_ = _interact(extraServerApi.GetLevelId())
    _inventory_ = _inventory(extraServerApi.GetLevelId())
    _item_ = _item(extraServerApi.GetLevelId())
    _itembanned_ = _itembanned(extraServerApi.GetLevelId())
    _itemInfo_ = _itemInfo(extraServerApi.GetLevelId())
    _lobbyGood_ = _lobbyGood(extraServerApi.GetLevelId())
    _lv_ = _lv(extraServerApi.GetLevelId())
    _mobSpawn_ = _mobSpawn(extraServerApi.GetLevelId())
    _modAttr_ = _modAttr(extraServerApi.GetLevelId())
    _model_ = _model(extraServerApi.GetLevelId())
    _moveTo_ = _moveTo(extraServerApi.GetLevelId())
    _msg_ = _msg(extraServerApi.GetLevelId())
    _name_ = _name(extraServerApi.GetLevelId())
    _neApi_ = _neApi(extraServerApi.GetLevelId())
    _offHand_ = _offHand(extraServerApi.GetLevelId())
    _persistence_ = _persistence(extraServerApi.GetLevelId())
    _pet_ = _pet(extraServerApi.GetLevelId())
    _player_ = _player(extraServerApi.GetLevelId())
    _playerKillCount_ = _playerKillCount(extraServerApi.GetLevelId())
    _portal_ = _portal(extraServerApi.GetLevelId())
    _pos_ = _pos(extraServerApi.GetLevelId())
    _projectile_ = _projectile(extraServerApi.GetLevelId())
    _recipe_ = _recipe(extraServerApi.GetLevelId())
    _redStone_ = _redStone(extraServerApi.GetLevelId())
    _ride_ = _ride(extraServerApi.GetLevelId())
    _rot_ = _rot(extraServerApi.GetLevelId())
    _scale_ = _scale(extraServerApi.GetLevelId())
    _seasonMod_ = _seasonMod(extraServerApi.GetLevelId())
    _shareables_ = _shareables(extraServerApi.GetLevelId())
    _sign_ = _sign(extraServerApi.GetLevelId())
    _simpleMsg_ = _simpleMsg(extraServerApi.GetLevelId())
    _spawn_ = _spawn(extraServerApi.GetLevelId())
    _speed_ = _speed(extraServerApi.GetLevelId())
    _storyline_ = _storyline(extraServerApi.GetLevelId())
    _systemAudio_ = _systemAudio(extraServerApi.GetLevelId())
    _tag_ = _tag(extraServerApi.GetLevelId())
    _tame_ = _tame(extraServerApi.GetLevelId())
    _team_ = _team(extraServerApi.GetLevelId())
    _teamId_ = _teamId(extraServerApi.GetLevelId())
    _time_ = _time(extraServerApi.GetLevelId())
    _totalKillCount_ = _totalKillCount(extraServerApi.GetLevelId())
    _type_ = _type(extraServerApi.GetLevelId())
    _vDeliverComp_ = _vDeliverComp(extraServerApi.GetLevelId())
    _weather_ = _weather(extraServerApi.GetLevelId())
if ModBE.isClient():
    _factory = extraClientApi.GetEngineCompFactory()
    _action = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "action"})
    _actorCollidable = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "actorCollidable"})
    _actorMotion = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "actorMotion"})
    _actorRender = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "actorRender"})
    _attr = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "attr"})
    _auxValue = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "auxValue"})
    _biome = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "biome"})
    _block = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "block"})
    _blockGeometry = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "blockGeometry"})
    _blockInfo = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "blockInfo"})
    _blockUseEventWhiteList = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "blockUseEventWhiteList"})
    _brightness = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "brightness"})
    _bulletAttributes = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "bulletAttributes"})
    _camera = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "camera"})
    _carried = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "carried"})
    _chunkSource = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "chunkSource"})
    _cloudMusic = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "cloudMusic"})
    _collisionBox = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "collisionBox"})
    _config = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "config"})
    _customAudio = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "customAudio"})
    _customItem = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "customItem"})
    _device = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "device"})
    _effect = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "effect"})
    _effectInfo = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "effectInfo"})
    _engineEffectBindControl = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "engineEffectBindControl"})
    _engineType = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "engineType"})
    _fog = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "fog"})
    _frameAniControl = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "frameAniControl"})
    _frameAniEntityBind = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "frameAniEntityBind"})
    _frameAniNativeEntityBoneBind = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "frameAniNativeEntityBoneBind"})
    _frameAniSkeletonBind = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "frameAniSkeletonBind"})
    _frameAniTrans = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "frameAniTrans"})
    _game = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "game"})
    _health = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "health"})
    _inventory = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "inventory"})
    _item = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "item"})
    _miniMap = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "miniMap"})
    _modAttr = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "modAttr"})
    _model = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "model"})
    _mouseHook = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "mouseHook"})
    _name = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "name"})
    _neApi = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "neApi"})
    _offHand = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "offHand"})
    _operation = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "operation"})
    _particleControl = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "particleControl"})
    _particleEntityBind = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "particleEntityBind"})
    _particleNativeEntityBoneBind = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "particleNativeEntityBoneBind"})
    _particleSkeletonBind = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "particleSkeletonBind"})
    _particleSystem = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "particleSystem"})
    _particleTrans = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "particleTrans"})
    _path = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "path"})
    _player = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "player"})
    _playeranim = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "playeranim"})
    _playerView = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "playerView"})
    _pos = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "pos"})
    _postprocess = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "postprocess"})
    _queryVariable = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "queryVariable"})
    _recipe = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "recipe"})
    _research = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "research"})
    _ride = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "ride"})
    _rot = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "rot"})
    _seasonMod = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "seasonMod"})
    _Shop = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "Shop"})
    _skyRender = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "skyRender"})
    _systemAudio = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "systemAudio"})
    _tame = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "tame"})
    _textBoard = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "textBoard"})
    _textNotifyClient = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "textNotifyClient"})
    _time = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "time"})
    _type = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "type"})
    _virtualWorld = functools.partial(client.CreateComponent, **{"nameSpace": "Minecraft", "name": "virtualWorld"})

    _action_ = _action(extraClientApi.GetLevelId())
    _actorCollidable_ = _actorCollidable(extraClientApi.GetLevelId())
    _actorMotion_ = _actorMotion(extraClientApi.GetLevelId())
    _actorRender_ = _actorRender(extraClientApi.GetLevelId())
    _attr_ = _attr(extraClientApi.GetLevelId())
    _auxValue_ = _auxValue(extraClientApi.GetLevelId())
    _biome_ = _biome(extraClientApi.GetLevelId())
    _block_ = _block(extraClientApi.GetLevelId())
    _blockGeometry_ = _blockGeometry(extraClientApi.GetLevelId())
    _blockInfo_ = _blockInfo(extraClientApi.GetLevelId())
    _blockUseEventWhiteList_ = _blockUseEventWhiteList(extraClientApi.GetLevelId())
    _brightness_ = _brightness(extraClientApi.GetLevelId())
    _bulletAttributes_ = _bulletAttributes(extraClientApi.GetLevelId())
    _camera_ = _camera(extraClientApi.GetLevelId())
    _carried_ = _carried(extraClientApi.GetLevelId())
    _chunkSource_ = _chunkSource(extraClientApi.GetLevelId())
    _cloudMusic_ = _cloudMusic(extraClientApi.GetLevelId())
    _collisionBox_ = _collisionBox(extraClientApi.GetLevelId())
    _config_ = _config(extraClientApi.GetLevelId())
    _customAudio_ = _customAudio(extraClientApi.GetLevelId())
    _customItem_ = _customItem(extraClientApi.GetLevelId())
    _device_ = _device(extraClientApi.GetLevelId())
    _effect_ = _effect(extraClientApi.GetLevelId())
    _effectInfo_ = _effectInfo(extraClientApi.GetLevelId())
    _engineEffectBindControl_ = _engineEffectBindControl(extraClientApi.GetLevelId())
    _engineType_ = _engineType(extraClientApi.GetLevelId())
    _fog_ = _fog(extraClientApi.GetLevelId())
    _frameAniControl_ = _frameAniControl(extraClientApi.GetLevelId())
    _frameAniEntityBind_ = _frameAniEntityBind(extraClientApi.GetLevelId())
    _frameAniNativeEntityBoneBind_ = _frameAniNativeEntityBoneBind(extraClientApi.GetLevelId())
    _frameAniSkeletonBind_ = _frameAniSkeletonBind(extraClientApi.GetLevelId())
    _frameAniTrans_ = _frameAniTrans(extraClientApi.GetLevelId())
    _game_ = _game(extraClientApi.GetLevelId())
    _health_ = _health(extraClientApi.GetLevelId())
    _inventory_ = _inventory(extraClientApi.GetLevelId())
    _item_ = _item(extraClientApi.GetLevelId())
    _miniMap_ = _miniMap(extraClientApi.GetLevelId())
    _modAttr_ = _modAttr(extraClientApi.GetLevelId())
    _model_ = _model(extraClientApi.GetLevelId())
    _mouseHook_ = _mouseHook(extraClientApi.GetLevelId())
    _name_ = _name(extraClientApi.GetLevelId())
    _neApi_ = _neApi(extraClientApi.GetLevelId())
    _offHand_ = _offHand(extraClientApi.GetLevelId())
    _operation_ = _operation(extraClientApi.GetLevelId())
    _particleControl_ = _particleControl(extraClientApi.GetLevelId())
    _particleEntityBind_ = _particleEntityBind(extraClientApi.GetLevelId())
    _particleNativeEntityBoneBind_ = _particleNativeEntityBoneBind(extraClientApi.GetLevelId())
    _particleSkeletonBind_ = _particleSkeletonBind(extraClientApi.GetLevelId())
    _particleSystem_ = _particleSystem(extraClientApi.GetLevelId())
    _particleTrans_ = _particleTrans(extraClientApi.GetLevelId())
    _path_ = _path(extraClientApi.GetLevelId())
    _player_ = _player(extraClientApi.GetLevelId())
    _playeranim_ = _playeranim(extraClientApi.GetLevelId())
    _playerView_ = _playerView(extraClientApi.GetLevelId())
    _pos_ = _pos(extraClientApi.GetLevelId())
    _postprocess_ = _postprocess(extraClientApi.GetLevelId())
    _queryVariable_ = _queryVariable(extraClientApi.GetLevelId())
    _recipe_ = _recipe(extraClientApi.GetLevelId())
    _research_ = _research(extraClientApi.GetLevelId())
    _ride_ = _ride(extraClientApi.GetLevelId())
    _rot_ = _rot(extraClientApi.GetLevelId())
    _seasonMod_ = _seasonMod(extraClientApi.GetLevelId())
    _Shop_ = _Shop(extraClientApi.GetLevelId())
    _skyRender_ = _skyRender(extraClientApi.GetLevelId())
    _systemAudio_ = _systemAudio(extraClientApi.GetLevelId())
    _tame_ = _tame(extraClientApi.GetLevelId())
    _textBoard_ = _textBoard(extraClientApi.GetLevelId())
    _textNotifyClient_ = _textNotifyClient(extraClientApi.GetLevelId())
    _time_ = _time(extraClientApi.GetLevelId())
    _type_ = _type(extraClientApi.GetLevelId())
    _virtualWorld_ = _virtualWorld(extraClientApi.GetLevelId())
