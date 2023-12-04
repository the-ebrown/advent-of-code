# .././get_input.py --day 2 > 2.in
# python3 2.py 2.in
import sys
from collections import defaultdict

#input:
# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green

# possibilities: 
# only 12 red cubes, 13 green cubes, and 14 blue cubes

#foreach line split on : -- game, events
#foreach event split on ; -- event, draws
#foreach draw split on , -- draw, cubes
#foreach cube compare posibile cube_values for cube_value > possibility
#if true, save game number to possible game array
#foreach game in possible_array get the sum

#D = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
D = open(sys.argv[1]).read().strip()
p1 = 0
p2 = 0
#winners = []
for line in D.split('\n'):
    ok = True
    id, line = line.split(':')
    values = defaultdict(int)
    for event in line.split(';'):
        for draws in event.split(','):
            n,color = draws.split()
            n = int(n)
            values[color] = max(values[color], n)
            #possibilities = {'red': 12, 'green': 13, 'blue': 14}.get(color)
            #if(possibilities < int(n)):
            if int(n) > {'red': 12, 'green': 13, 'blue': 14}.get(color):
                ok = False
                #print('not ok')                        
            #print(n)            
            #print(color)
        #print('='*80)
        #print(event)
    #print(values)
    score = 1
    for v in values.values():
        score *= v
    #print ('game: ' + str(id) + ' score: ' + str(score))
    p2 += score
    if ok:
 #       winners.append(id.split()[-1])
        p1 += int(id.split()[-1])

#print(winners)
print('part 1: ' + str(p1))
print('part 2: ' + str(p2))
    #print(id.split()[-1])
