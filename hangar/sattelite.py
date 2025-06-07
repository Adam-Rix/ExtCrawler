# v.0.0.2
## designed to look at extensions of a files and pass it to analyzer

import os
import glob
import logging


EXTENSION = '*.json'
FORMAT = '%(asctime)s %(folder)s \n %(message)s'
logging.basicConfig(format=FORMAT)


class Sattelite:
    def __init__(self, ext = EXTENSION):
        self.ext = ext
        self.directory = os.getcwd()

    def get_files(self):
        files = glob.glob(self.ext, recursive=True)
        return files

    def logger_knocker(self, files):
        logger = logging.getLogger('knocker')
        d = {'folder': self.directory}

        count = len(files)
        match count:
            case 1:
                verb = 'is a'
            case 0:
                verb = 'is no any'
            case _:
                verb = 'are a'

        logger.warning(f'There {verb} {self.ext}: %s',
                       f' Quantity #{count}: {files}',
                       extra=d)

    def knocker(self):
        files = self.get_files()
        self.logger_knocker(files)
        return files, self.directory

if __name__ == "__main__":
    sat = Sattelite()
    files, folder = sat.knocker()