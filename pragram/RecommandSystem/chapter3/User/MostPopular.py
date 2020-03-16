
def MostPopular(train, profile, N):
    '''
    :param train:
    :param profile: 用户的注册信息
    :param N: 推荐TopN物品的个数
    :return:
    '''
    items = {}
    for user in train:
        for item in train[user]:
            if item not in items:
                items[item] = 0
            items[item] += 1
    items = list(sorted(items.items(), key=lambda x: x[1], reverse=True))

    # 获取接口函数
    def GetRemmendation(user):
        seen_items = set(train[user]) if user in train else set()
        recs = [item for item in items if item[0] not in seen_items][:N]
        return recs

    return GetRemmendation



