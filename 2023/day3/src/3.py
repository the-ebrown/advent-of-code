# .././get_input.py --day 3 > 3.in
# python3 3.py 3.in
import sys
from collections import defaultdict

# D = """467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598.."""

D = open(sys.argv[1]).read().strip()
p1 = 0
p2 = 0
#winners = []
lines = D.split('\n')

# create a grid
G = [[c for c in line] for line in lines]
# number of rows
R = len(G)
# number of columns
C = len(G[0])

nums = defaultdict(list)
# go through the rows to find the numbers
for r in range(len(G)):
    gears = set()
    n = 0
    has_part = False
    # go through the characters in the column
    for c in range(len(G[r])+1):
        # if character is a digit
        if c<C and G[r][c].isdigit():
            # keep track of the current number
            n = n*10+int(G[r][c])
            # check adjacent squares
            for rr in [-1,0,1]:
                for cc in [-1,0,1]:
                    # a neighbor
                    if 0<=r+rr<R and 0<=c+cc<C:
                        ch = G[r+rr][c+cc]
                        # a neighbor is not a digit
                        if not ch.isdigit() and ch != '.':
                            has_part = True
                        if ch=='*':
                            gears.add((r+rr, c+cc))
        elif n>0:
            for gear in gears:
                nums[gear].append(n)
            if has_part:
                p1 += n
            n = 0
            has_part = False
            gears = set()

print(p1)

for k,v in nums.items():
    if len(v)==2:
        p2 += v[0]*v[1]

print(p2)
