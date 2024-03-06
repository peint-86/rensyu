n=int(input())
key=input()
mozi=[]

for i in range(n):
    mozi.append(input())
    mozi_2=[s for s in mozi if "ai" in s]
if len(mozi_2)>=1:
    print(*mozi_2, sep="\n")
else:
    print("None")
    
mozi_2 = [s for s in mozi if key in s]
if mozi_2:
    print(*mozi_2, sep="\n")
else:
    print("None")
