import random
from sys import stderr
from time import sleep

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-n', type=int, help='Number of expected messages')
args = parser.parse_args()

i = 0

while True:
    sleep(1)
    if random.random() > 0.5:
        print("Just message")
    else:
        # into error stream prings
        # impromptu error message
        print("Some error", file=stderr)

    i += 1
    if not args.n is None:
        if i >= args.n: break
        
    