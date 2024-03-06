m,p,q=map(int,input().split())
p=p/100
q=q/100
print(m*(1-p)*(1-q))

m, p, q = map(int, input().split())
p = p / 100
q = q / 100
nokori = m * (1 - p)  # 最初に売れ残った量
nokori *= (1 - q)  # お惣菜として売れた後の売れ残り
print(nokori)

nin,base=map(int,input().split())
dic={}
for i in range(nin):
    key=i+1
    a,b=map(int,input().split())
    seiseki=a-(b*5)
    dic[key]=seiseki
    if seiseki>= base:
        print(key)
    elif base==0:
        print(key)

        s = 'abc-xyz-123-789-ABC-XYZ'

print(s.replace('xyz', ''))
# abc--123-789-ABC-XYZ

print(s.translate(str.maketrans({'o': 'O', 't': 'T'})))
# One TwO One TwO One

print(s.translate(str.maketrans({'o': 'XXX', 't': None})))
# XXXne wXXX XXXne wXXX XXXne

# 標準入力から文字列を受け取る
s = input()

# 母音のリストを定義
boin = "aeiouAEIOU"

# 母音を取り除く
result = ''.join([char for char in s if char not in boin])

# 結果を出力
print(result)


my_list = ['Python', 'は', '素晴らしい']
result = ' '.join(my_list)
print(result)  # 出力: Python は 素晴らしい
fruits = ['りんご', 'バナナ', 'オレンジ']
result = ', '.join(fruits)
print(result)  # 出力: りんご, バナナ, オレンジ
s = '12345'
result = '-'.join(s)
print(result)  # 出力: 1-2-3-4-5

s=input()
c=0
s=''.join([char for char in s if char not in "-"])
dic={"0":12,"1":3,"2":4,"3":5,"4":6,"5":7,"6":8,"7":9,"8":10,"9":11}
s=str(s)
for i in s:
    v=dic[i]*2
    c+=v
print(c)
