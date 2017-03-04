# -*- coding: utf-8 -*-
from random import choice,randint,shuffle
from os import system

class Cards:

    trump = ''

    def shuffle_deck(self):
        self.deck =['C6','C7','C8','C9','CT','CJ','CQ','CK','CA',
                    'D6','D7','D8','D9','DT','DJ','DQ','DK','DA',
                    'H6','H7','H8','H9','HT','HJ','HQ','HK','HA',
                    'S6','S7','S8','S9','ST','SJ','SQ','SK','SA'
                    ]
        for i in range(10):
            shuffle(self.deck)
        return self.deck

    def give_cards(self):
        self.cards_player = []
        self.cards_robot = []
        for i in range(6):
            self.cards_robot.append(self.deck[-1])
            self.deck.pop()
            self.cards_player.append(self.deck[-1])
            self.deck.pop()
        return self.cards_player,self.cards_robot

    def give_cards_pla(self,cards_player,deck):
        if len(self.cards_player) < 6:
            self.cards_player.append(self.deck[-1])
            self.deck.pop()
        return self.cards_player,self.deck

    def give_cards_rob(self,cards_robot,deck):
        if len(self.cards_robot) < 6:
            self.cards_robot.append(self.deck[-1])
            self.deck.pop()
        return self.cards_robot,self.deck

    def make_trump(self):
        self.trump = self.deck[randint(0,len(self.deck)-1)]
        self.deck.remove(self.trump)
        self.deck.insert(0,self.trump)
        return self.trump

class Player:
    deck_weight = [ 'C6','C7','C8','C9','CT','CJ','CQ','CK','CA',
                    'D6','D7','D8','D9','DT','DJ','DQ','DK','DA',
                    'H6','H7','H8','H9','HT','HJ','HQ','HK','HA',
                    'S6','S7','S8','S9','ST','SJ','SQ','SK','SA'
                    ]
    draw_suit = {'C': '\u2667','D': '\u2666','H': '\u2665','S': '\u2664'}
    card_ranks = [ '6','7','8','9','T','J','Q','K','A' ]

    def __init__(self,deck,cards_player,trump):
        self.deck = deck
        self.cards_player = cards_player
        self.trump = trump

    def see_cards(self,deck,cards_player,trump):
        system('clear')
        print("{0} The Card Game: Sipmle Duren' {0}".format('='*30) )
        print(  '\t\tКарта вводиться 2-ма латинськими літерами, '
                'наприклад: ha (Черва Туз)\n\n\t'
                '{0} => C (clubs|трефа),{1} => D (diamonds|бубна),'
                '{2} => H (hearts|черва),{3} => S (spades|піка)'
                .format(self.draw_suit['C'],self.draw_suit['D'],\
                self.draw_suit['H'],self.draw_suit['S']))
        print(  '\n\tT => Ten|Десятка, J => Jack|Валет, Q => Queen|Королева, '
                'K => King|Король, A => Ace|Туз\n')
        print("\t\tКоли немає чим бити, забрати карту => take\n")
        print('\n' + '='*90)
        print("Твої карти:", end=' ')
        for card in self.cards_player:
            print("{0} {1} ".format(self.draw_suit[card[0]],card[1]), end='')
        if len(self.deck) > 0:
            print("\nКарти на столі: %s " % len(self.deck[1:]), end='')
            print("+ {0} {1} Козир".format(self.draw_suit[self.trump[0]],self.trump[1]))
        else:
            print("\nкозир:{0}".format(self.draw_suit[self.trump[0]]))
        print("{0} Карти в грі {0}".format('='*10) )
        return 0

    def see_trump(self,cards_player,trump):
        self.trump_pla = ''
        while self.trump_pla == '':
            self.trump_pla = input("Покажи молодший козир, "
                                "якщо немає, введи 'no':").upper()
            if self.trump_pla == 'NO': break
            if self.trump_pla not in self.cards_player:
                self.trump_pla = input("Тільки козир або 'no'?:").upper()
            if self.trump_pla in self.cards_player \
                and self.trump_pla[0] == self.trump[0]: break
            else:
                if self.trump_pla == 'NO': break
                self.trump_pla = input("Це не твій козир!Востаннє - "
                                     "козир або 'no'?:").upper()
                if self.trump_pla in self.cards_player \
                    and self.trump_pla[0] == self.trump[0]:
                    break
                else:
                    self.trump_pla = 'NO'
        return self.trump_pla

    def attack(self,cards_player,trump):
        cardgame = []
        card = input("Твій хід>").upper()
        while card not in self.cards_player:
            card = input("В тебе немає цеї карти, введи карту:").upper()
        cardgame.append(card)
        self.cards_player.remove(card)
        print("{0} {1}".format(self.draw_suit[cardgame[0][0]],cardgame[0][1]))
        return cardgame,self.cards_player

    def defence(self,cardgame,cards_player,trump):
        self.result = ''
        card = input("Бити>").upper()
        while card not in self.cards_player:
            if card.lower() == 'take':
                self.result = 'take'
                break
            if card in self.cards_player:
                break
            else:
                card = input("В тебе немає цеї карти, карту або 'take':").upper()
        if self.result != 'take':
            cardgame.append(card)
            if self.card_ranks.index(cardgame[1][1]) > \
                self.card_ranks.index(cardgame[0][1]) \
                and cardgame[1][0] == cardgame[0][0]:
                self.result = 'beat'
            elif cardgame[1][0] == self.trump[0] \
                and cardgame[0][0] != self.trump[0]:
                self.result = 'beat_trump'
            else:
                self.cards_player.remove(card)
                self.result = 'take'
        if self.result == 'beat':
            self.cards_player.remove(card)
            print("{0} {1} Бито!" \
            .format(self.draw_suit[cardgame[1][0]],cardgame[1][1]))
        elif self.result == 'beat_trump':
            self.cards_player.remove(card)
            print("{0} {1} Козир!!!" \
            .format(self.draw_suit[cardgame[1][0]],cardgame[1][1]))
        else:
            self.cards_player.extend(cardgame)
            print("Щоб я скис! Ти забрав...")
        return self.result,self.cards_player

