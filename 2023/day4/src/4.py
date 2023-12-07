# .././get_input.py --day 4 > 4.in
# python3 4.py ../data/4.in
import sys
import re
from collections import defaultdict

#input:
# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# winning numbers on left of '|' my numbers on right
# matched winning numbers double the prize points 4 matches = 8 points
# add all the prize points together

#D = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
D = open(sys.argv[1]).read().strip()
p1 = 0
p2 = 0
lines = D.split('\n')
N = defaultdict(int)
for i, line in enumerate(lines):
    N[i] += 1
    first, rest = line.split('|')
    id, card = first.split(':')
    card_nums = [int(n) for n in card.split()]
    rest_nums = [int(n) for n in rest.split()]
    val = len(set(card_nums) & set(rest_nums))
    if(val > 0):
        p1 += 2**(val-1)
    for j in range(val):
        N[i+1+j] += N[i]

#print(N)
p2 = sum(N.values())

print(p1)
print(p2)
