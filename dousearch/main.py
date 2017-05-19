import argparse, sys


class Main:
    def __init__(self, argv):
        parser = argparse.ArgumentParser(argv)
        parser.add_argument('--foo', dest='foo', help='foo help')
        parser.add_argument('--version', action='version', version='%(prog)s 1.0')
        args = parser.parse_args()

        if args.foo:
            self.foo(args.foo)

    @staticmethod
    def foo(arg):
        print(arg)


def main(argv):
    Main(argv)


if __name__ == "__main__":
    main(sys.argv[1:])
