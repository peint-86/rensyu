'''
作成日:2024/3/7
作成者:hulo
'''
#import

#global変数の宣言

#味方モンスターの定義
seiryu={'name':'青龍','hp':'150','max_hp':'150','element':'風','ap':15,'dp':10}
suzaku ={'name':'朱雀','hp':'150','max_hp':'150','element':'火','ap':25,'dp':10}
byakko={'name':'白虎','hp':'150','max_hp':'150','element':'土','ap':20,'dp':5}
genbu={'name':'玄武','hp':'150','max_hp':'150','element':'水','ap':20,'dp':15}
friends={0:seiryu,1:suzaku,2:byakko,3:genbu}
hp_sum=0
dp_ave=0

#モンスターの定義
slime={'name':'スライム','hp':'100','max_hp':'100','element':'水','ap':10,'dp':1}
gobrin={'name':'ゴブリン','hp':'200','max_hp':'200','element':'土','ap':20,'dp':5}
ookoumori={'name':'オオコウモリ','hp':'300','max_hp':'300','element':'風','ap':30,'dp':10}
weauluf={'name':'ウェアウルフ','hp':'400','max_hp':'400','element':'風','ap':40,'dp':15}
doragon={'name':'ドラゴン','hp':'500','max_hp':'500','element':'火','ap':50,'dp':20}
monlis={0:slime,1:gobrin,2:ookoumori,3:weauluf,4:doragon,}


#エレメントの定義
ELEMENT_SYMBOLS={"火":'$',"水":'~',"風":'@',"土":'#',"命":'&',"無":' ',}

#エレメントカラーの定義
element_color={"火":int(31),"水":int(36),"風":int(32),"土":int(33),"命":int(35),"無":int(37)}
#関数宣言
def organaize_party(friends):
    hp_sum=0
    dp_ave=0
    for j in range(len(friends)):
        hp_sum+=int(friends[j]['hp'])
        dp_ave+=int(friends[j]['dp'])
        dp_ave/len(friends)
    return hp_sum,dp_ave
        

def show_party(friends):
    for k in range(len(friends)):
        symbol_mikata=ELEMENT_SYMBOLS[friends[k]['element']]
        friends_name=friends[k]['name']
        color=element_color[friends[k]['element']]
        hp=friends[k]['hp']
        kougeki=friends[k]['ap']
        defence=friends[k]['dp']
        print(f'\033[{color}m{symbol_mikata}{friends_name}{symbol_mikata}\033[0m HP={hp} 攻撃={kougeki} 防御={defence}')


def print_monster_appere(monlis,i,name):
    hp_sum,dp_ave=organaize_party(friends)
    symbol=ELEMENT_SYMBOLS[monlis[i]['element']]
    monster_name=monlis[i]['name']
    color=element_color[monlis[i]['element']]
    print(f'\033[{color}m{symbol}{monster_name}{symbol}\033[0mが現れた!')
    hp_sum=hp_sum
    hp_sum=10
    return hp_sum

def print_monster_disappere(monlis,i,hp_sum,name):
    symbol=ELEMENT_SYMBOLS[monlis[i]['element']]
    monster_name=monlis[i]['name']
    color=element_color[monlis[i]['element']]
    print(f'\033[{color}m{symbol}{monster_name}{symbol}\033[0mを倒した!')
    hp_sum=hp_sum
    hp_sum = hp_sum
    if hp_sum <= 0:
        print(f'{name}はダンジョンから逃げ出した')
    else:
        print(f'{name}はさらに奥へと進んだ')


def do_battle(monlis,name):
    hp_sum,dp_ave=organaize_party(friends)
    c=0#モンスターの倒した数を格納
    for i in monlis.keys():
        print_monster_appere(monlis,i,hp_sum,name)
        hp_sum=print_monster_appere
        print_monster_disappere(monlis,i,hp_sum,name)
        c+=1
    return c

def go_dungeon(name):
    if name=="":
        print("エラー：プレイヤー名を入力してください")
    else:
        hp_sum,dp_ave=organaize_party(friends)
        print(f'{name}のパーティー（HP={hp_sum})はダンジョンに到着した')
        print("<パーティー編成＞--------------------")
        show_party(friends)
        print("-----------------------------------")
        toubatu=do_battle(monlis,name)
        print(f'{name}はダンジョンを制覇した')
        return toubatu


def main():
    name=input("プレイヤー名を入力してください＞＞")
    print('***puzle&monsters***')
    toubatu=go_dungeon(name)
    print('***GAME CLEARED!!***')
    if toubatu==5:
        print(f'倒したモンスターの数＝{toubatu}')
    else:
        print('***GAME OVER!!***')



#main関数の呼び出し
main()
