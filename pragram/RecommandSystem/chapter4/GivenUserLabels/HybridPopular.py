from .Popular import *

def HybridPopular(train, N, alpha):
    '''
    :param train:
    :param N:
    :return:
    '''
    # 统计user_tags
    user_tags ,item_tags = {}, {}
    for user in train:
        if user not in user_tags:
            user_tags[user] = {}
        for item in train[user]:
            if item not in item_tags:
                item_tags[item] = {}
            for tag in train[user][item]:
                if tag not in user_tags[user]:
                    user_tags[user][tag] = 0
                if tag not in item_tags[item]:
                    item_tags[user][tag] = 0
            user_tags[user][tag] += 1
            item_tags[item][tag] += 1

    def GetRecommendation(user, item):
        tag_score = {}
        if user in user_tags:
            max_user_tag = max(user_tags[user].values())
            for tag in user_tags[user]:
                if tag not in tag_score:
                    tag_score[tag] = 0
                tag_score[tag] += (1-alpha) * user_tags[user][tag] / max_user_tag

        if item in item_tags:
            max_item_tag = max(item_tags[user].values())
            for tag in item_tags[user]:
                if tag in tag_score:
                    tag_score[tag] = 0
                tag_score[tag] += alpha*item_tags[item][tag] / max_item_tag

        return list(sorted(tag_score.items(), key=lambda x: x[1], reverse=True))[:N]

    return GetRecommendation

