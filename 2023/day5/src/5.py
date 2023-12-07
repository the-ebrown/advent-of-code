import sys
import re
from collections import defaultdict

# D="""seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15

# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4

# water-to-light map:
# 88 18 7
# 18 25 70

# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13

# temperature-to-humidity map:
# 0 69 1
# 1 0 69

# humidity-to-location map:
# 60 56 37
# 56 93 4"""

D = open(sys.argv[1]).read().strip()
#p1 = 0
#L = D.split('\n')

parts = D.split('\n\n')
seed, *others = parts
seed = [int(x) for x in seed.split(':')[1].split()]
        
class Function:
    def __init__(self, S):
        lines = S.split('\n')[1:] # throw away name
        # dst src sz
        self.tuples: list(tuple[int, int, int]) = [[int(x) for x in line.split()] for line in lines]
    def apply_one(self, x: int) -> int:
        for(dst, src, sz) in self.tuples:
            if src<=x<src+sz:
                return x+dst-src
        return x

Fs = [Function(s) for s in others]

P1 = []
for x in seed:
    for f in Fs:
        x = f.apply_one(x)
    P1.append(x)
print(min(P1))
