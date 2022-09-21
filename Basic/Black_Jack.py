############### Our Blackjack House Rules #####################
## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from Black_Jack_Art import logo
import random

card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

while True:
    play_y_or_n = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    if play_y_or_n == 'y':
        print(logo)
        user_card_list = []
        dealer_card_list = []
        user_sum_of_cards = 0
        dealer_sum_of_cards = 0

        for index in range(2):
            user_card_list.append(random.choice(card))
            user_sum_of_cards += user_card_list[index]
            dealer_card_list.append(random.choice(card))
            dealer_sum_of_cards += dealer_card_list[index]
        
        print(f"Your card : {user_card_list}, current score : {user_sum_of_cards}")
        print(f"Computer's first card : {dealer_card_list[0]}")

        # 딜러 카드의 합이 16을 넘지않는 경우
        while dealer_sum_of_cards < 17:
            another_card = random.choice(card)
            dealer_card_list.append(another_card)
            dealer_sum_of_cards += another_card

            if (dealer_sum_of_cards > 21) and (11 in dealer_card_list):
                dealer_card_list.remove(11)
                dealer_card_list.append(1)
                dealer_sum_of_cards -= 10

        # 처음 뽑힌 두 카드의 합이 21이면 블랙잭이므로 게임 종료.
        if (user_sum_of_cards == 21) and (user_sum_of_cards == dealer_sum_of_cards):
            print("Win! It is Blackjack")
            continue

        isChosen_new_card = True

        # yes응답으로 또 다른 카드를 뽑는 경우
        while isChosen_new_card and (user_sum_of_cards < 21):
            choose_next_card = input("Type 'y' to get another card, type 'n' pass: ").lower()

            if choose_next_card == 'n':
                isChosen_new_card = False
            elif choose_next_card == 'y':
                another_card = random.choice(card)
                user_card_list.append(another_card)
                user_sum_of_cards += another_card

                if (user_sum_of_cards > 21) and (11 in user_card_list):
                    user_card_list.remove(11)
                    user_card_list.append(1)
                    user_sum_of_cards -= 10
                
                print(f"Your card : {user_card_list}, current score : {user_sum_of_cards}")
                print(f"Computer's first card : {dealer_card_list[0]}")

        print(f"Your card : {user_card_list}, final score : {user_sum_of_cards}")
        print(f"Computer's final hand : {dealer_card_list}, final score : {dealer_sum_of_cards}")

        if user_sum_of_cards > 21 and dealer_sum_of_cards > 21:
            print("You lose")
        elif dealer_sum_of_cards > 21:
            print("You win")
        elif user_sum_of_cards > 21:
            print("You lose")
        else:
            if user_sum_of_cards < dealer_sum_of_cards:
                print("You lose") 
            elif user_sum_of_cards == dealer_sum_of_cards:
                print("Draw")
            elif user_sum_of_cards > dealer_sum_of_cards:
                print("You win")

    elif play_y_or_n == "n":
        print("Game is over")
        break
    else:
        print("Your answer is wrong. please try program again!")
        break