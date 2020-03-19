from .timmer import timmer

class Metric():

    def __init__(self, fp):
        self.data = self.load(fp)

    @timmer
    def loadData(self, fp):
        data = [f.strip().split('\t')[:3] for f in open(fp).readlines()[1:]]
        return data

    @timmer
    def splitData(self, M, k, seed=1):
        '''
        :param data: 加载的所有(user, item)数据条目
        :param M:  划分的数目，最后需要取M折的平均
        :param k: 本次是第几次划分，k~[0, M]
        :param seed: 随机种子
        :return:
        '''
        # 按照(user, item)作为key进行划分
        train, test = [], []
        import random
        random.seed(seed)
        for user, item, tag in self.data:
            # 这里与书上的不一致，本人觉得取M-1较为合理，因randint是左右都覆盖的
            if random.randint(0, M-1) == k:
                test.append((user, item, tag))
            else:
                train.append((user, item, tag))

        # 处理成字典的形式，user -> set(items)
        def convert_dict(data):
            data_dict = {}
            for user, item, tag in data:
                if user not in data_dict:
                    data_dict[user] = {}
                if item not in data_dict[user]:
                    data_dict[user][item] = set()
                data_dict[user][item].add(tag)

            for user in data_dict:
                for item in data_dict[user]:
                    data_dict[user][item] = list(data_dict[user][item])
            return data_dict

        return convert_dict(train), convert_dict(test)
