import random
from art import logo, vs
from game_data import data

def pick_item(data_list):
    item = random.choice(data_list)
    return item

def compare_items(answer, follower_A, follower_B):
    if follower_A > follower_B:
        return answer == 'A'
    else:
        return answer == 'B'

def game():
    score = 0
    is_playing = False
    print(logo)
    item_B = pick_item(data)

    while not is_playing:
        item_A = item_B
        item_B = pick_item(data)

        while item_A == item_B:
            item_B = pick_item(data)

        print(f"Compare A: {item_A['name']}, {item_A['description']}, from {item_A['country']}")
        print(vs)
        print(f"Compare B: {item_B['name']}, {item_B['description']}, from {item_B['country']}")
        answer = input("Who has more followers? Type 'A' or 'B': ").upper()
        is_correct = compare_items(answer, item_A['follower_count'], item_B['follower_count'])

        print(logo)
        
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            is_playing = True
            print(f"Sorry, that's wrong. Final score: {score}")

game()
