
class Metric():

    def __init__(self, train, test, GetRecommendation):
        '''
        :param train: 训练数据集
        :param test: 测试数据集
        :param GetRecommendation:
        '''
        self.train = train
        self.test = test
        self.GetRecommendation = GetRecommendation
        self.recs = self.getRecs()

    # 为test中的每个用户进行推荐
    def getRecs(self):
        recs = {}
        for user in self.test:
            rank = self.GetRecommendation(user)
            recs[user] = rank
        return recs

    # 定义精确率指标计算方式
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

    # define recall
    def recall(self):
        all, hit = 0, 0
        for user in self.test:
            test_items = set(self.test[user])
            rank = self.recs[user]
            for item, score in rank:
                if item in test_items:
                    hit += 1
            all += len(test_items)
        return round(hit / all*100, 2)

    # 定义覆盖率指标计算公式
    def coverage(self):
        all_item, recom_item = set(), set()
        for user in self.test:
            if user in self.train:
                for item in self.train[user]:
                    all_item.add(item)
            rank = self.recs
            for item, score in rank:
                recom_item.add(item)
        return round(len(recom_item) / len(all_item) * 100, 2)

    def eval(self):
        metrics = {
            'Precision': self.precision(),
            'Recall': self.recall(),
            'Coverage': self.coverage()
        }
        print('Metric:', metrics)
        return metrics