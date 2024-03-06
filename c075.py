kin,n=map(int,input().split())
lis=[]
lis_2=[[0 for _ in range(2)]for _ in range(n)]
point=0
for i in range(n):
    lis.append(int(input()))
    if int(lis[i]) <= point:
        point=point-int(lis[i])
        lis_2[i][1]=point
        lis_2[i][0]=kin
    else:
        kin=kin-int(lis[i])
        point+=lis[i]//10
        lis_2[i][0]=kin
        lis_2[i][1]=point
    print(*lis_2[i])
    
