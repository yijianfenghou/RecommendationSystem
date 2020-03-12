# import sys
# sys.path.append("..")
from pragram.RecommandSystem.preprocessing_code import timmer, evaluation_standard, split_dataset
from pragram.RecommandSystem.chapter2 import MostPopular, Random, UserCF, UserIIF

class UserExperiment():

    def __init__(self, M, K, N, fp="../dataset/ml-1m/ratings.dat", rt="UserCF"):
        '''
        :param M: 进行测试的次数
        :param K: TopK相似用户的个数
        :param N: TopN推荐物品的个数
        :param fp: 数据文件路径
        :param rt: 推荐算法类型
        '''
        self.M = M
        self.K = K
        self.N = N
        self.fp = fp
        self.rt = rt
        self.alg = {"Random": Random.Random, "MostPopular": MostPopular.MostPopular, "UserCF": UserCF.UserCF, "UserIIF": UserIIF.UserIIF}

    #定义单次试验
    @timmer.timmer
    def worker(self, train, test):
        '''
        :param train: 训练数据集
        :param test: 测试数据集
        :return: 各指标的值
        '''
        funcname = self.alg[self.rt]
        getRecommendation = funcname(train, self.K, self.N)
        metric = evaluation_standard.Metric(train, test, getRecommendation)
        return metric.eval()

    #定义多次实验
    @timmer.timmer
    def run(self):
        metrics = {'Precision': 0, 'Recall': 0, 'Coverage': 0, "Popularity": 0}
        dataset = split_dataset.Dataset(self.fp)
        for ii in range(self.M):
            train, test = dataset.SplitData(self.M, ii)
            print('Experiment {}:'.format(ii))
            metric = self.worker(train, test)
            metrics = {k: metrics[k] / self.M for k in metrics}
        metrics = {k: metrics[k] / self.M for k in metrics}
        print('Average Result (M={}, K={}, N={}): {}'.format(self.M, self.K, self.N, metrics))

if __name__ == "__main__":
    M, N = 8, 10
    K = 0
    mp_exp = UserExperiment(M, K, N, rt='MostPopular')
    mp_exp.run()

