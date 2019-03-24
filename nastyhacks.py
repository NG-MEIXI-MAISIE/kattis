import sys

inputstd = sys.stdin.read()

lines = inputstd.split("\n")
line = lines[1:-1]
i = 0
while i < len(line):
    r,e,c = map(int, line[i].split())
    if (e-c)>r:
        print("advertise")
    elif (e-c)==r:
        print("does not matter")
    else:
        print("do not advertise")
    i+=1
