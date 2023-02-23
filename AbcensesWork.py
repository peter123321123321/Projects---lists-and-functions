def names():
    absence_list = list()
    while True:
        name = input("Enter employee name (or $ to exit): ")
        if name == "$":
            break
        days = int(input("Enter number of days absent: "))
        absence_list.append((name, days))


def absence_list():
    total_days = sum([days in absence_list()])



