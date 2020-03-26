import time

def RecentPopular(train, K, N, alpha=1.0, t0=int(time.time())):
    '''
    :param train: 训练数据集
    :param K: 可忽略
    :param N: 超参数，设置取TopN推荐物品的数目
    :param alpha: 时间衰减因子
    :param t0: 当前的时间戳
    :return: GetRecommendation
    '''
    item_score = {}
    for user in train:
        for item, t in train[user]:
            if item not in item_score:
                item_score[item] = 0
            item_score[item] += 1.0/(alpha*(t0-t))

    item_score = list(sorted(item_score.items(), key=lambda x: x[1], reverse=True))

    def GetRecommendation(user):
        # 随机推荐N个未见过的
        seen_items = set(train[user])
        recs_items = [x for x in item_score if x[0] not in seen_items][:N]
        return recs_items

    return GetRecommendation


