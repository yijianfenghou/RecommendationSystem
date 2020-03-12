from pragram.RecommandSystem.preprocessing_code.chapter2 import timmer

class DataSet():

    def __init__(self, fp, up):
        '''
        :param fp: data file path
        :param up: user profile path
        '''
        self.data, self.profile = self.loadData(fp, up)

    @timmer.timmer
    def loadData(self, fp, up):