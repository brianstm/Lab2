def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
    num = input("Enter the number: ")
    li = num.split(", ")

    floats = []
    for element in li:
        floats.append(float(element))
    return floats


def calc_average(l):
    sum = 0
    for x in l:
        sum += x

    avg = sum / len(l)
    print("The average is: ", avg)


def calc_min_max(l):
    largest = l[0]
    smallest = l[0]

    for number in l:
        if number > largest:
            largest = number

    for number2 in l:
        if number2 < smallest:
            smallest = number2

    print("The largest is: ", largest)
    print("The smallest is: ", smallest)


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    calc_average(num_list)
    calc_min_max(num_list)


if __name__ == "__main__":
    main()
