#https://paiza.jp/works/challenges/76/retry
xc,yc,r_1,r_2=map(int,input().split())
n=int(input())
for i in range(n):
    x,y=map(int,input().split())
    if r_1**2<=(x-xc)**2+(y-yc)**2<=r_2**2:
        print("yes")
    else:
        print("no")

#https://paiza.jp/challenges/85/show
atari=list(map(int,input().split()))
n=int(input())
c=0
for i in range(n):
    katta=list(set(map(int,input().split())))
    c=0
    for j in katta:
        if j in atari:
            c+=1
    print(c)

#https://paiza.jp/works/mondai/class_primer/class_primer__make_class
class Employee:
    def __init__(self, number, name):
        self.number = number
        self.name = name

    def getnum(self):
        return self.number

    def getname(self):
        return self.name


n = int(input())

roster = []
for _ in range(n):
    values = input().split()

    query = values[0]
    if query == "make":
        number = int(values[1])
        name = values[2]
        roster.append(Employee(number, name))
    elif query == "getnum":
        index = int(values[1]) - 1
        number = roster[index].getnum()
        print(number)
    else:
        index = int(values[1]) - 1
        name = roster[index].getname()
        print(name)

#https://paiza.jp/challenges/48/show
n,r=map(int,input().split())#箱の数n, ボールの半径r 表す整数
t=r*2#tyokkei
for i in range(n):
    h,w,d=map(int,input().split())
    if min(t,h,w,d)==t:
        print(i+1)