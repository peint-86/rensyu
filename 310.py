#二次元配列の標準入力受け取り方
A = [[int(x) for x in input().split()] for i in range()]

# 入力されたHとWに基づいてパネルの状態と得点を受け取る
H, W = map(int, input().split())
panels = [input() for _ in range(H)]
scores = [list(map(int, input().split())) for _ in range(H)]
# 合計得点を計算するための変数を初期化
total_score = 0
# H×Wのパネルを走査して、撃ち抜かれたパネルの得点を合計する
for i in range(H):
    for j in range(W):
        if panels[i][j] == 'o':  # 撃ち抜かれたパネルを確認
            total_score += scores[i][j]  # 撃ち抜かれたパネルの得点を加算
# 最終得点を出力
print(total_score)

y,x=map(int,input().split())
marubatu= [[i for i in input()] for i in range(y)]
stolak=[[int(i) for i in input().split()] for i in range(y)]
c=0
for i in range(y):
    for j in range(x):
        if marubatu[i][j]=="o":
            c+=stolak[i][j]
            
print(c)
#c089

#splitの使い方
test_str = "A B C D E"
result = test_str.split(None, 3)
print(result)
['A', 'B', 'C', 'D E']


#https://paiza.jp/works/mondai/class_primer/class_primer__constructor

N = int(input())
name = [input() for _ in range(N)]

# ユーザーIDの数字部分を取得し、その数字でソートするための関数
def sort_key(name):
    num_part = ''.join(filter(str.isdigit,name))
    return int(num_part)

sorted_user_ids = sorted(name, key=sort_key)

for name in sorted_user_ids:
    print(name)
