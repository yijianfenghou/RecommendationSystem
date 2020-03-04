import math
from operator import itemgetter
import numpy as np
import pandas as pd

#在线个性化推荐系统中，当一个用户A需要个性化推荐时，可以先找到和他相似的用户
#把那些喜欢的、而用户A没有听说过的物品推荐给A

#计算两个用户的兴趣相似度。这里，协同过滤算法主要利用行为数据的相似度计算兴趣的相似度。
#给定用户u和v，令N(u)表示用户u曾经有过正反馈的物品集合，令N(v)为用户v曾经有过正反馈的物品集合
#可以通过Jaccard公式简单地计算u和v的兴趣相似度：w_uv = |N(u)相交N(V)| / |N(u)并于N(v)|
#通过cosine公司计算相似度：w_uv = |N(u)相交N(V)| / math.sqrt(|N(u)|*|N(v)|)
###cosine_similarity:first method
def first_UserSimilarity(train):
    W = dict()
    for u in train.keys():
        for v in train.keys():
            if u == v:
                continue
            W[u][v] = len(train[u] & train[v])
            W[u][v] /= math.sqrt(len(train[u])*len(train[v])*1.0)
    return W

###second method
def second_UserSimilarity(train):
    #build inverse table for item_users
    items_users = dict()
    for u, items in train.items():
        for i in items.keys():
            if i not in items_users:
                items_users[i] = set()
            items_users[i].add(u)

    #calculate co-rated items between users
    C = dict()
    N = dict()
    for i, users in items_users.items():
        for u in users:
            N[u] += 1
            for v in users:
                if u == v:
                    continue
                C[u][v] += 1

    #calculate finial similarity matrix
    W = dict()
    for u, related_users in C.items():
        for v, cuv in related_users.items():
            W[u][v] = cuv / math.sqrt(N[u]*N[v])
    return W

def Recommend(user, train, W, K):
    rank = dict()
    interacted_items = train[user]
    for v, wuv in sorted(W[u].items, key=itemgetter(1), reverse=True)[0:K]:
        for i, rvi in train[v].items:
            if i in interacted_items:
                continue
            rank[i] += wuv*rvi
    return rank

if __name__ == "__main__":
    dic = {'A': ('a', 'b', 'd'), 'B': ('a', 'c'), 'C': ('b', 'e'), 'D': ('c', 'd', 'e')}

