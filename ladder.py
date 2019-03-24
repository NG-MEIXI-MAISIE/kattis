import sys
import math
inputstd = sys.stdin.read()
lines = inputstd.split("\n")
line = lines[:-1]
i=0
while i <len(line):
    h,v=map(int,line[i].split())
    l=h/math.sin(math.radians(v))
    print (math.ceil(l))
    i+=1
