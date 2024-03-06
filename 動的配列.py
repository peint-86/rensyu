n,l=map(int,input().split())
lis=list(map(int,input().split()))
for i in range(l):
    f=list(map(int,input().split()))
    if f[0]==0:
        lis.append(f[1])
    elif f[0]==2:
        print(*lis)
    elif f[0]==1:
        del lis[-1]
        
    