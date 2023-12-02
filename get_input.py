#!/usr/bin/python3
import argparse
import subprocess
import sys
#import requests

# Usage: ./get_input.py > 1.in
# You must fill in SESSION following the instructions below.
# DO NOT run this in a loop, just once.

# You can find SESSION by using Chrome tools:
# 1) Go to https://adventofcode.com/2022/day/1/input
# 2) right-click -> inspect -> click "Network".
# 3) Refresh
# 4) Click click
# 5) Click cookies
# 6) Grab the value for session. Fill it in.
#github login 
# SESSION = '53616c7465645f5fded52ba2c4bf12638edf33ecda7614d536c872308941cd0a0761d7dbc7284c7a708025c40e3fd73b2deca25abb662dce8600449794d381e0'

#google login
SESSION = '53616c7465645f5f0a46feb3b43909e35e47644548f5db0cfad3534d748b7b250e6a679982c639c64d97a76d31b583ba55a3da4e0b0f182dba881f8bb64829de'

#useragent = 'https://github.com/the-ebrown/AdventOfCode/blob/main/get_input.py by evan.m.brown@gmail.com'
parser = argparse.ArgumentParser(description='Read input')
parser.add_argument('--year', type=int, default=2023)
parser.add_argument('--day', type=int, default=1)
args = parser.parse_args()

cmd = f'curl https://adventofcode.com/{args.year}/day/{args.day}/input --cookie "session={SESSION}"'
output = subprocess.check_output(cmd, shell=True)
output = output.decode('utf-8')
print(output, end='')
print('\n'.join(output.split('\n')[:10]), file=sys.stderr)