class Robot(Player):

    def __init__(self,deck,cards_robot,trump):
        self.deck = deck
        self.cards_robot = cards_robot
        self.trump = trump

    def eval_rob_ranks(self,cards_robot):
        cardsrobranks = {'6':0,'7':0,'8':0,'9':0,'T':0,'J':0,'Q':0,'K':0,'A':0}
        for card in self.cards_robot:
            cardsrobranks[card[1]] += 1
        return cardsrobranks

    def see_trump(self,cards_robot,trump):
        self.trump_rob = 'NO'
        for card in self.cards_robot:
            if card[0] == self.trump[0]:
                if self.trump_rob != 'NO':
                    if self.deck_weight.index(card) \
                        < self.deck_weight.index(self.trump_rob):
                        self.trump_rob = card
                    else:
                        continue
                else:
                    self.trump_rob = card
        return self.trump_rob

    def attack(self,cards_robot,trump):
        cardsrobranks = self.eval_rob_ranks(self.cards_robot)
        cardgame = []
        robot_att = []
        robot_att_trump = []
        for rank in self.card_ranks:
            if cardsrobranks[rank] > 0:
                for card in self.cards_robot:
                    if card[1] == rank and card[0] != self.trump[0]:
                        robot_att.append(card)
                    else:
                        robot_att_trump.append(card)
        if len(robot_att) != 0:
            cardgame.append(robot_att[0])
            self.cards_robot.remove(robot_att[0])
            cardsrobranks[robot_att[0][1]] -= 1
        else:
            cardgame.append(robot_att_trump[0])
            self.cards_robot.remove(robot_att_trump[0])
            cardsrobranks[robot_att_trump[0][1]] -= 1
        print("Ходжу:{0} {1}".format(self.draw_suit[cardgame[0][0]],cardgame[0][1]))
        return cardgame,self.cards_robot

    def defence(self,cardgame,cards_robot,trump):
        cardsrobranks = self.eval_rob_ranks(self.cards_robot)
        self.result = ''
        robot_def = []
        robot_def_trump = []
        # find the variance for defence
        for card in self.cards_robot:
            if self.card_ranks.index(card[1]) > self.card_ranks.index(cardgame[0][1]) \
                and card[0] == cardgame[0][0]:
                robot_def.append(card)
            elif cardgame[0][0] != self.trump[0] and card[0] == self.trump[0] :
                robot_def_trump.append(card)
        robot_def.sort()
        robot_def_trump.sort()
        if len(robot_def) != 0:
            cardgame.append(robot_def[0])
            self.result = 'beat'
        elif len(robot_def_trump) != 0:
            cardgame.append(robot_def_trump[0])
            self.result = 'beat_trump'
        else:
            self.result = 'take'

        if self.result == 'beat':
            self.cards_robot.remove(cardgame[1])
            cardsrobranks[cardgame[1][1]] -= 1
            print("{0} {1} Бито!"\
            .format(self.draw_suit[cardgame[1][0]],cardgame[1][1]))
        elif self.result == 'beat_trump':
            self.cards_robot.remove(cardgame[1])
            cardsrobranks[cardgame[1][1]] -= 1
            print("{0} {1} Б'ю Козирем!"\
            .format(self.draw_suit[cardgame[1][0]],cardgame[1][1]))
        else:
            self.cards_robot.extend(cardgame)
            cardsrobranks[cardgame[0][1]] += 1
        return self.result,self.cards_robot

