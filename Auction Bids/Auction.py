import art

go_on=False
def highest_bidder(bidding):
    highest_bid = 0
    winner = ""
    for bidder in bidding:
        bid_amount = bidding[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"\n\nThe winner is {winner} with a bid of ${highest_bid}\n\n")


go_on=True
while go_on:
    print(art.logo)
    name=input("What is your name?\n")
    price=int(input("What is your bid?\n$"))
    bids={}
    bids[name]=price


    Loop=input("Are there any ther bidders?\nType 'yes' or 'no'\n").lower()
    if Loop == "yes":
        print("\n"*100)
        go_on=True
    else:
        go_on=False
        highest_bidder(bids)

