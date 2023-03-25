
from enum import Enum


class MapItem(str, Enum):
    # マップアイテム一覧
    def __new__(cls, value, mapItem, title, description):
        obj = str.__new__(cls, value)
        obj._value_ = value
        obj.mapItem = mapItem
        obj.title = title
        obj.description = description
        return obj
    BLOCK = 'B', '＃', '壁', '侵入不可エリア(壁)'
    EMPTY = 'E', '　', '空地', '何もないフィールド'
    PLAYER = 'P', 'P', 'プレイヤー', 'プレイヤーの位置'
    GOAL = 'G ','G', 'ゴール', 'ゴールの位置'
    WEAPON = 'W', '剣', '勇者の剣', '武器/勇者の剣/持っているだけで攻撃力アップ'
    SIELD = 'S', '盾', '勇者の盾', '防具/勇者の盾/持っているだけで防御力アップ'
    HERBS = 'H', '薬', '薬草', '道具/薬草/使うとHPがすこし回復する'
        
class Map:
    # class variable
    mapLists = [
        "BBBBBB",
        "BEEEEB",
        "BEEEEB",
        "BWEEEB",
        "BBBBBB",
    ]

    def __init__(self):
        self.now_h = 1
        self.now_w = 1
        self.counter = 0
        self.goal_flg = False
        self.goal_over_flg = False
        self.show_item_flg = False
        self.field = ""

    def show(self):
        for mapLine in self.mapLists:
            Map = ''
            for map_element in mapLine:
                #Map += map_element
                Map += MapItem(map_element).mapItem
            print(Map)

if __name__ == '__main__':
    weapon = 'W'
    print(MapItem(weapon).title)
