average_time = list()
average_cost = list()

name = input("What is your name")
while True:
    trip = input("Would you like to start a new trip[n/y]").lower()
    if trip == "y":
        time = int(input("How long did the trip take"))
        cost = time*2+10
        print(f"The cost for your ride is {cost}")
        average_time.append(time)
        average_cost.append(cost)
    else:
        print(f"Thank you for driving with us {name} You have traveled for a total of {sum(average_time)} minutes "
              f"with an average of {sum(average_time)/len(average_time)} minutes per trip"
              f""
              f"\nthe total cost is ${sum(average_cost)} and "
              f"the average cost of your trips are ${sum(average_cost)/len(average_cost)}")
        break