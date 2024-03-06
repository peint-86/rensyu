n=int(input())
dic={}
for i in range(10):
    key = i
    dic[key] = 0
lis_2=list(map(int,input().split()))
for j in lis_2:
    dic[j]+=1
new_lis=list(dic.values())
print(*new_lis)
#ディクショナリの{0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}こんな作るやつがi
#値だけを出すのがｊ


[chr(i) for i in range(97, 97+26)]
# [chr(i) for i in range(ord('a'), ord('z')+1)]
n=int(input())
dic={chr(i):0 for i in range(97, 97+26)}
#あるふぁべっと

lis_2=input()
for j in lis_2:
    dic[j]+=1
new_lis=list(dic.values())
print(*new_lis)
#[chr(i) for i in range(97, 97+26)]
# [chr(i) for i in range(ord('a'), ord('z')+1)]
#文字列判別に使える


for word, times in sorted(dic.items()):
    print(word, times)
#文字順にkey,valuesを表示させる
    

a, b = input().split()
#横にkeyと値が入力されていて受け取るとき

for _ in range(a):
    s = input()
    if s in dic:
        print(dic[s])
    else:
        print(-1)
#aの範囲でdicにある時は値を出すないときはー１


N, Q = map(int, input().split())

S = {}
for i in range(N):
    s = input()
    if s not in S:
        S[s] = i + 1#何番目にあったかを入れている　notのおかげで最初の時の位置を入れている
#ないなら追加すっぞの意
        
for _ in range(Q):
    t = input()
    if t in S:
        print(S[t])
    else:
        print(-1)
        

N = int(input())
A = [int(x) for x in input().split()]

memo = {A[0]}
for i in range(1, N):
    if A[i] in memo:
        print("Yes")
    else:
        memo.add(A[i])#setはaddで追加
        print("No")

