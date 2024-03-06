niti,kau,uru=map(int,input().split())
kane=0
hendou=[]
moti=0
for i in range(niti):
    hendou.append(input())
    if i == niti-1:
        moti=0
    elif int(hendou[i])<=kau:
        kane-=int(hendou[i])
        moti+=1
    elif int(hendou[i]) >= uru and moti>0:
        kane+=(int(hendou[i])*moti)
        moti=0
    
print(kane)
        
