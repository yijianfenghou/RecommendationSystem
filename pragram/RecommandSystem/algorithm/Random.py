import random

def Random(train, K, N):
    '''
    :param train:
    :param K:
    :param N:
    :return: GetRecommendation，推荐接口函数
    '''
    items = {}
    for user in train:
        for item in train[user]:
            items[item] = 1

    def GetRecommendation(user):
        #随机推荐N个未见过的
        user_items = set(train[user])
        rec_items = {k: items[k] for k in items if k not in user_items}
        rec_items = list(rec_items.items())
        random.shuffle(rec_items)
        return rec_items[:N]

    return GetRecommendation