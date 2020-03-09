
def MostPopular(train, K, N):
    '''
    :param train:
    :param K:
    :param N:
    :return:GetRecommendation
    '''
    items = {}
    for user in train:
        for item in train[user]:
            if item not in items:
                items[item] = 0
            items[item] += 1

    def GetRecommendation(user):
        #随机推荐N个没见过的最热门的
        user_items = set(train[user])
        rec_items = {k: items[k] for k in items if k not in user_items}
        rec_items = list(sorted(rec_items.items(), key=lambda x: x[1], reverse=True))
        return rec_items[:N]

    return GetRecommendation