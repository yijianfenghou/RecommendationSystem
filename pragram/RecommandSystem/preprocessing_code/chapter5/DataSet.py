import random
import codecs

class DataSet():
    # 对每个用户按照时间进行从前到后的排序，取最后一个时间的item作为预测的测试集
    def __init__(self, site):
        '''
        :param site:  which site to load
        '''
        self.bookmark_path = ""
        self.user_bookmark_path = ""
        self.site = site
        self.loadData()

    def loadData(self):
        bookmarks = [f.strip() for f in codecs.open(self.bookmark_path, 'r', encoding='ISO-8859-1').readlines()][1:]
        site_ids = {}
        for b in bookmarks:
            b = b.split('\t')
            if b[-1] not in site_ids:
                site_ids[b[-1]] = set()
            site_ids[b[-1]].add(b[0])
        user_bookmarks = [f.strip() for f in codecs.open(self.user_bookmark_path, 'r', encoding='ISO-8859-1').readlines()]