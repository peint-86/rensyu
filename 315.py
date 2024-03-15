#super().親クラスのメソッド # python3系での標準の書き方

# 関数を使わずに解く
N, M = map(int, input().split())
min_remainder = N
max_containers = 0
best_machine = 0
machines = [int(input()) for _ in range(M)]
for i, m in enumerate(machines):
    remainder = N % m
    if remainder < min_remainder or (remainder == min_remainder and m > max_containers):
        min_remainder = remainder
        max_containers = m
        best_machine = i + 1

# 出力
print(best_machine)


