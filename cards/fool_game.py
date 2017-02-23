# -*- coding: utf-8 -*-
from random import choice,randint,shuffle
from os import system

card_ranks = [ '6','7','8','9','T','J','Q','K','A' ]
cards_rob_ranks = {'6':0,'7':0,'8':0,'9':0,'T':0,'J':0,'Q':0,'K':0,'A':0}
draw_map_suit = {'C': '\u2667', 'D': '\u2666', 'H': '\u2665', 'S': '\u2664'}
deck_cards_weighted = [ 'C6','C7','C8','C9','CT','CJ','CQ','CK','CA',
                        'D6','D7','D8','D9','DT','DJ','DQ','DK','DA',
                        'H6','H7','H8','H9','HT','HJ','HQ','HK','HA',
                        'S6','S7','S8','S9','ST','SJ','SQ','SK','SA'
                        ]
cardgame = []

def shuffle_give_cards():
    global cards_rob_ranks, deck_cards_rand
    cards_robot = []
    cards_player = []
    trump=''
    deck_cards_rand = [ 'C6','C7','C8','C9','CT','CJ','CQ','CK','CA',
                        'D6','D7','D8','D9','DT','DJ','DQ','DK','DA',
                        'H6','H7','H8','H9','HT','HJ','HQ','HK','HA',
                        'S6','S7','S8','S9','ST','SJ','SQ','SK','SA'
                        ]
    # shuffle deck ten times
    for i in range(10):
        shuffle(deck_cards_rand)

    # distribute card
    for i in range(6):
        cards_player.append(deck_cards_rand[-1])
        deck_cards_rand.pop()
        cards_robot.append(deck_cards_rand[-1])
        deck_cards_rand.pop()
    cards_player.sort()
    cards_robot.sort()

    # robot evaluate ranks
    for card in cards_robot:
        cards_rob_ranks[card[1]] += 1

    # trump to table
    trump = deck_cards_rand[randint(0,len(deck_cards_rand)-1)]
    deck_cards_rand.remove(trump)
    deck_cards_rand.insert(0,trump)

    return deck_cards_rand, cards_player, cards_robot, trump

def see_cards(deck_cards_rand,cards_player,trump):
    system('clear')
    print("{0} The Card Game: Sipmle Duren' {0}".format('='*30) )
    print(  '\t\tКарта вводиться 2-ма латинськими літерами, '
            'наприклад: ha (Черва Туз)\n\n\t'
            '{0} => C (clubs|трефа),{1} => D (diamonds|бубна),'
            '{2} => H (hearts|черва),{3} => S (spades|піка)'
            .format(draw_map_suit['C'],draw_map_suit['D'],\
            draw_map_suit['H'],draw_map_suit['S']))
    print(  '\n\tT => Ten|Десятка, J => Jack|Валет, Q => Queen|Королева, '
            'K => King|Король, A => Ace|Туз\n')
    print("\t\tКоли немає чим бити, забрати карту => take\n")
    print('\n' + '='*90)
    print("Твої карти:", end=' ')
    for card in cards_player:
        print("{0} {1} ".format(draw_map_suit[card[0]],card[1]), end='')
    if len(deck_cards_rand) > 0:
        print("\nКарти на столі: %s " % len(deck_cards_rand[1:]), end='')
        print("+ {0} {1} Козир".format(draw_map_suit[trump[0]],trump[1]))
    else:
        print("\nкозир:{0} {1}".format(draw_map_suit[trump[0]],trump[1]))
    print("{0} Карти в грі {0}".format('='*10) )
    return 0

def pla_take_card(cards_player,deck_cards_rand):
    while len(cards_player) < 6:
        if len(deck_cards_rand) == 0: break
        cards_player.append(deck_cards_rand[-1])
        deck_cards_rand.pop()
    return cards_player,deck_cards_rand

def rob_take_card(cards_robot,deck_cards_rand):
    global cards_rob_ranks
    while len(cards_robot) < 6:
        if len(deck_cards_rand) == 0: break
        cards_robot.append(deck_cards_rand[-1])
        cards_rob_ranks[cards_robot[-1][1]] += 1
        deck_cards_rand.pop()
    return cards_robot,deck_cards_rand

def trump_robot(cards_robot,trump):
    trump_robot = 'NO'
    for card in cards_robot:
        if card[0] == trump[0]:
            if trump_robot != 'NO':
                if deck_cards_weighted.index(card) \
                    < deck_cards_weighted.index(trump_robot):
                    trump_robot = card
                else:
                    continue
            else:
                trump_robot = card
    return trump_robot

def trump_player(cards_player,trump):
    trump_player = ''
    while trump_player == '':
        trump_player = input("Покажи молодший козир, "
                            "якщо немає, введи 'no':").upper()
        if trump_player == 'NO': break
        if trump_player not in cards_player:
            trump_player = input("Тільки козир або 'no'?:").upper()
        if trump_player in cards_player and trump_player[0] == trump[0]: break
        else:
            if trump_player == 'NO': break
            trump_player = input("Це не твій козир!Востаннє - "
                                 "козир або 'no'?:").upper()
            if trump_player in cards_player and trump_player[0] == trump[0]:
                break
            else:
                trump_player = 'NO'
    return trump_player

