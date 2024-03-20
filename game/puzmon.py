'''
作成日:2024/3/7
作成者:hulo
'''
#import
import random
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
def on_enemy_turn(name,i,mon_hp,hp_sum):
      print(f'【{name}のターン】(HP={mon_hp})')
      print(f'コマンド？＞B')
      damage=int(random.uniform(20,80))
      print(f'{damage}のダメージを受けた')
      hp_sum-=damage
      return hp_sum

def on_player_turn(name,i,hp_sum,mon_hp):
    print(f'【{name}のターン】(HP={hp_sum})')
    print(f'コマンド？＞A')
    damage=int(random.uniform(70,150))
    print(f'{damage}のダメージを与えた')
    mon_hp-=damage
    return mon_hp

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
    organaize_party(friends)
    symbol=ELEMENT_SYMBOLS[monlis[i]['element']]
    monster_name=monlis[i]['name']
    color=element_color[monlis[i]['element']]
    hp=monlis[i]['hp']
    print(f'\033[{color}m{symbol}{monster_name}{symbol}\033[0m(HP={hp})が現れた!')
    

def print_monster_disappere(monlis,i,name,hp_sum,c):
    symbol=ELEMENT_SYMBOLS[monlis[i]['element']]
    monster_name=monlis[i]['name']
    color=element_color[monlis[i]['element']]
    if hp_sum <= 0:
        print(f'{name}はダンジョンから逃げ出した') 
        c = None
        return c
    else:
        print(f'\033[{color}m{symbol}{monster_name}{symbol}\033[0mを倒した!')
        print(f'{name}はさらに奥へと進んだ')
        c=int(c)
        c+=1
        return c

def do_battle(monlis,name,friends):
    hp_sum,dp_ave=organaize_party(friends)
    c=0#モンスターの倒した数を格納
    for i in monlis.keys():
        mon_hp=int(monlis[i]['hp'])
        print_monster_appere(monlis,i,name)
        while True:
             if hp_sum <= 0 or mon_hp <= 0:
                 break
             mon_hp=on_player_turn(name,i,hp_sum,mon_hp)
             if hp_sum <= 0 or mon_hp <= 0:
                 break
             hp_sum=on_enemy_turn(monlis[i]['name'],i,mon_hp,hp_sum)
             if hp_sum <= 0 or mon_hp <= 0:
                 break
             
        c=print_monster_disappere(monlis,i,name,hp_sum,c)
        if c == None:
            break

    return c

def go_dungeon(name,friends):
    if name=="":
        print("エラー：プレイヤー名を入力してください")
    else:
        hp_sum,dp_ave=organaize_party(friends)
        print(f'{name}のパーティー（HP={hp_sum})はダンジョンに到着した')
        print("<パーティー編成＞--------------------")
        show_party(friends)
        print("-----------------------------------")
        toubatu=do_battle(monlis,name,friends)
        if toubatu==5:
         print(f'{name}はダンジョンを制覇した')
        return toubatu


def main():
    name=input("プレイヤー名を入力してください＞＞")
    print('***puzle&monsters***')
    toubatu=go_dungeon(name,friends)
    if toubatu==5:
        print(f'倒したモンスターの数＝{toubatu}')
        print('***GAME CLEARED!!***')
    else:
        print('***GAME OVER!!***')




#main関数の呼び出し
main()
