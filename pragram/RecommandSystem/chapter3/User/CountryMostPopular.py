from .MostPopular import *

def CountryMostPopular(train, profile, N):
    '''
    :param train:
    :param profile:
    :param N:
    :return:
    '''
    # 分城市进行统计
    items = {}
    for user in train:
        country = profile[user]['country']
        if country not in items:
            items[country] = {}
        for item in train[user]:
            if item not in items[country]:
                items[country][item] = 0
            items[country][item] += 1
    for country in items:
        items[country] = list(sorted(items[country].items(), key=lambda x: x[1], reverse=True))

    mostPopular = MostPopular(train, profile, N)

    # 获取接口函数
    def GetRecommendation(user):
        seen_items = set(train[user]) if user in train else set()
        country = profile[user]['country']
        if country in items:
            recs = [x for x in items[country] if x[0] not in seen_items][:N]
        else:
            recs = mostPopular(user)
        return recs

    return GetRecommendation