import argparse, sys


def main(argv):
    parser = argparse.ArgumentParser(argv)
    parser.add_argument('--foo', help='foo help')
    args = parser.parse_args()

    if args.foo:
        print(args.foo)

if __name__ == "__main__":
    main(sys.argv[1:])