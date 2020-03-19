
class Metric():

    def __init__(self, train, test, GetRemmendation):
        '''
        :param train:
        :param test:
        :param GetRemmendation:
        '''
        self.train = train
        self.test = test
        self.Getcommendation = GetRemmendation
        self.recs = self.getRecs()

    # 为test中的每个用户进行推荐
    def getRecs(self):
        recs = {}
        for user in self.test:
            recs[user] = {}
            for item in self.test[user]:
                rank = self.Getcommendation(user, item)
                recs[user][item] = rank
        return recs

    # 定义精确率指标计算公式
    def precision(self):
        all, hit = 0, 0
        for user in self.test:
            for item in self.test[user]:
                test_tags = set(self.test[user][item])
                rank = self.recs[user][item]
                for tag, score in rank:
                    if tag in test_tags:
                        hit += 1
                all += len(rank)
        return round(hit/ all * 100, 2)

    # 定义召回率指标计算公式
    def recall(self):
        all, hit = 0 ,0
        for user in self.test:
            for item in self.test[user]:
                test_tags = set(self.test[user][item])
                rank = self.recs[user][item]
                for tag, score in rank:
                    if tag in test_tags:
                        hit += 1
                all += len(test_tags)
        return round(hit / all * 100, 2)

    def eval(self):
        metrics = {
            'Precision': self.precision(),
            'Recall': self.recall()
        }
        print("Metric:", metrics)
        return metrics
