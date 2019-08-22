# Streaming Dataframe聚合由三种方法构建
#
# initial：给定一个空的示例数据帧，创建初始状态
# on_new：更新状态并生成新结果以发出给定的新数据
# on_old：更新状态并生成新结果以发出给定的衰减数据