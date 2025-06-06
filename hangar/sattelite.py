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

    def knocker(self):

            files = glob.glob(self.ext, recursive=True)

            logger = logging.getLogger('knocker')
            d = {'folder': self.directory}

            count = 0
            files_arr = []
            for file in files:

                if any(file):
                    count += 1
                    files_arr.append(file)

            match count:
                case 1:
                    verb = 'is a'
                case 0:
                    verb = 'is no any'
                case _:
                    verb = 'are a'

            logger.warning(f'There {verb} {self.ext}: %s',
                           f' Quantity #{count}: {files_arr}',
                           extra=d)

            return files_arr

if __name__ == "__main__":
    Sattelite().knocker()