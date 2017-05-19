import argparse
import os
import sys

sys.path.insert(0, os.path.abspath("../"))

from main.config import VERSION
from core.webscrapy import DOU
from core.douparser import DouParser


class DouManager:
    DEFAULT_ARGS = [{'name': '--term', 'dest': 'term', 'help': 'term to search'},
                    {'name': '--start', 'dest': 'start', 'help': 'start date to search'},
                    {'name': '--end', 'dest': 'end', 'help': 'end date to search'},
                    {'name': '--year', 'dest': 'year', 'help': 'year to search'}]
    
    def __init__(self):
        pass

    @classmethod
    def from_args(cls, args):
        if not isinstance(args, argparse.Namespace):
            raise Exception("Incorrect arguments from main")

        cls.run(args)

    @staticmethod
    def run(args):
        dou = DOU()
        res = dou.search(term=args.term, start=args.start, end=args.end, year=args.year)
        print(DouParser(source=res).parser())


class Main:
    def __init__(self):
        pass

    @classmethod
    def parse_args(cls, argv):
        parser = argparse.ArgumentParser(argv)

        for arg in DouManager.DEFAULT_ARGS:
            parser.add_argument(arg['name'], dest=arg['dest'], help=arg['help'])

        parser.add_argument('--version', action='version', version=VERSION)
        return parser.parse_args()


if __name__ == "__main__":
    DouManager.from_args(args=Main().parse_args(sys.argv[1:]))
