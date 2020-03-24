
def SimpleTagBased(train, N):
    '''
    :param train: 训练数据
    :param N: 超参数，设置取TopN推荐物品数目
    :return:
    '''
    # 统计user_tags和tag_items0
    user_tags, tag_items = {}, {}
    for user in train:
        user_tags[user] = {}
        for item in train[user]:
            for tag in train[user][item]:
                if tag not in user_tags[user][tag]:
                    user_tags[user][tag] = 0
                user_tags[user][tag] += 1
                if tag not in tag_items:
                    tag_items[tag] = {}
                if item not in tag_items[tag]:
                    tag_items[tag][item] = 0
                tag_items[tag][item] += 1

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
                item_score[item] += user_tags[user][tag]*tag_items[tag][item]
        item_score = list(sorted(item_score.items(), key=lambda x: x[1], reverse=True))[:N]
        return item_score

    return GetRecommendation

