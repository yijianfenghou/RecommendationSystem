import numpy as np
from copy import copy

def LFM(train, ratio, K, lr, step, lmda, N):
    '''
    :param train: 训练数据
    :param ratio: 负采样的正负比例
    :param K: 隐语义个数
    :param lr: 初始学习率
    :param step: 迭代次数
    :param lmda: 正则化系数
    :param N: 推荐TopN物品的个数
    :return: GetRecommendation,获取推荐结果的接口
    '''
    all_items = {}
    for user in train:
        for item in train[user]:
            if item not in all_items:
                all_items[item] = 0
            all_items[item] += 1

    all_items = list(all_items.items())
    items = [x[0] for x in all_items]
    pops = [x[1] for x in all_items]

    ### 负采样函数(注意！！！要按照流行度进行采样)
    def nSample(data, ratio):
        new_data = {}
        #正样本
        for user in data:
            if user not in new_data:
                new_data[user] = {}
            for item in data[user]:
                new_data[user][item] = 1

        #负样本
        for user in data:
            seen = set(new_data[user])
            pos_num = len(seen)
            item = np.random.choice(items,int(pos_num*ratio*3),pops)
            item = [x for x in item if x not in seen][:int(pos_num*ratio)]
            new_data[user].update({x: 0 for x in item})
        return new_data

    # 训练
    P, Q = {}, {}
    for user in train:
        P[user] = np.random.random(K)
    for item in items:
        Q[item] = np.random.random(K)

    for s in range(step):
        data = nSample(train, ratio)
        for user in data:
            for item in data[user]:
                eui = data[user][item] - (P[user]*Q[user]).sum()
                saveP = copy(P[user])
                P[user] += lr * (Q[item]*eui - lmda*P[user])
                Q[item] += lr * (saveP*eui - lmda*Q[item])

        lr *= 0.9

    # 获取接口函数
    def GetRecommendation(user):
        seen_items = set(train[set])
        recs = {}
        for item in items:
            if item not in seen_items:
                recs[item] = (P[user]*Q[item]).sum()
        recs = list(sorted(recs.items(), key=lambda x: x[1], reverse=True))[:N]

    return GetRecommendation
