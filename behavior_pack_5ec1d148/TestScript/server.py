# -*- coding: utf-8 -*-

from modbe.module import *
from modbe.enum import *


def main():
    # Callback.register("entityAdd", entityAdded)  # 目前只加入了一个回调`entityAdded`
    # Callback.register("entityAdd", entityAddedSimple)
    Callback.register("itemUse", itemUsed)


def entityAdded(entity, entityType, pos, dimension, isBaby, itemName, auxValue):
    # type: (Actor, str, Pos, int, bool, str, int) -> None
    """
    参数要写全
    :param entity: 实体，`Actor`类
    :param entityType: 实体类型标识符
    :param pos: 实体坐标，`Pos`类
    :param dimension: 实体所在维度数字ID
    :param isBaby: 实体是否是幼体
    :param itemName: 如果是物品实体，物品的类型标识符
    :param auxValue: 如果是物品实体，物品的附加值
    :return: 无
    """
    ModBE.log(LogType.info, LogLevel.inform, "Test", "Actor Added: %s of type %s.", entity.getUniqueID(),
              entity.getEntityTypeId())
    entity.kill()  # 示例逻辑：实体出生后立马杀死实体


def entityAddedSimple(entity, *args):
    # type: (Actor, Any) -> None
    """
    如果不想写全，就需要末尾有`*args`参数
    :param entity: 实体，`Actor`类
    :param args: 用于接受剩余参数而不报错
    :return: 无
    """
    ModBE.log(LogType.info, LogLevel.inform, "Test", "Actor Added Simple: %s of type %s.", entity.getUniqueID(),
              entity.getEntityTypeId())


def itemUsed(entity, oldName, oldAux):
    print(Block.getStatesFromAux("minecraft:log", 10))
    ModBE.log(LogType.info, LogLevel.inform, "Test", "Actor used Item: %s of type %s.", entity.getUniqueID(),
              entity.getEntityTypeId())
    ModBE.log(LogType.info, LogLevel.inform, "Test", "item Used: type %s and aux %s.", oldName, oldAux)
