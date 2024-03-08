'''
作成日：2024/3/7
作成日：hulo
'''
#import

#global変数の宣言

#モンスターの定義
slime={'name':'スライム','hp':'100','max_hp':'100','element':'水','ap':10,'dp':1}
gobrin={'name':'ゴブリン','hp':'200','max_hp':'200','element':'土','ap':20,'dp':5}
ookoumori={'name':'オオコウモリ','hp':'300','max_hp':'300','element':'風','ap':30,'dp':10}
weauluf={'name':'ウェアウルフ','hp':'400','max_hp':'400','element':'風','ap':40,'dp':15}
doragon={'name':'ドラゴン','hp':'500','max_hp':'500','element':'火','ap':50,'dp':20}

#エレメントの定義
ELEMENT_SYMBOLS={"火":'$',"水":'~',"風":'@',"土":'#',"命":'&',"無":' ',}

#エレメントカラーの定義
element_color={"火":int(31),"水":int(36),"風":int(32),"土":int(33),"命":int(35),"無":int(37)}
#関数宣言
def print_monster_name(monlis,i):
    symbol=ELEMENT_SYMBOLS[monlis[i]['element']]
    monster_name=monlis[i]['name']
    color=element_color[monlis[i]['element']]
    print(f'\033[{color}m{symbol}{monster_name}{symbol}\033[0m')


def do_battle():
    c=0#モンスターの倒した数を格納
    monlis={0:slime,1:gobrin,2:ookoumori,3:weauluf,4:doragon,}
    for i in monlis.keys():
        print_monster_name(monlis,i)
        c+=1
    return c

def go_dungeon(name):
    if name=="":
        print("エラー：プレイヤー名を入力してください")
    else:
        print(f'{name}はダンジョンに到着した')
        toubatu=do_battle()
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