class Game:
    deck_weight = [ 'C6','C7','C8','C9','CT','CJ','CQ','CK','CA',
                    'D6','D7','D8','D9','DT','DJ','DQ','DK','DA',
                    'H6','H7','H8','H9','HT','HJ','HQ','HK','HA',
                    'S6','S7','S8','S9','ST','SJ','SQ','SK','SA'
                    ]
    draw_suit = {'C': '\u2667','D': '\u2666','H': '\u2665','S': '\u2664'}

    def __init__(self,trump_pla,trump_rob,trump):
        self.trump_pla = trump_pla
        self.trump_rob = trump_rob
        self.trump = trump

    def trumping(self,trump_pla,trump_rob,trump):
        self.step_player = False
        self.step_robot = False

        if self.trump_rob == 'NO' and self.trump_pla == 'NO':
            print("Козирів немає,даю тобі фору, ходи:", end='')
            self.step_player = True
        elif self.trump_rob != 'NO' and self.trump_pla == 'NO':
            print("Я козиряю {0} {1}, тож мій хід! "\
            .format(self.draw_suit[self.trump[0]],self.trump_rob[1]))
            self.step_robot = True
        elif self.trump_pla != 'NO' and self.trump_rob == 'NO':
            print("Ти козиряєш {0} {1} і ходиш перший!"\
            .format(self.draw_suit[self.trump[0]],self.trump_pla[1]))
            self.step_player = True
        else:
            if self.deck_weight.index(self.trump_rob) \
                < self.deck_weight.index(self.trump_pla):
                print("Мій козир {0} {1} молодший, я ходжу! "\
                .format(self.draw_suit[self.trump[0]],self.trump_rob[1]))
                self.step_robot = True
            else:
                print("Твій козир {0} {1} молодший мого {2} {3}, ходи! "\
                .format(self.draw_suit[self.trump[0]],self.trump_pla[1],\
                self.draw_suit[trump[0]],self.trump_rob[1]))
                self.step_player = True
        return self.step_player,self.step_robot
