def add_user_nums ():
    sum_of_nums = 0
    user_inp = int(input("Enter a Number: "))
    sum_of_nums = int(user_inp)
    while user_inp != 0:
        sum_of_nums = sum_of_nums + user_inp
        user_inp = int(input("Enter a Number: "))

    return sum_of_nums

add_user_nums()