def trumping(trump_player,trump_robot,trump):
    step_robot = False
    step_player = False

    if trump_robot == 'NO' and trump_player == 'NO':
        print("Козирів немає, даю тобі фору, ходи:", end='')
        step_player = True
    elif trump_robot != 'NO' and trump_player == 'NO':
        print("Я козиряю {0} {1}, тож мій хід! "\
        .format(draw_map_suit[trump[0]],trump_robot[1]))
        step_robot = True
    elif trump_player != 'NO' and trump_robot == 'NO':
        print("Ти козиряєш {0} {1} і ходиш перший!"\
        .format(draw_map_suit[trump[0]],trump_player[1]))
        step_player = True
    else:
        if deck_cards_weighted.index(trump_robot) \
        < deck_cards_weighted.index(trump_player):
            print("Мій козир {0} {1} молодший, я ходжу! "\
            .format(draw_map_suit[trump[0]],trump_robot[1]))
            step_robot = True
        else:
            print("Твій козир {0} {1} молодший мого {2} {3}, ходи! "\
            .format(draw_map_suit[trump[0]],trump_player[1],\
            draw_map_suit[trump[0]],trump_robot[1]))
            step_player = True
    return step_player, step_robot

def robot_attack(cards_robot,trump):
    global cardgame, cards_rob_ranks, card_ranks
    cardgame = []
    robot_att = []
    robot_att_trump = []
    for rank in card_ranks:
        if cards_rob_ranks[rank] > 0:
            for card in cards_robot:
                if card[1] == rank and card[0] != trump[0]:
                    robot_att.append(card)
                else:
                    robot_att_trump.append(card)
    if len(robot_att) != 0:
        cardgame.append(robot_att[0])
        cards_robot.remove(robot_att[0])
        cards_rob_ranks[robot_att[0][1]] -= 1
    else:
        cardgame.append(robot_att_trump[0])
        cards_robot.remove(robot_att_trump[0])
        cards_rob_ranks[robot_att_trump[0][1]] -= 1
    print("Ходжу:{0} {1}".format(draw_map_suit[cardgame[0][0]],cardgame[0][1]))
    return cards_robot

def robot_defence(cards_robot,trump):
    global cardgame, cards_rob_ranks, card_ranks
    result = ''
    robot_def = []
    robot_def_trump = []
    # find the variance for defence
    for card in cards_robot:
        if card_ranks.index(card[1]) > card_ranks.index(cardgame[0][1]) \
            and card[0] == cardgame[0][0]:
            robot_def.append(card)
        elif cardgame[0][0] != trump[0] and card[0] == trump[0] :
            robot_def_trump.append(card)
    robot_def.sort()
    robot_def_trump.sort()
    if len(robot_def) != 0:
        cardgame.append(robot_def[0])
        result = 'beat'
    elif len(robot_def_trump) != 0:
        cardgame.append(robot_def_trump[0])
        result = 'beat_trump'
    else:
        result = 'take'

    if result == 'beat':
        cards_robot.remove(cardgame[1])
        cards_rob_ranks[cardgame[1][1]] -= 1
        print("{0} {1} Бито!"\
        .format(draw_map_suit[cardgame[1][0]],cardgame[1][1]))
    elif result == 'beat_trump':
        cards_robot.remove(cardgame[1])
        cards_rob_ranks[cardgame[1][1]] -= 1
        print("{0} {1} Б'ю Козирем!"\
        .format(draw_map_suit[cardgame[1][0]],cardgame[1][1]))
    else:
        cards_robot.extend(cardgame)
        cards_rob_ranks[cardgame[0][1]] += 1
    return result, cards_robot

def player_attack(cards_player,trump):
    global cardgame
    cardgame = []
    card = input("Твій хід>").upper()
    while card not in cards_player:
        card = input("В тебе немає цеї карти, введи карту:").upper()
    cardgame.append(card)
    cards_player.remove(card)
    print("{0} {1}".format(draw_map_suit[cardgame[0][0]],cardgame[0][1]))
    return cards_player

def player_defence(cards_player,trump):
    global cardgame, deck_cards_rand, card_ranks
    result = ''
    card = input("Бити>").upper()
    while card not in cards_player:
        if card.lower() == 'take':
            result = 'take'
            break
        if card in cards_player:
            break
        else:
            card = input("В тебе немає цеї карти, карту або 'take':").upper()
    if result != 'take':
        cardgame.append(card)
        if card_ranks.index(cardgame[1][1]) > card_ranks.index(cardgame[0][1])\
            and cardgame[1][0] == cardgame[0][0]:
            result = 'beat'
        elif cardgame[1][0] == trump[0] and cardgame[0][0] != trump[0]:
            result = 'beat_trump'
        else:
            cards_player.remove(card)
            result = 'take'
    if result == 'beat':
        cards_player.remove(card)
        print("{0} {1} Бито!" \
        .format(draw_map_suit[cardgame[1][0]],cardgame[1][1]))
    elif result == 'beat_trump':
        cards_player.remove(card)
        print("{0} {1} Козир!!!" \
        .format(draw_map_suit[cardgame[1][0]],cardgame[1][1]))
    else:
        cards_player.extend(cardgame)
        print("Щоб я скис! Ти забрав...")
    return result, cards_player
