import sys
import argparse
parser = argparse.ArgumentParser(description='Add 2 numbers')
parser.add_argument('--x', type=int, required=True, help='First Nmber')
parser.add_argument('--y', type=int, required=True, help='Second Number')
parser.add_argument('--op', type=str, required=True, help='Operation')
arg = parser.parse_args()
if arg.op.lower() == 'add' or 'addition' or 'sum' or '+':
    res = arg.x+arg.y
    print(res)
    sys.exit()
if arg.op.lower() == 'sub' or '-':
    res = arg.x-arg.y
    print(res)
    sys.exit()
if arg.op.lower() == 'mul':
    res = arg.x*arg.y
    print(res)
    sys.exit()
if arg.op.lower() == 'div':
    res = arg.x/arg.y
    print(res)
    sys.exit()
else:
    print("Enter only add/sub/mul/div")
