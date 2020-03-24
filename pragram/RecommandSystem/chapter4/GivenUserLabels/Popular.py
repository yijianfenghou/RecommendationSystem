
# 推荐热门标签
def Popular(train, N):
    '''
    :param train: 训练数据集
    :param N: 超参数，设置取TopN推荐物品数目
    :return: GetRecommendation,推荐接口函数
    '''
    # 统计tags
    tags = {}
    for user in train:
        for item in train[user]:
            for tag in train[user][item]:
                if tag not in tags:
                    tags[tag] = 0
                tags[tag] += 1

    tags = list(sorted(tags.item(), key=lambda x: x[1], reverse=True))[:N]

    def GetRecommendation(user, item):
        return tags

    return GetRecommendation


