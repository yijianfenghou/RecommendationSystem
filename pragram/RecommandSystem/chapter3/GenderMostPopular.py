from .MostPopular import *

def GenderMostPopular(train, profile, N):
    '''
    :param train: 训练数据
    :param profile: 用户注册信息
    :param N: 推荐TopN物品的个数
    :return:
    '''
    mitems, fitems = {}, {}
    for user in train:
        if profile[user]['gender'] == 'm':
            tmp = mitems
        elif profile[user]['gender'] == 'f':
            tmp = fitems
        for item in train[user]:
            if item not in tmp:
                tmp[item] = 0
            tmp[item] += 1

    mitems = list(sorted(mitems.items(), key=lambda x:x[1], reverse=True))
    fitems = list(sorted(fitems.items(), key=lambda x: x[1],reverse=True))

    mostPopular = MostPopular(train, profile, N)

    # 获取接口函数
    def GetRecommendation(user):
        seen_items = set(train[user]) if user in train else set()
        if profile[user]['gender'] == 'm':
            recs = [x for x in mitems if x[0] not in seen_items][:N]
        elif profile[user]['gender'] == 'f':
            recs = [x for x in fitems if x[0] not in seen_items][:N]
        else:
            recs = mostPopular(user)
        return recs

    return GetRecommendation