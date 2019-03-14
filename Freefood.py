days=[]
for _ in range(int(input())):
    a,b=[int(x) for x in input().split()]
    days_in=range(a,b+1)
    days.extend(days_in)
days=dict.fromkeys(days)
print(len([*days]))
