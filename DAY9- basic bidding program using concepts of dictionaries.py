bids={}

def highest_bidding_amount(bidding_dictionary):
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount> highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

choice=True

while choice == True:
    name=input("What is your name?:\n")
    bid=int(input("What is your bid?:\n$"))
    yes_no = input("Are there any other bidders? type 'yes' or 'no'\n").lower()
    bids[name]=bid
    if yes_no=="no":
        choice=False
        highest_bidding_amount(bids)
    elif yes_no=="yes":
        print("\n"*20)



