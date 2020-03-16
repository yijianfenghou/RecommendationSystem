import math

def ItemCFNorm(train, K, N):
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
                sim[user_contains_item][other_user_contains_item] += 1

    for user_contains_item in sim:
        for other_user_contains_item in sim[user_contains_item]:
            sim[user_contains_item][other_user_contains_item] /= math.sqrt(num(user_contains_item)*num(other_user_contains_item))

    # 对相似度矩阵进行按行归一化
    for user_contains_item in sim:
        s = 0
        for other_user_contains_item in sim[user_contains_item]:
            s += sim[user_contains_item][other_user_contains_item]
        if s > 0:
            for other_user_contains_item in sim[user_contains_item]:
                sim[user_contains_item][other_user_contains_item] /= s

    # 按照相似度排序
    sorted_item_sim = {k: list(sorted(v.items(), key=lambda x: x[1], reverse=True)) for k, v in sim.items()}

    # 获取接口函数
    def GetRecommendation(user):
        items = {}
        seen_items = set(train[user])
        for item in train[user]:
            for other_user_contains_item, _ in sim[item].items():
                if other_user_contains_item not in seen_items:
                    if other_user_contains_item not in items:
                        items[other_user_contains_item] = 0
                    items[other_user_contains_item] += sim[item][other_user_contains_item]
        recs = list(sorted(items.values(), key=lambda x: x[1], reverse=True))[:N]
        return recs

    return GetRecommendation