# -*- coding: utf-8 -*-

from random import choice,randint,shuffle
from os import system

card_ranks = [ '6','7','8','9','T','J','Q','K','A' ]
draw_map_suit = {'C': '\u2667', 'D': '\u2666', 'H': '\u2665', 'S': '\u2664'}
deck_cards_weighted = [ 'C6','C7','C8','C9','CT','CJ','CQ','CK','CA',
                        'D6','D7','D8','D9','DT','DJ','DQ','DK','DA',
                        'H6','H7','H8','H9','HT','HJ','HQ','HK','HA',
                        'S6','S7','S8','S9','ST','SJ','SQ','SK','SA'
                        ]
deck_cards_rand = []
cards_robot = []
cards_player = []
trump = ''

def shuffle_deck():
    global deck_cards_rand
    deck_cards_rand = [ 'C6','C7','C8','C9','CT','CJ','CQ','CK','CA',
                        'D6','D7','D8','D9','DT','DJ','DQ','DK','DA',
                        'H6','H7','H8','H9','HT','HJ','HQ','HK','HA',
                        'S6','S7','S8','S9','ST','SJ','SQ','SK','SA'
                        ]
    # shuffle the deck 10 times
    i = 0
    while i < 10:
        shuffle(deck_cards_rand)
        i += 1
    return deck_cards_rand

def start_new_game():
    global trump
    # distribute card !
    i = 0
    while i < 6:
        cards_player.append(deck_cards_rand[-1])
        deck_cards_rand.pop()
        cards_robot.append(deck_cards_rand[-1])
        deck_cards_rand.pop()
        i += 1
    # trump to table !
    trump = deck_cards_rand[randint(0,len(deck_cards_rand))]
    deck_cards_rand.remove(trump)
    return cards_player.sort(), cards_robot.sort(), trump

def see_cards(cards_player):
    system('clear')
    print("================ The Card Game: Sipmle Duren'=================")
    print("Підказка для вводу: карта вводиться 2-ма латинськими літерами, наприклад: HA (Черва Туз)\n\n\
    \t{0} =>C (clubs|трефа),{1} =>D (diamonds|бубна),{2} =>H (hearts|черва),{3} =>S (spades|піка)"\
    .format(draw_map_suit['C'],draw_map_suit['D'],draw_map_suit['H'],draw_map_suit['S']))
    print("\tT => Ten|Десятка,J => Jack|Валет,Q => Queen|Королева,K => King|Король,A => Ace|Туз\n")
    print("Відбій => beat, Забираю => take\n")
    print("Ваші карти:", end=' ')
    for card in cards_player:
        print("[{0} {1}] ".format(draw_map_suit[card[0]],card[1]), end='')
    print("\ntrump(козир): [{0} {1}]".format(draw_map_suit[trump[0]],trump[1]))
    print("Cards on table=%s" % len(deck_cards_rand))
    return 0

def game(deck_cards_weighted,deck_cards_rand,cards_player,cards_robot,trump):
    global draw_map_suit
    global card_ranks
    card_in_game = []
    robot_up_trump = ''
    step_robot = 0
    step_player = 0
    player_up_trump = input("Покажіть ваш козир, якщо немає, введіть 'no':").upper()
    while player_up_trump not in cards_player:
        if player_up_trump == 'NO': break
        player_up_trump = input("У Вас немає такої карти, введіть карту, або 'no':").upper()

    # What smallest robots trump
    for card in cards_robot:
        if card[0] == trump[0]:
            if robot_up_trump != '':
                if deck_cards_weighted.index(card) < deck_cards_weighted.index(robot_up_trump):
                    robot_up_trump = card
                else:
                    continue
            robot_up_trump = card

    # Trumping
    if robot_up_trump == '' and player_up_trump == 'NO':
        print("Козирів немає, ваш хід:")
        step_player = 1
    elif robot_up_trump != '' and player_up_trump == 'NO':
        print("Я показую козир [{0} {1}], мій хід: ".format(draw_map_suit[trump[0]],robot_up_trump[1]))
        step_robot = 1
    elif player_up_trump != '' and robot_up_trump == '':
        print("Ви показуєте козир [{0} {1}] і ходите перші:"\
        .format(draw_map_suit[trump[0]],player_up_trump[1]))
        step_player = 1
    else:
        if deck_cards_weighted.index(robot_up_trump) < deck_cards_weighted.index(player_up_trump):
            print("Мій козир [{0} {1}] молодший, мій хід: "\
            .format(draw_map_suit[trump[0]],robot_up_trump[1]))
            step_robot = 1
        else:
            print("Ваш козир [{0} {1}] молодший мого [{2} {3}], ваш хід: "\
            .format(draw_map_suit[trump[0]],player_up_trump[1],draw_map_suit[trump[0]],robot_up_trump[1]))
            step_player = 1

    # bouts: attack ROBOT
    while len(deck_cards_rand) > 0:
        robot_attack = []
        robot_attack_trump = []
        while step_robot == 1:
            for card in cards_robot:
                if card[0] != trump[0] and card[1] in card_ranks[:5]:
                    robot_attack.append(card)
                elif card[0] != trump[0] and card[1] in card_ranks[5:]:
                    robot_attack.append(card)
                else:
                    robot_attack_trump.append(card)
            i = 0
            while i < 1:
                if len(robot_attack) > 0:
                    card = choice(robot_attack)
                    card_in_game.append(card)
                    print("[{0} {1}]".format(draw_map_suit[card[0]],card[1]))
                    cards_robot.remove(card)

                elif len(robot_attack_trump) > 0:
                    card = choice(robot_attack_trump)
                    card_in_game.append(card)
                    print("[{0} {1}]".format(draw_map_suit[card[0]],card[1]))
                    cards_robot.remove(card)

                card = input("Бити>").upper()
                while card not in cards_player:
                    card = input("Ви немаєте цеї карти, введіть карту, або 'take':").upper()
                    if card == 'take':
                        cards_player.extend(card_in_game)
                        card_in_game = []
                    break

                card_in_game.append(card)
                print("[{0} {1}]".format(draw_map_suit[card[0]],card[1]))
                if deck_cards_weighted.index(card_in_game[1]) < deck_cards_weighted.index(card_in_game[0]):
                    print("Ви змахлювали, забирайте карти!")
                    cards_player.extend(card_in_game)
                elif [card_in_game[1]][0] == trump[0] \
                    and deck_cards_weighted.index(card_in_game[1]) < deck_cards_weighted.index(card_in_game[0]):
                    cards_player.remove(card)
                    print("Бито!")

                cards_robot.append(deck_cards_rand[-1])
                deck_cards_rand.pop()
                if len(cards_player) < 6:
                    cards_player.append(deck_cards_rand[-1])
                    deck_cards_rand.pop()
                card_in_game = []
                step_robot = 0
                step_player = 1
                i += 1

            see_cards(cards_player)
        while step_player == 1:
            card = input("Ваш хід>").upper()
            while card not in cards_player:
                card = input("Ви немаєте цеї карти, введіть карту:").upper()
                card_in_game.append(card)
            print("[{0} {1}]".format(draw_map_suit[card[0]],card[1]))

    return step_robot,step_player

shuffle_deck()
start_new_game()
see_cards(cards_player)
game(deck_cards_weighted,deck_cards_rand,cards_player,cards_robot,trump)
