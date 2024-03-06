count=int(input())
print("カレーを召し上がれ！")
print(f'カレーを{count}皿食べました')
inp=input("お変わりはいかがですか?(Y?N)>>")
while True:
 if inp=="y":
    count += 1
    print(f'カレーを{count}皿食べました')
    inp=input("お変わりはいかがですか?(Y?N)>>")
 else:
    print("ごちそうさまでした")
    break