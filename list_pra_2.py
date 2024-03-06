n=int(input())
lis=list(map(int,input().split()))
n_2=int(input())
lis_2=list(map(int,input().split()))
for i in range(n_2):
    print(lis[lis_2[i]-1])

#要素数 N の数列 A と要素数 Q の数列 B が与えられます。 1 ≦ i ≦ Q の各 i について、i 行目に A の B_i 番目の値を出力してください。