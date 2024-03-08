# Program: The six games in the task 3 ( Grade calculator , Armstrong , Leibniz pi , Cesar encryption , List comparing ,
# Factors ) Games
# Authors: Ahmed Atef and solved game 1 & 2
#          Kirollos Adel and solved game 3 & 4
#          Mina Maher and solved game 5 & 6
# Version: 3.0
# Date: 2 / 25 / 2024

import sys

""" Developed by Ahmed Atef  """


def main_menu():
    print("***please choose an option of the following***")
    operation = int(
        input(" 1) problem 1 [ Grade calculator ] \n 2) problem 2 [ Armstrong_number validator ] \n 3) problem 3 "
              "[ Pi Approximation ] " "\n 4) problem 4 [ Cesar Encryption ] \n 5) problem 5 [ List comparing ] \n "
              "6) problem 6 [ Factors ] \n " "7) exit program \n >> "))

    if operation == 1:
        grad_calc()
    elif operation == 2:
        Armstrong_number()
    elif operation == 3:
        pi_approximation()
    elif operation == 4:
        cesar_encryption()
    elif operation == 5:
        list_comparison()
    elif operation == 6:
        prob_6()
    elif operation == 7:
        sys.exit()


# Grade calculator


def grad_calc():
    print("Wellcome to the Grade Calculator\n")
    # grade input string validation
    try:
        Grade = int(input("please Enter a grade: "))
    except:
        # calling the main function to go back to the input menu
        print("Enter a valid integer")
        grad_calc()
    # comparing the inputted number with multiple grade ranges and outputting the grade accordingly
    if Grade >= 97 and Grade <= 100:
        print("Your grade is A+")
    if Grade >= 93 and Grade < 97:
        print("Your grade is A")
    if Grade >= 90 and Grade < 93:
        print("Your grade is A-")
    if Grade >= 87 and Grade < 90:
        print("Your grade is B+")
    if Grade >= 83 and Grade < 87:
        print("Your grade is B")
    if Grade >= 80 and Grade < 83:
        print("Your grade is B-")
    if Grade >= 77 and Grade < 80:
        print("Your grade is C+")
    if Grade >= 73 and Grade < 77:
        print("Your grade is C")
    if Grade >= 70 and Grade < 73:
        print("Your grade is C-")
    if Grade >= 67 and Grade < 70:
        print("Your grade is D+")
    if Grade >= 63 and Grade < 67:
        print("Your grade is D")

    if Grade >= 60 and Grade < 63:
        print("Your grade is D-")

    if Grade < 60 and Grade >= 0:
        print("Your grade is F")
    # validating for invalid integer inputs
    if Grade < 0 or Grade > 100:
        print("Enter a valid positive grade")
        grad_calc()
    main_menu()


# ================================================= #

# Armstrong_number validator
# main function

def Armstrong_number():
    print("Wellcome to Armstrong numbers validator\n")
    # take input from the user as a string
    armstrong_number = str(input("Please enter a postive number: "))
    # initialize a variable n and set it equal to the length of the integer
    n = len(armstrong_number)
    # initialize sum = 0
    sum = 0
    # validate this number for being positive
    if int(armstrong_number) > 0:
        # in range from 0 to n add to sum the digit of the armstrong number rased to the power of the length n
        for i in range(0, n):
            sum += (int(armstrong_number[i]) ** n)
    else:
        # calling the main function if input is negative to reset the function
        Armstrong_number()
        # validating if the number is armstrong or not
    if sum == int(armstrong_number):
        print("This is an armstrong number")
    else:
        print("This is not armstrong number")


# calling the main function
# Armstrong_number()

# ================================================= #

""" Developed by Kirollos Adel  """


# Pi Approximation
# Calc function
def pi_approximation():
    def calc_pi(num):
        res = 0
        for i in range(1, num + 1):
            # Check if the number in term even or not to multiplicative it by - 1
            if i % 2 == 0:
                res -= 1 / (2 * i - 1)
            else:
                res += 1 / (2 * i - 1)
        return res

    # Main function
    def main():
        print("Welcome to Pi approximation calculater\n")
        # Validation while
        while True:
            user_input = input("Please, enter the number of terms: ")
            # Check if a user inserts a number or not
            if user_input.isalpha() or len(user_input) == 0 or user_input.isspace():
                print("Error! please insert a valid number of terms")
                continue
            break
        # Casting the user_input to integer
        term = int(user_input)
        print("Approximation of π: ", calc_pi(term) * 4)
        main_menu()

    # Call back the main function
    main()


# ================================================= #

# Cesar Encryption
# Function that converts the characters to the next char by ascii code
def cesar_encryption():
    def cesar_enc(text):
        res = ""
        # Convert the main text to lowercase
        text = text.lower()
        for char in text:
            if char.islower():
                # get the ASCII code and shift it by 1 and return the new text
                res += chr((ord(char) + 1 - 97) % 26 + 97)
            else:
                res += char
        return res

    # Main function
    def main4():
        print("Welcome to Cesar Encryption")
        # Validation while loop
        while True:
            text = input("Please, enter your text to encrypt: ")
            # Check if the user inserts text or not
            if text.isdigit() or text.isspace() or len(text) == 0:
                print("Please enter a valid string")
                continue
            break
        #  Print the final result by shifting the user's text
        print("Your text entered is: ", cesar_enc(text))
        main_menu()

    # call back the mian function
    main4()


# ================================================= #

""" Developed by Mina Maher  """


# List comparing
def list_comparison():
    global len_of_list
    list1 = []  # place holds elements of first list
    list2 = []  # place holds elements of second list
    n1 = 0  # variable for first loop
    n2 = 0  # variable for second loop
    len_of_list = 0  # to store the length of both lists.

    def menu5():  # define let user entre the len of list
        print("Welcome to List Comparison\n")
        global len_of_list
        len_of_list = int(input("Enter the length of the list: "))
        if len_of_list < 0:
            print("Please enter a valid positive integer ")
            return menu5()

    print("welcome to the game")
    menu5()
    print("please choose your first  lists")
    while n1 < len_of_list:
        num1 = int(input("Enter the number: "))
        list1.append(num1)
        n1 = n1 + 1
    print(list1)
    print("please choose your second list ")
    while n2 < len_of_list:
        num2 = int(input("Enter a number: "))
        list2.append(num2)
        n2 = n2 + 1
    print(list2)

    def check_elements():  ##function to check if the elements are equal in lists
        return sorted(list1) == sorted(list2)

    if check_elements():  # if statment to check the condition
        print("true")
    else:
        print("false")
    main_menu()


# ================================================= #

# Factors

''''
In menu() we make user enter a number and check if this number is positive or not
then enter a for loop to print the factors of the number '''


def prob_6():
    global number
    print("wlecome to the game ")
    number = 0

    def menu6():
        print("Welcome to the factor calculator\n")
        global number
        number = int(input("choose a positive intger"))
        if number <= 0:
            print("entre a valid number please")
            return menu6()
        print("the factors of number are: ")
        for i in range(1, number + 1):  # condition for factors
            if number % i == 0:
                print(i)
        main_menu()

    menu6()


main_menu()
