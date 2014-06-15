#!/usr/bin/env python
# coding: utf-8

import random
import sys

def make_uniq_nums():
    return random.randint(1,75)

class BingoBox:
    def __init__(self):
        pass
    def pull(self):
        pass

class BingoCard:
    """
    プレイヤーに配られれるカードを表すクラス
    たぶん意味的規模(?)としては一番小さいくらす
    """
    def __init__(self):
        self.cell = [[ {"num":make_uniq_nums(),"punched":False} for x in range(5)] for y in range(5)]
        self.cell[2][2] = {"num":0, "punched":True} # カードの真ん中の穴はあけておく。

    def punch(self,hit_number):
        for line in self.cell:
            for current_cell in line:
                if current_cell["num"] == hit_number:
                    current_cell["punched"] = True
                    return True

    def show(self):
        for line in self.cell:
            sys.stdout.write("[ ")
            for cell in line:
                sys.stdout.write("{0:2} ".format("--" if cell["punched"] else cell["num"]))
            print("]")
        print("")

    def check_all():

 
class BingoGame:
    def __init__(self,player=3):
        self.was_bingo_player = 0
        self.player_cards = [BingoCard() for n in range(player)]

    def play(self):
        pass

def main():
    game = BingoGame(player=3) 
    for card in game.player_cards:
        card.show()
        game.play()
    #while game.was_bingo_player < 5:
    #    game.play()

    #test_BingoCard_punch() 

"""
test methods
"""
def test_BingoCard_init():
    card = BingoCard()
    card.show()

def test_BingoCard_punch():
    card = BingoCard()
    card.show()
    card.punch(7)
    card.show()

if __name__ == '__main__':
    main()
