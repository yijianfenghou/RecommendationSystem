
def TagBasedTFIDF(train, N):
    '''
    :param train:
    :param N:
    :return:
    '''
    # 统计user_tags和tag_items
    user_tags, tag_items = {}, {}
    # 统计标签的热门程度，即打过此标签的不同用户数
    tag_pop = {}
    for user in train:
        user_tags[user] = {}
        for item in train[user]:
            for tag in train[user][item]:
                if tag not in user_tags[user]:
                    user_tags[user][tag] = 0
                user_tags[user][tag] += 1
                if tag not in tag_items:
                    tag_items[tag] = {}
                if item not in tag_items[tag]:
                    tag_items[tag][item] = 0
                tag_items[tag][item] += 1
                if tag not in tag_pop:
                    tag_pop[tag] = set()
                tag_pop[tag].add(user)

    tag_pop = {k: len(v) for k, v in tag_pop.items()}

    def GetRecommendation(user):
        # 按照打分推荐N个未见过的
        if user not in train:
            return []
        seen_items = set(train[user])
        item_score = {}
        for tag in user_tags[user]:
            for item in tag_items[tag]:
                if item in seen_items:
                    continue
                if item not in item_score:
                    item_score[item] = 0
                item_score[item] += user_tags[user][tag]*tag_items[tag][item]/tag_pop[tag]

        item_score = list(sorted(item_score.items(), key=lambda x: x[1], reverse=True))[:N]
        return item_score
    return GetRecommendation