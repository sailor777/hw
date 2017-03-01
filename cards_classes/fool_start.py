# -*- coding: utf-8 -*-
from time import sleep
from fool_game import Cards,Player,Robot,Game

result = ''
winner = ''
game_run = 'y'
cardg = []
player_name = input("Введи своє ім'я:").capitalize()

i = 0
while not player_name.isalpha():
    player_name = input("Введи людське ім'я:").capitalize()
    if player_name.isalpha():
        print("Привіт, %s =)" % player_name)
        break
    if i == 2:
        print("OK!Дістав, привіт %s =)" % player_name)
        break
    i += 1

deck_game = Cards()

while game_run == 'y':
    print("Ок!Поїхали %s" % player_name)
    sleep(2)
    ######## Start ########
    # shuffle deck
    deck = deck_game.shuffle_deck()
    # make trump
    trump = deck_game.make_trump()
    # distribute cards for play's and take cards from table
    cards_player, cards_robot = deck_game.give_cards()
    cards_player.sort()
    cards_robot.sort()
    # define players
    player = Player(deck,cards_player,trump)
    robot = Robot(deck,cards_robot,trump)
    # player see cards and table
    player.see_cards(deck,cards_player,trump)
    # determine younger trump
    trump_pla = player.see_trump(cards_player,trump)
    trump_rob = robot.see_trump(cards_robot,trump)
    # determine whose first step
    gamgam = Game(trump_pla,trump_rob,trump)
    step_player, step_robot = gamgam.trumping(trump_pla,trump_rob,trump)

    while len(cards_robot) > 0 and len(cards_player) > 0:
        if step_robot:
            cardg, cards_robot = robot.attack(cards_robot,trump)
            result, cards_player = player.defence(cardg,cards_player,trump)
            if result == 'beat' or result == 'beat_trump':
                step_robot = False
                step_player = True
                sleep(2)
            elif result == 'take':
                sleep(2)
        else:
            cardg, cards_player = player.attack(cards_player,trump)
            result, cards_robot = robot.defence(cardg,cards_robot,trump)
            if result == 'beat' or result == 'beat_trump':
                step_robot = True
                step_player = False
                sleep(2)
            elif result == 'take':
                print("Холєра!Я забираю..")
                sleep(2)

        if len(deck) > 0:
            if step_player:
                cards_robot,deck = deck_game.give_cards_rob(cards_robot,deck)
                cards_player,deck = deck_game.give_cards_pla(cards_player,deck)
            else:
                cards_player,deck = deck_game.give_cards_pla(cards_player,deck)
                cards_robot,deck = deck_game.give_cards_rob(cards_robot,deck)
            cards_robot.sort()
            cards_player.sort()

        if len(cards_robot) > 0 and len(cards_player) > 0:
            player.see_cards(deck,cards_player,trump)
        elif len(cards_robot) == 0 and len(cards_player) == 0:
            winner = 'NO'
            break
        elif len(cards_robot) > 0 and len(cards_player) == 0:
            winner = 'You'
            break
        elif len(cards_robot) == 0 and len(cards_player) > 0:
            winner = 'Me'
            break

    if winner == 'Me':
        game_run = input("Я виграв! Граємо далі? 'y'/'n':")
    elif winner == 'You':
        game_run = input("Вітаю %s!Ти виграв, граємо далі? 'y'/'n':" % player_name)
    elif winner == 'NO':
        game_run = input("Нічия!!! Граємо далі? 'y'/'n':")

    if game_run.lower() != 'y' and game_run.lower() != 'n':
        game_run = 'y'
    elif game_run.lower() == 'n':
        print("Па-па, дякую за гру!")
