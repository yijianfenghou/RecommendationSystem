from pragram.RecommandSystem.preprocessing_code.chapter2 import timmer
import random

class DataSet():

    def __init__(self, fp, up):
        '''
        :param fp: data file path
        :param up: user profile path
        '''
        self.data, self.profile = self.loadData(fp, up)

    @timmer.timmer
    def loadData(self, fp, up):
        data = []
        for l in open(fp):
            data.append(tuple(l.strip().split('\t')[:2]))
        profile = {}
        for k in open(up):
            user, gender, age, country, _ = k.strip().split('\t')
            if age == '':
                age = -1
            profile[user] = {'gender': gender, 'age': age, 'country': country}

        # 按照用户进行采样
        users = list(profile.keys())
        random.shuffle()
        users = set(users[:5000])
        data = [x for x in data if x[0] in users]
        profile = {k: profile(k) for k in users}
        return data, profile

    @timmer.timmer
    def splitData(self, M, k, seed = 1):
        '''
        :param M: 划分的数目，最后需要取M折的平均
        :param k: 本次是第几次划分，k~[0,M)
        :param seed: random随机数种子，对应不同的k应设置成一样的
        :return:
        '''
        train, test = [], []
        random.seed(1)
        for user, item in self.data:
            # 这里与书中的不一致，本人认为取M-1较为合理，因为randint是左右都被覆盖的
            if random.randint(0, M-1) == k:
                test.append((user, item))
            else:
                train.append((user, item))

        # 处理成字典形式，user -> set(item)
        def convert_dict(data):
            data_dict = {}
            for user, item in data:
                if user not in data_dict:
                    data_dict[user] = set()
                data_dict[user].add(item)

            data_dict = {k: list(data_dict[k]) for k in data_dict}
            return data_dict

        return convert_dict(train), convert_dict(test), self.profile