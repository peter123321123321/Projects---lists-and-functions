

# Main Routine
bid = 0
highest_bid = 0
item = input("What would you like to auction")
reserve = int(input("What is the reserve for your item"))
while bid != "im so bad i cant even win a bid":
    bid = int(input("What is your bid [-1 to quit]"))
    if bid >= highest_bid:
        highest_bid = bid
        print(f"the highest bid is {highest_bid}")
    elif bid == -1:
        break
    else:
        print(f"Sorry {bid} was not high enough")

if highest_bid >= reserve:
    print("Congrats you have won the auction")
else:
    print("Sorry you have no reached the reserve the item will not be sold")
