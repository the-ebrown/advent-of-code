import sys
print("Let's read the arguments from the command line")
D = open(sys.argv[1]).read().strip()
print(D)