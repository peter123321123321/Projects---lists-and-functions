def welcome():
    print("--------------------------------"
          "--- Welcome to Mgs Childcare ---"
          "--------------------------------")
    task = int(input("What would you like to do today "
                 "\n[1] Check a child in "
                 "\n[2] Check a child out"
                 "\n[3] Calculate the cost"
                 "\n[4] Show child roll"
                 "\n[5] Exit"))
    if task == 1:
        drop_off()
    elif task == 2:
        pick_up()
    elif task == 3:
        calc_cost()
    elif task == 4:
        print_roll()
    elif task == 5:
        print("Thank you for using Mgs Childcare")
        exit()


def drop_off():
    while True:
        question = input("[Y/N]Would you like to check in a child?").upper()
        if question == "Y":
            check_in = input("What is the name of the child you would like to check in?")
            roll.append(check_in)
        elif question == "N":
            print("Returning to menu")
            print()
            return welcome()


def pick_up():
    while True:
        question = input("[Y/N]Would you like to check out a child?").upper()
        if question == "Y":
            check_in = input("What is the name of the child you would like to check out?")
            roll.remove(check_in)
        elif question == "N":
            print("Returning to menu")
            print()
            return welcome()


def calc_cost():
    while True:
        question = input("[Y/N]Would you like to calculate the cost?").upper()
        if question == "Y":
            hours = int(input("How many hours would you like for us to look after your children"))
            check_in = input(f"The cost to look after {len(roll)} children for {hours} hours is {len(roll)*hours*12}")
        elif question == "N":
            print("Returning to menu")
            print()
            return welcome()


def print_roll():
    while True:
        question = input("[Y/N]Would you like to see the roll").upper()
        if question == "Y":
            print(roll)
        elif question == "N":
            print("Returning to menu")
            print()
            return welcome()


# Main Routine
roll = list()
welcome()