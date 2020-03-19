
def SimpleTagBased(train, N):
    '''
    :param train: 训练数据
    :param N: 超参数，设置取TopN推荐物品数目
    :return:
    '''
    # 统计user_tags和tag_items
