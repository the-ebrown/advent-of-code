import sys

# Read input
D = open(sys.argv[1]).read().strip()

# Part 1: Count times we END at position 0
position = 50
count_part1 = 0

for line in D.split('\n'):
    direction = line[0]
    distance = int(line[1:])
    
    if direction == 'L':
        position = (position - distance) % 100
    else:  # 'R'
        position = (position + distance) % 100
    
    if position == 0:
        count_part1 += 1

print(f"Part 1: {count_part1}")

# Part 2: Count ALL times we pass through or end at position 0
position = 50
count_part2 = 0

for line in D.split('\n'):
    direction = line[0]
    distance = int(line[1:])
    
    if direction == 'R':
        # Moving right: count how many times we cross 0
        # We cross 0 at positions 100, 200, 300, etc. from our starting position
        crosses = (position + distance) // 100
        count_part2 += crosses
        position = (position + distance) % 100
        
    else:  # 'L'
        # Moving left: count how many times we cross 0
        # We hit 0 first after 'position' steps, then every 100 steps after
        if position > 0 and distance >= position:
            # We hit 0 at least once, then potentially more times
            crosses = 1 + (distance - position) // 100
        elif position == 0:
            # Starting at 0, we hit it every 100 steps going left
            crosses = distance // 100
        else:
            crosses = 0
        
        count_part2 += crosses
        position = (position - distance) % 100

print(f"Part 2: {count_part2}")