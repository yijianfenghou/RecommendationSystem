import math

def ItemIUF(train, K, N):
    '''
    :param train: 训练数据集
    :param K: 超参数，设置取TopK相似物品数目
    :param N: 超参数，设置取TopN推荐物品数目
    :return:
    '''
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
                other_user_contains_item = items[j]
                if other_user_contains_item not in sim[user_contains_item]:
                    sim[user_contains_item][other_user_contains_item] = 0
                sim[user_contains_item][other_user_contains_item] += 1 / math.log(1 + len(items))

    for user_contains_item in sim:
        for other_user_contains_item in sim[user_contains_item]:
            sim[user_contains_item][other_user_contains_item] /= math.sqrt(num[user_contains_item]*num[other_user_contains_item])

    # 按照相似度排序
    sorted_item_sim = {k: list(sorted(v.items(), key=lambda x: x[1], reverse=True)) for k, v in sim.items()}

    # 获取接口函数
    def GetRecommendation(user):
        items = {}
        seen_items = set(train[user])
        for item in train[user]:
            for other_user_contains_item, _ in sorted_item_sim[item][:K]:
                '''
                要去掉用户见过的
                '''
                if other_user_contains_item not in seen_items:
                    if other_user_contains_item not in items:
                        items[other_user_contains_item] = 0
                    items[other_user_contains_item] += sim[item][other_user_contains_item]
        recs = list(sorted(items.items(), key=lambda x: x[1], reverse=True))[:N]
        return recs

    return GetRecommendation
