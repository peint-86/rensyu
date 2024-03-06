n=int(input())
lis=[]
for i in range(n):
    s=int(input())
    lis.append(s)
new_lis=[]
new_lis=lis

for i in lis:
    v=i
    s.sort(reverse=True)
    for j in range(n):
        if i==new_lis[j]:
            print(new_lis.index(i)+1)
            break
            # まず、リストを降順にソートします。
            sorted_lis = sorted(new_lis, reverse=True)
            # 各要素のランクを格納するための辞書を作成します。
            rank_dict = {}
            rank = 1
            # ソートされたリストをループし、各要素のランクを辞書に格納します。
            # 同じ値の要素は同じランクを持つため、辞書に既に存在する値はスキップします。
            for index, value in enumerate(sorted_lis):
                if value not in rank_dict:
                    rank_dict[value] = rank
                rank += 1
            # 元のリストの各要素のランクを、辞書を使用して出力します。
        
