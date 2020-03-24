import math

def ExpandtagBased(train, N, M=20):
    '''
    :param train:
    :param N:
    :param M:
    :return:
    '''
    # 计算标签之间的相似度
    item_tag = {}
    for user in train:
        for item in train[user]:
            if item not in item_tag:
                item_tag[item] = set()
            for tag in train[user][item]:
                item_tag[item].add(tag)

    tag_sim, tag_cnt = {}, {}
    for item in item_tag:
        for u in item_tag[item]:
            if u not in tag_cnt:
                tag_cnt[u] = 0
            tag_cnt[tag] += 1
            if u not in tag_sim:
                tag_sim[u] = {}
            for v in item_tag[item]:
                if u == v:
                    continue
                if v not in tag_sim[u]:
                    tag_sim[u][v] = 0
                tag_sim[u][v] += 1

    for u in tag_sim:
        for v in tag_sim[u]:
            tag_sim[u][v] /= math.sqrt(tag_cnt[u]*tag_cnt[v])


    # 为每个用户扩展标签
    user_tags = {}
    for user in train:
        if user not in user_tags:
            user_tags[user] = {}
        for item in train[user]:
            for tag in train[user][item]:
                if tag not in user_tags[user]:
                    user_tags[user][tag] = 0
                user_tags[user][tag] += 1
    expand_tags = {}
    for user in user_tags:
        if len(user_tags[user]) >= M:
            if user not in expand_tags:
                expand_tags[user] = {}
            expand_tags[user] = user_tags[user]
            continue
        # 不满足M个的进行标签扩展
        expand_tags[user] = {}
        seen_tags = set(user_tags[user])
        for tag in user_tags[user]:
            for t in tag_sim[tag]:
                if t in seen_tags:
                    continue
                if t not in expand_tags[user]:
                    expand_tags[user][t] = 0
                expand_tags[user][t] += user_tags[user][tag] * tag_sim[tag][t]
        expand_tags[user].update(user_tags[user])
        expand_tags[user] = dict(list(sorted(expand_tags[user].items(), key=lambda x: x[1], reverse=True))[:M])

    # SimpleTagBased算法
    tag_items = {}
    for user in train:
        for item in train[user]:
            for tag in train[user][item]:
                if tag not in tag_items:
                    tag_items[tag] = {}
                if item not in tag_items[tag]:
                    tag_items[tag][item] = 0
                tag_items[tag][item] += 1

    def GetRecommendation(user):
        # 按照打分推荐N个未见过的
        if user not in user_tags:
            return []
        seen_items = set(train[user])
        items_score = {}
        for tag in expand_tags[user]:
            for item in tag_items[tag]:
                if item in seen_items:
                    continue
                if item not in items_score:
                    items_score[item] = 0
                items_score[item] += expand_tags[user][tag]*tag_items[tag][item]
        items_score = list(sorted(items_score.items(), key=lambda x: x[1], reverse=True))
        return items_score[:N]

    return GetRecommendation






