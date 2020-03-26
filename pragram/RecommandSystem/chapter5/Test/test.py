from pragram.RecommandSystem.chapter5.BasedTimeRecommendation.RecentPopular import RecentPopular
from pragram.RecommandSystem.preprocessing_code.chapter5 import Metric, DataSet

class Expriment():

    def __init__(self, K, N, site=None, rt = "RecentPopular"):
        self.K = K
        self.N = N
        self.site = site
        self.rt = rt
        self.alg = {
            'RecentPopular': RecentPopular,
        }

    # 定义单次实验
    def worker(self, train, test):
        '''
        :param train:
        :param test:
        :return:
        '''
        getRecommendation = self.alg[self.rt](train, self.K, self.N)
        metric = Metric.Metric(train, test, getRecommendation)
        return metric.eval()

    # 运行实验
    def run(self):
        dataset = DataSet.DataSet()
        train, test = dataset.splitData()
        metric = self.worker(train, test)
        print('Result (site = {}, K = {}, N = {}): {}'.format(self.site, self.K, self.N, metric))

if __name__ == "__main__":
    K = 0
    for site in ['www.nytimes.com', 'en.wikipedia.org']:
        for N in range(10, 110, 10):
            exp = Expriment(K, N, site=site, rt="RecentPopular")
            exp.run()