def square_user_nums ():
    # Initialize loop variable
    user_inp = input("Enter the next number (negative to quit):")
    user_num = int(user_inp)
    while user_num >= 0:
        print(user_num, "squared is", user_num ** 2)
        user_inp = input("Enter the next number (negative to quit):")
        user_num = int(user_inp)
square_user_nums()

# user_num is not defined if the first two lines are commented out. If the second set of lines are commented out,
# values continue on repeating infinitely because there is no break in the while loop.