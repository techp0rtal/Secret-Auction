from art import logo

print(logo)
print("Welcome to the secret auction program.")

bidders = {}
bids_list = [0]
auction_over = False
winner = ""

#My method: Make an empty list, add all the bids there. Find the biggest number in that list, then match the biggest number to the key.
#but how do you find a key with the value in python? can use .items() or do an if statement
while auction_over == False:
    name = input("What is your name?: ")
    bid = float(input("What's your bid?: "))
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.")
    bidders[name] = bid
    bids_list.append(bid)
    if other_bidders == "no":
        auction_over = True
        highest_bid = max(bids_list)
        for dude in bidders:
            if bidders[dude] == highest_bid:
                winner = dude
    else:
        print("\n" *100)

print(bidders)
print(f"The winner is {winner} with a bid of ${highest_bid}")

