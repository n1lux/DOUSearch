import argparse
import os
import sys
sys.path.insert(0, os.path.abspath("../"))

from main.config import VERSION
from core.webscrapy import DOU
from core.douparser import DouParser


class Main:
    def __init__(self, argv):
        parser = argparse.ArgumentParser(argv)
        parser.add_argument('--foo', dest='foo', help='foo help')
        parser.add_argument('--version', action='version', version=VERSION)
        args = parser.parse_args()

        if args.foo:
            self.foo(args.foo)

    @staticmethod
    def foo(arg):
        dou = DOU()
        term = "universidade federal dos vales do jequitinhonha e mucuri"
        res = dou.search(term=term, start='01/01', end='12/12', year='2017')
        print(DouParser(source=res).parser())


def main(argv):
    Main(argv)


if __name__ == "__main__":

    main(sys.argv[1:])
