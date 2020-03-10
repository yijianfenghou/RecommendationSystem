import math

#基于物品余弦相似度推荐
def ItemCF(train, K, N):
    '''
    :param train: 训练数据集
    :param K: 超参数，设置取TOPK相似物品数目
    :param N: 超参数，设置取TopN推荐物品数目
    :return: GetRecommendation, 推荐接口函数
    '''
    # 计算物品相似度矩阵
    sim = {}
    num = {}
    for user in train:
        items = train[user]
        for i in range(len(items)):
            user_contains_item = items[i]
            if user_contains_item not in num:
                num[user_contains_item] = 0
            num[user_contains_item] += 1
            if user_contains_item not in sim:
                sim[user_contains_item] = {}
            for j in range(len(items)):
                if j == i: continue
                user_contains_other_item = items[j]
                if user_contains_other_item not in sim[user_contains_item]:
                    sim[user_contains_item][user_contains_other_item] = 0
                sim[user_contains_item][user_contains_other_item] += 1
    for user_contains_item in sim:
        for user_contains_other_item in sim[user_contains_item]:
            sim[user_contains_item][user_contains_other_item] /= math.sqrt(num[user_contains_item]*num[user_contains_other_item])

    # 按照相似度排序
    sorted_item_sim = {k: list(sorted(v.items(), key=lambda x: x[1], reverse=True)) for k, v in sim.items()}

    #获取接口函数
    def GetRecommendation(user):
        items = {}
        for item in train[user]:
            for u, _ in sorted_item_sim[item][:K]:
                if u not in train[user]:
                    if u not in items:
                        items[u] = 0
                    items[u] += sim[item][u]
        recs = list(sorted(items.items(), key=lambda x: x[1], reverse=True))[:N]
        return recs

    return GetRecommendation