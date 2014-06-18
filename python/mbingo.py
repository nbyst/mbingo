#!/usr/bin/env python
# coding: utf-8

import random
import sys

class BingoNumOverPullException(BaseException):
    pass

class BingoNumGenerator:
    def __init__(self):
        self.used_nums = []
    def pull(self):
        if len(self.used_nums) >= 75:
            raise BingoNumOverPullException

        pulled_num = random.randint(1,75)
        if pulled_num not in self.used_nums:
            self.used_nums.append(pulled_num)
            return pulled_num 
        else:
            return self.pull()

class BingoCard:
    """
    プレイヤーに配られれるカードを表すクラス
    たぶん意味的規模(?)としては一番小さいくらす
    """
    def __init__(self):
        g = BingoNumGenerator()
        self.cell = [[ {"num": g.pull(),"punched":False} for x in range(5)] for y in range(5)]
        self.cell[2][2] = {"num":0, "punched":True} # カードの真ん中の穴はあけておく。

    def punch(self,hit_number):
        for line in self.cell:
            for current_cell in line:
                if current_cell["num"] == hit_number:
                    current_cell["num"] = "--" #本当はpunch前の数字がわかる方がいいかもしれないが...
                    current_cell["punched"] = True
                    return True
        return False

    def show(self):
        for line in self.cell:
            sys.stdout.write("[ ")
            for cell in line:
                sys.stdout.write("{0:2} ".format("--" if cell["punched"] else cell["num"]))
            print("]")
        print("")

    def listen(self,drawn_number):
        #print("listened number is: {0}".format(drawn_number))
        self.punch(drawn_number)

class BingoGame:
    def __init__(self,member_count=3):
        self.was_bingo_player = 0
        self.player_cards = [BingoCard() for n in range(member_count)]
        self.bingobox = BingoNumGenerator()

    def draw(self):
        drawn_number = self.bingobox.pull()
        [player.listen(drawn_number) for player in self.player_cards]

    def current_status(self):
        pass

    def show_drawn_numbers(self):
        print("Drawn Numbers:")
        print(self.bingobox.used_nums)

def main():
    game = BingoGame(member_count=3)
    [card.show() for card in game.player_cards]
    for i in range(1,10):
        game.draw()
    [card.show() for card in game.player_cards]
    game.show_drawn_numbers()


    #while game.was_bingo_player < 5:
    #    game.draw()

    #test_BingoNumGenerator()
    #test_BingoNumGenerator_overpull()
    #test_BingoCard_init() 
    #test_BingoCard_punch() 

"""
test methods
"""

def test_BingoNumGenerator():
    generator = BingoNumGenerator()
    for i in xrange(1,75+1):
        sys.stdout.write("{0} ".format(generator.pull()))

def test_BingoNumGenerator_overpull():
    generator = BingoNumGenerator()
    for i in xrange(1,77):
        sys.stdout.write("{0} ".format(generator.pull()))

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
