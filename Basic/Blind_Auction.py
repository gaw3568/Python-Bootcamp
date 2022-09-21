# 비밀 경매 프로그램
from Secret_Bid_Art import logo

def Find_highest_bid(bids_record):
    """Print person who bids the highest money """
    highest_record = 0
    highest_record_name = ""
    for person in bids_record:
        if bids_record[person] > highest_record:
            highest_record = bids_record[person]
            highest_record_name = person
    print(f"The winner is {highest_record_name} with a bid of ${highest_record}")

print(logo)

bids = {}
isFinished = False

while not isFinished:
    name = input("What is your name? : ")
    price = int(input("What is your bid? : $"))
    bids[name] = price
    answer = input("Are there any other bidders? Type 'yes' or 'no'. ")

    if answer == "no":
        isFinished = True

Find_highest_bid(bids)
