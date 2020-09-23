import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--gao", help="increase output verbosity")
args = parser.parse_args()
if args.gao:
    print("gao turned on")