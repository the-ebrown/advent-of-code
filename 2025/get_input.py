#!/usr/bin/python3
import argparse
import os
import subprocess
import sys

# Usage:
#   AOC_SESSION=<session_cookie> ./get_input.py --day 1 > 1.in
# Notes:
#   - The session cookie must be set via the AOC_SESSION environment variable.
#   - Find your cookie by inspecting requests to
#     https://adventofcode.com/2025/day/1/input while logged in.

parser = argparse.ArgumentParser(description='Fetch Advent of Code input')
parser.add_argument('--year', type=int, default=2025)
parser.add_argument('--day', type=int, default=1)
args = parser.parse_args()

session_cookie = os.environ.get('AOC_SESSION')
if not session_cookie:
    print('Error: AOC_SESSION environment variable is not set.', file=sys.stderr)
    print('Set it to your Advent of Code session cookie and try again.', file=sys.stderr)
    sys.exit(1)

url = f'https://adventofcode.com/{args.year}/day/{args.day}/input'
user_agent = 'github.com/the-ebrown/AdventOfCode get_input.py'
cmd = (
    f'curl -sSf "{url}" '
    f'--cookie "session={session_cookie}" '
    f'--user-agent "{user_agent}"'
)

result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
if result.returncode != 0:
    # Forward curl's error to stderr for easier debugging
    sys.stderr.write(result.stderr if result.stderr else 'Request failed.\n')
    sys.exit(result.returncode)

print(result.stdout, end='')


