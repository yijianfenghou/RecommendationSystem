from .MostPopular import *

def AgeMostPopular(train, profile, N):
    ages = []
    for user in profile:
        if profile[user]['age'] >= 0:
            ages.append(profile[user]['age'])
    maxAge, minAge = max(ages), min(ages)
    items = [{} for _ in range(int(maxAge // 10 + 1))]

    # 分年龄段进行统计
    for user in train:
        if profile[user]['age'] >= 0:
            age = profile[user]['age'] // 10
            for item in train[user]:
                if item not in items[age]:
                    items[age][item] = 0
                items[age][item] += 1

    for i in range(len(items)):
        items[i] = list(sorted(items[i].items(), key=lambda x: x[1], reverse=True))

    mostPopular = MostPopular(train, profile, N)

    # 获取接口函数
    def GetRemmendation(user):
        seen_items = set(train[user]) if user in train else set()
        if profile[user]['age'] >= 0:
            age = profile[user]['age'] // 10
            # 年龄信息异常，按照全局推荐
            if age >= len(items) or len(items[age]) == 0:
                recs = mostPopular(user)
            else:
                recs = [x for x in items[age] if x[0] not in seen_items][:N]
        else:
            recs = mostPopular(user)
        return recs

    return GetRemmendation
