from .Popular import *

def ItemPopular(train, N):
    '''
    :param train:
    :param N:
    :return:
    '''
    item_tags = {}
    for user in train:
        for item in train[user]:
            for tag in train[user][item]:
                if item not in item_tags:
                    item_tags[item] = {}
                if tag not in item_tags[item]:
                    item_tags[item][tag] = 0
                item_tags[item][tag] += 1

    item_tags = {k: list(sorted(v.items(),key = lambda x: x[1], reverse = True)) for k, v in item_tags.items()}

    def GetRecommendation(user, item):
        if item in item_tags:
            return item_tags[item][:N]
        else:
            return Popular(train, N)

    return GetRecommendation