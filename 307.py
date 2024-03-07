a,b=input().split()
oya={1:int(a),2:int(b)}
n=int(input())
for i in range(n):
    c,d=input().split()
    c=int(c)
    d=int(d)
    if oya[1]>c:
        print("High")
    elif oya[1]==c:
        if oya[2]<d:
            print("High")
        else:
            print("Low")
    elif oya[1]<c:
        print("Low")
# 入力された地図のサイズと標高データを受け取る
H, W = map(int, input().split())
map_data = [list(map(int, input().split())) for _ in range(H)]

# 山頂の標高を格納するリスト
mountain_tops = []

# 地図の各マスを調べる
  for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            ni, nj = i + di, j + dj
            # 地図の範囲内かつ現在のマスより標高が高い場合
            if 0 <= ni < H and 0 <= nj < W and map_data[ni][nj] > current_height:
                is_mountain_top = False
                break
        # 周りのマスより標高が高い場合、山頂としてリストに追加
        if is_mountain_top:
            mountain_tops.append(current_height)

# 山頂の標高を高い順にソートして出力
for height in sorted(mountain_tops, reverse=True):
    print(height)for i in range(H):
    for j in range(W):
        # 現在のマスの標高
        current_height = map_data[i][j]
        # 周囲のマスと比較するためのフラグ
        is_mountain_top = True
        # 周囲のマスを調べる（上下左右、さらに四隅も考慮）
      
#C017
class Student:
    def __init__(self, name, old, birth, state):
        self.name = name
        self.old = old
        self.birth = birth
        self.state = state

    def change_name(self, name):
        self.name = name


n, k = [int(x) for x in input().split()]

roster = [None] * n
for i in range(n):
    name, old, birth, state = input().split()
    roster[i] = Student(name, old, birth, state)

for i in range(k):
    index, new_name = input().split()
    roster[int(index) - 1].change_name(new_name)

for student in roster:
    print(student.name, student.old, student.birth, student.state)