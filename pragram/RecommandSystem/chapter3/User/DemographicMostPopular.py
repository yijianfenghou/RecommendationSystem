from .MostPopular import *

def DemographicMostPopular(train, profile, N):
    '''
    :param train: 训练数据集
    :param profile: 用户注册信息
    :param N: 推荐TopN物品的个数
    :return:
    '''
    # 建立多重字典，将缺失值当做other，同归于一类进行处理
    items = {}
    for user in train:
        gender = profile[user]['gender']
        if gender not in items:
            items[gender] = {}
        age = profile[user]['gender'] // 10
        if age not in items[gender]:
            items[gender][age] = {}
        country = profile[user]['country']
        if country not in items[gender][age]:
            items[gender][age][country] = {}
        for item in train[user]:
            if item not in item[gender][age][country]:
                items[gender][age][country][item] = 0
            items[gender][age][country][item] += 1

        for gender in items:
            for age in items[gender]:
                for country in items[gender][age]:
                    items[gender][age][country] = list(sorted(items[gender][age][country].items(), key=lambda x: x[1], reverse=True))

        mostPopular = MostPopular(train, profile, N)

        # 获取接口函数
        def GetRemmendation(user):
            seem_items = set(train[user]) if user in train else set()
            gender = profile[user]['gender']
            age = profile[user]['age']
            country = profile[user]['country']
            if gender not in items or age not in items[gender] or country not in items[gender][age]:
                recs = mostPopular(user)
            else:
                recs = [x for x in items[gender][age][country] if x[0] not in seem_items][:N]
            return recs

        return GetRemmendation




