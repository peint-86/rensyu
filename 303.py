n=int(input())
lis=list(map(int,input().split()))
memo={lis[0]}
for i in range(1,n):
    if lis[i] in memo:
        print("Yes")
    else:
        memo.add(lis[i])
        print("No")


n=int(input())
a=set(map(int,input().split()))
b=set(map(int,input().split()))
n=sorted(a|b)
print(*n)


a=int(input())
yotei_a=[]
for _ in range(a):
    yotei_a.append(int(input()))
    
b=int(input())
yotei_b=[]
for q in range(b):
    yotei_b.append(int(input()))


sche={int(i):"x" for i in range(1,32)}
c=0

for j in yotei_a:
    key = j
    sche[key]="A"
for k in yotei_b:
    key = k
    if sche[key]!="A":
        sche[key]="B"
    else:
        c+=1
        if c%2==0:
            sche[key]="B"
for h in sche.values():
    print(h)
