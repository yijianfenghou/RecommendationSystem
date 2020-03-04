import numpy as np
import math
import random
from timer import *
from tqdm import tqdm

class Metric():

    def __init__(self, train, test, GetRecommendation):
        '''
        :param train: 训练数据集
        :param test: 测试数据集
        :param GetRecommendation: 为某个用户获取推荐物品的接口函数
        '''
        self.train = train
        self.test = test
        self.GetRecommendation = GetRecommendation
        self.recs = self.getRec()
    #为test中的每个用户推荐
    def getRec(self):
        recs = {}
        for user in self.test:
            rank = self.GetRecommendation(user)
            recs[user] = rank
        return recs

    # 精确率描述最终的推荐列表中有多少比例是发生过用户-物品评分记录
    # precision = sum_u(R(u)相交于T(u))/sum_u(T(u))
    def precision(self):
        all, hit = 0, 0
        for user in self.test:
            test_items = set(self.test[user])
            rank = self.recs[user]
            for item, score in rank:
                if item in test_items:
                    hit += 1
            all += len(rank)
        return round(hit / all*100, 2)

    #推荐系统的召回率，描述有多少比率的用户-物品记录包含在最终的推荐列表中
    #Recall = sum_u(R(u)相交于T(u))/sum_u(R(u))
    #其中，对用户u推荐N个物品(记为R(u))，令用户u在测试集上喜欢的物品集合为T(u)
    def recall(self):
        hit, all = 0, 0
        for user in self.test:
            test_items = set(self.test[user])
            rank = self.recs[user]
            for item, score in rank:
                if item in test_items:
                    hit += 1
            all += len(test_items)
        return round(hit / all*100, 2)

    #算法覆盖率反映了推荐算法发掘长尾的能力，覆盖率越高，说明推荐算法越能够将长尾中的物品推荐给用户
    #coverage = (并集R(u))/|I|
    #该覆盖率表示最终的推荐列表中包含多大的比例。
    def coverage(self):
        all_item, recom_item = set(), set()
        for user in self.test:
            for item in self.train[user]:
                all_item.add(item)
            rank = self.recs[user]
            for item, score in rank:
                recom_item.add(item)
        return round(len(recom_item) / len(all_item), 2)

    #推荐列表中物品的平均流行度度量推荐结果的新颖度。如果推荐出的物品很热门，说明推荐的新颖度较低。
    def popularity(self):
        #计算物品的流行度
        item_pop = {}
        for user in self.train:
            for item in self.train[user]:
                if item not in item_pop:
                    item_pop[item] = 0
                item_pop[item] += 1

        num, pop = 0, 0
        for user in self.test:
            rank = self.recs[user]
            for item, score in rank:
                #取对数，防止因长尾问题带来的被流行物品所主导
                pop += math.log(1 + item_pop[item])
                num += 1
        return round(pop / num, 6)

    def val 
