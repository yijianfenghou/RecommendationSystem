from pragram.RecommandSystem.preprocessing_code import timmer, evaluation_standard, split_dataset
from pragram.RecommandSystem.chapter2.item import ItemCF, ItemCFNorm, ItemIUF


class ItemExperiment():

    def __init__(self, M, K, N, fp="../dataset/ml-1m/ratings.dat", rt="ItemCF"):
        '''
        :param M: 进行多少次实验
        :param K: TopK相似物品的个数
        :param N: TopN推荐物品的个数
        :param fp: 数据文件路径
        :param rt: 推荐算法类型
        '''
        self.M = M
        self.K = K
        self.N = N
        self.fp = fp
        self.rt = rt
        self.alg = {'ItemCF': ItemCF.ItemCF, "ItemIUF": ItemIUF.ItemIUF, "ItemCFNorm": ItemCFNorm.ItemCFNorm}

    @timmer.timmer
    def worker(self, train, test):
        getRecommendation = self.alg[self.rt](train, self.M, test)
        metric = evaluation_standard.Metric(train, test, getRecommendation)
        return metric.eval()

    @timmer.timmer
    def run(self):
        metrics = {"Precision": 0, "Recall": 0, "Coverage": 0, "Popularity": 0}
        dataset = split_dataset.Dataset(self.fp)
        for ii in range(self.M):
            train, test = dataset.SplitData(self.M, ii)
            print("Experiment {}:".format(ii))
            metric = self.worker(train, test)
            metrics = {k: metrics[k]+metric[k] for k in metrics}
            print('Average Result (M={}, K={}, N={}): {}'.format(self.M, self.K, self.N, metrics))

if __name__ == "__main__":
    M, N = 8, 10
    for K in [5, 10, 20, 40, 80, 160]:
        cf_exp = ItemExperiment(M, K, N, rt="ItemCF")
        cf_exp.run()


