# .././get_input.py > 1.in
# pypy 1.py 1.in
import sys

# #read in the input file
D = open(sys.argv[1]).read().strip()
p1 = 0
p2 = 0
for line in D.split('\n'):
    p1_digits = []
    p2_digits = []
#read each character and find all the numeric digits
    for i,c in enumerate(line):
        if c.isdigit():
            p1_digits.append(c)
            p2_digits.append(c)
        #compare the string at the current character and if it starts with a spelled out number add it
        for d, val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            if line[i:].startswith(val): #leverage slice here
                p2_digits.append(str(d+1))

#combine the  numbers from the first and last digits and add to the totals
    if p1_digits: p1 += int(p1_digits[0]+p1_digits[-1])
    if p2_digits: p2 += int(p2_digits[0]+p2_digits[-1])

#find the sum
#    total1 += p1
#    total2 += p2
    
print("problem 1: " + str(p1))
print("problem 2: " + str(p2))