# -*- coding: utf-8 -*-

from random import choice,randint,shuffle

suit = ['clubs','diamonds','hearts','spades']
card_ranks = ['6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace' ]
draw_map_suit = {'clubs': '\u2667', 'diamonds': '\u2666', 'hearts': '\u2665', 'spades': '\u2664'}
deck_cards_weighted = [
                    ('clubs', '6'),
                    ('clubs', '7'),
                    ('clubs', '8'),
                    ('clubs', '9'),
                    ('clubs', '10'),
                    ('clubs', 'Jack'),
                    ('clubs', 'Queen'),
                    ('clubs', 'King'),
                    ('clubs', 'Ace'),
                    ('diamonds', '6'),
                    ('diamonds', '7'),
                    ('diamonds', '8'),
                    ('diamonds', '9'),
                    ('diamonds', '10'),
                    ('diamonds', 'Jack'),
                    ('diamonds', 'Queen'),
                    ('diamonds', 'King'),
                    ('diamonds', 'Ace'),
                    ('hearts', '6'),
                    ('hearts', '7'),
                    ('hearts', '8'),
                    ('hearts', '9'),
                    ('hearts', '10'),
                    ('hearts', 'Jack'),
                    ('hearts', 'Queen'),
                    ('hearts', 'King'),
                    ('hearts', 'Ace'),
                    ('spades', '6'),
                    ('spades', '7'),
                    ('spades', '8'),
                    ('spades', '9'),
                    ('spades', '10'),
                    ('spades', 'Jack'),
                    ('spades', 'Queen'),
                    ('spades', 'King'),
                    ('spades', 'Ace')
                    ]
deck_cards_rand = []
cards_robot = []
cards_player = []
trump = ()

def shuffle_deck():
    global deck_cards_rand
    deck_cards_rand = []
    card_ranks_clubs = ['6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    card_ranks_diamonds = ['6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    card_ranks_hearts = ['6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    card_ranks_spades = ['6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck_cards = {  'clubs': card_ranks_clubs,
                    'diamonds': card_ranks_diamonds,
                    'hearts': card_ranks_hearts,
                    'spades': card_ranks_spades
                }

    for key in deck_cards.keys():
        shuffle(deck_cards[key])

    while len(deck_cards_rand) < 36:
        suit_tmp = choice(suit)
        if deck_cards[suit_tmp] == []:
            continue
        rank_tmp = choice(deck_cards[suit_tmp])
        deck_cards_rand.append((suit_tmp,rank_tmp))
        deck_cards[suit_tmp].remove(rank_tmp)

    return deck_cards_rand

def start_new_game():
    i = 0
    global trump
    while i < 6:
        cards_player.append(deck_cards_rand[-1])
        deck_cards_rand.pop()
        cards_robot.append(deck_cards_rand[-1])
        deck_cards_rand.pop()
        i += 1
    trump = deck_cards_rand[randint(0,len(deck_cards_rand))]
    deck_cards_rand.remove(trump)
    return cards_player, cards_robot, trump

def see_cards(cards_player):
    print("Підказка: {0} = clubs(трефа),{1} = diamonds(бубна),{2} = hearts(черва),{3} = spades(піка)"\
    .format(draw_map_suit['clubs'],draw_map_suit['diamonds'],draw_map_suit['hearts'],draw_map_suit['spades']))
    print("Ваші карти:", end=' ')
    for card in cards_player:
        print("[{0} {1}] ".format(draw_map_suit[card[0]],card[1]), end='')
    return 0

def game(deck_cards_weighted,deck_cards_rand,cards_player,cards_robot,trump):
    card_in_game = []
    cards_beaten = []
    global draw_map_suit
    player_up_trump = tuple(input("Покажіть вагу вашого козира, якщо немає, введіть 'no':").split(' '))
    robot_up_trump = ()

    for t in cards_robot:
        if t[0] == trump[0]:
            if robot_up_trump != ():
                if deck_cards_weighted.index(robot_up_trump) > deck_cards_weighted.index(t):
                    robot_up_trump = t
                else:
                    continue
            robot_up_trump = t

    if robot_up_trump == () and player_up_trump[0] == 'no':
        print("Козирів немає, ваш хід:")
    elif robot_up_trump != () and player_up_trump[0] == 'no':
        print("Робот показує козир: [{0} {1}]".format(draw_map_suit[trump[0]],robot_up_trump[1]))
    elif player_up_trump != () and robot_up_trump == ():
        print("Ви показуєте козир [{0} {1}] і ходите перші:"\
        .format(draw_map_suit[trump[0]],player_up_trump[1]))
    else:
        if deck_cards_weighted.index(robot_up_trump) > deck_cards_weighted.index(player_up_trump):
            print("Робот показує козир [{0} {1}] вагоміший вашого, його хід: "\
            .format(draw_map_suit[trump[0]],robot_up_trump[1]))
        else:
            print("Ваш козир [{0} {1}] вагоміший ніж в робота [{2} {3}], ваш хід: "\
            .format(draw_map_suit[trump[0]],player_up_trump[1],draw_map_suit[trump[0]],robot_up_trump[1]))
    return 0

shuffle_deck()
#print(deck_cards_rand)
print("===========start game=================")
start_new_game()
#print("cards_player: %s" % cards_player)
see_cards(cards_player)
#print("cards_robot: %s" % cards_robot)
print("\ntrump(козир): [{0} {1}]".format(draw_map_suit[trump[0]],trump[1]))
#print("deck: %s" % deck_cards_rand)
print(len(deck_cards_rand))
game(deck_cards_weighted,deck_cards_rand,cards_player,cards_robot,trump)
