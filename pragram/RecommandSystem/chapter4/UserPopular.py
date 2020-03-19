from .Popular import *

def UserPopular(train, N):
    '''
    :param train:
    :param N:
    :return:
    '''
    user_tags = {}
    for user in train:
        for item in train[user]:
            for tag in train[user][item]:
                if user not in user_tags:
                    user_tags[user] = {}
                if tag not in user_tags[user]:
                    user_tags[user][tag] = 0
                user_tags[user][tag] += 1

    user_tags = {k: list(sorted(v.items(), key= lambda x: x[1], reverse=True)) for k, v in user_tags.items()}

    def GetRecommendation(user, item):
        if user in user_tags:
            return user_tags[user][:N]
        else:
            return Popular(train, N)

    return GetRecommendation