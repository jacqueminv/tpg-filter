import pyExcelerator
from model.Tournee import Tournee
import fnmatch
import os

class Filter(object):

    def __init__(self, xls_file, data_dir):
        self.xls_file = xls_file
        self.data_dir = data_dir
        self.tournees = []

    def parse(self):
        xls = pyExcelerator.ImportXLS.parse_xls(self.xls_file)

        def get_tab_index(tabname):
            for i in range(len(xls)):
                if xls[i][0] == tabname:
                    return (i+1)

        #xls is a list of dict ('tab-name', 'tab-content')
        for tab in [key for key, value in xls if self.__is_empty(value) is False]:
            content = pyExcelerator.Utils.xls2list(xls, get_tab_index(tab), 'iso-8859-1')
            #: get rid of the 1st row defining the tournee name
            content = content[1:]

            contents = []
            for i in range(len(content)):
                r = content[i]
                if r[0] is None:
                    continue
                contents.append(r)
            t = Tournee.init_with_data(tab, contents)
            self.tournees.extend(t.display_filenames)

    def filter(self):
        ''' Deletes every pdf file under any *totem folder whose name is not listed in the tournee xls'''
        for root, dirnames, filenames in os.walk(self.data_dir):
            for filename in fnmatch.filter(filenames, '*.pdf'):
                os.remove(os.path.join(root, filename))

    def __is_empty(self, tab_content):
        '''Checks if a tab contains any value'''
        return tab_content == {}


if __name__ == '__main__':
    src_file = os.path.join(os.path.dirname(__file__), "../tests/tournee-totems.xls")
    DATA_ROOT = '../tests/'
    filter = Filter(src_file, os.path.abspath(DATA_ROOT))
    filter.parse()
    filter.filter()
