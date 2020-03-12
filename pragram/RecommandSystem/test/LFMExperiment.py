from pragram.RecommandSystem.chapter2.LFM import LFM
from pragram.RecommandSystem.preprocessing_code import timmer, evaluation_standard, split_dataset

class LFMExperiment():

    def __init__(self, M, N, ratio = 1, K = 100, lr = 0.02, step = 100, lmda = 0.01, fp = "../dataset/ml-1m/ratings.dat"):
        self.M = M
        self.N = N
        self.ratio = ratio
        self.K = K
        self.lr =lr
        self.step = step
        self.lmda = lmda
        self.fp =fp
        self.alg = LFM

    @timmer.timmer
    def worker(self, train, test):
        '''
        :param train: 训练数据集
        :param test: 测试数据集
        :return:
        '''
        getRecommendation = self.alg(train, self.ratio, self.K, self.lr, self.step, self.lmda, self.N)
        metric = evaluation_standard.Metric(train, test, getRecommendation)
        return metric.eval()

    @timmer.timmer
    def run(self):
        metrics = {'Precision': 0, 'Recall': 0, 'Coverage': 0,'Popularity': 0}
        dataset = split_dataset.Dataset(self.fp)
        for ii in range(self.M):
            train, test = dataset.SplitData(self.M, ii)
            print('Experiment {}:'.format(ii))
            metric = self.worker(train, test)
            metrics = {k: metrics[k]+metric[k] for k in metrics}
        metrics = {k: metrics[k] / self.M for M in metrics}
        print('Average Result (M={}, N={}, ratio={}): {}'.format(self.M, self.N, self.ratio, metrics))


if __name__ == "__main__":
    M, N = 8, 10
    for r in [1, 2, 3, 5, 10, 20]:
        exp = LFMExperiment(M, N, ratio=r)
        exp.run()