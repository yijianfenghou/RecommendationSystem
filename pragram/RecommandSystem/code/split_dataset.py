import random
from .timmer import timmer

class Dataset():

    def __init__(self, fp):
        #fp:data file path
        self.data = self.loadData(fp)

    @timmer
    def loadData(self, fp):
        data = []
        for l in open(fp):
            data.append(list(map(int, l.strip().split('::')[:2])))
        return data

    @timmer
    def SplitData(self, M, k, seed = 1):
        test = []
        train = []
        random.seed(seed)
        for user, item in self.data:
            if random.randint(0, M-1) == k:
                test.append([user, item])
            else:
                train.append([user, item])

        #处理成字典形式，user->set(items)
        def convert_dict(data):
            data_dict = {}
            for user, item in data:
                if user not in data_dict:
                    data_dict[user] = set()
                data_dict.add(item)
            data_dict = {k: list(data_dict[k]) for k in data_dict}
            return data_dict

        return convert_dict(train), convert_dict(test)



