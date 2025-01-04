def operations_with_string():    #function for manipulating strings
    sentence = "Interactive games are fun"

    # loop for different operations that uses chooses from
    while True:
        print("Please select operation:")
        print("1 - for slicing")
        print("2 - for uppercase")
        print("3 - for replace")
        print('4 - for previous menu')
        choice = input()

    # here we take part of the sentence
        if choice == '1':
            print(f"sentence = {sentence}")
            print("Type of operation:slicing")
            print(f"Result:{sentence[-3:]}\n")

    # here we make all chars uppercase
        elif choice == '2':
            print(f"sentence = {sentence}")
            print("Type of operation:uppercase")
            print(f"Result:{sentence.upper()}\n")

    # here we replace part of the sentence
        elif choice == '3':
            print(f"sentence = {sentence}")
            print("Type of operation:replace")
            print(f"Result:{sentence.replace("fun","interesting")}\n")

    # returning to base menu
        elif choice == '4':
            return base_menu()

    # here we manage wrong selections
        else:
            print("Error.Please select again:\n")


def operations_with_numbers():    #function for operations with numbers

    #here we create loop for multiple use of operations
    while True:
        print("\nPlease select operation:")
        print("1 - for addition")
        print("2 - for subtraction")
        print("3 - for multiplication")
        print("4 - for division")
        print("5 - for raising to a power")
        print('6 - for previous menu')
        choice = input()
        if choice == '1':     #here we prompt user to choose numbers and then we do operation "addition"
            number_one = float(input("\nChoose a number:"))
            number_two = float(input("\nChoose another number:"))
            print(f"Operation:addition\nResult:{number_two + number_one}")
        elif choice == '2':       #here we prompt user to choose numbers and then we do operation "subtraction"
            number_one = float(input("\nChoose a number:"))
            number_two = float(input("\nChoose another number:"))
            print(f"Operation:subtraction\nResult:{number_one - number_two}")
        elif choice == '3':       #here we prompt user to choose numbers and then we do operation "multiplication"
            number_one = float(input("\nChoose a number:"))
            number_two = float(input("\nChoose another number:"))
            print(f"Operation:multiplication\nResult:{number_one * number_two}")
        elif choice == '4':       #here we prompt user to choose numbers and then we do operation "division"
            number_one = float(input("\nChoose a number:"))
            number_two = float(input("\nChoose another number:"))
            if number_two != 0:     #here we handle not possible division by 0
                print(f"Operation:division\nResult:{number_one / number_two}")
            else:
                print(f"Operation:division\nResult:Error.Cannot divide by 0")
        elif choice == '5':       #here we prompt user to choose numbers,and then we do operation "raising to a power"
            number_one = float(input("\nChoose a number:"))
            number_two = float(input("\nChoose another number:"))

            # here we handle edge case not multiplying by positive integer
            if number_two.is_integer() and number_two > 0:
                print(f"Operation:raising to a power\nResult:{number_one ** number_two}")
            else:
                print("Operation:raising to a power\nResult:Error.You can raise to a power only positive integers")
        elif choice == '6':       #return to previous menu
            return base_menu()
        else:
            print("Error.Please select again:\n")


def boolean_operations():    #function for exploring different boolean operations
    is_false = False          #declaring boolean that we use later for examples
    is_true = True          #declaring boolean that we use later for examples
    print("Example of boolean variables:\nis_false = False,is_true = True")
    print("Please select:")
    while True:
        print("1 - for logical operator")
        print("2 - for comparison operators")
        print("3 - for previous menu")
        choice = input()
        if choice == '1':
            return boolean_logical_operators()   #here we call function for exploring different logical operators
        elif choice == '2':
            return boolean_comparison_operators()   ##here we call function for exploring different comparison operators
        elif choice == '3':       #return to base menu
            return base_menu()
        else:       #if user chooses wrong number
            print("Wrong choice.Please select again:\n")


def boolean_logical_operators():    #function for exploring different logical operators
    print("\nPlease select:")
    while True:
        print("1 - for logical operator AND")
        print("2 - for logical operator OR")
        print("3 - for logical operator NOT")
        print('4 - for previous menu')
        choice = input()   #here we prompt user to choose logical operator
        if choice == '1':     #result of logical operator "AND"
            print("is_false AND is_true\nResult:False\n")
        elif choice == '2':       #result of logical operator "OR"
            print('is_false OR is_true\nResult:True\n')
        elif choice == '3' :       #result of logical operator "NOT"
            print('NOT is_true\nResult:False\nNOT is_false\nResult:True\n')
        elif choice == '4':       #return to previous menu
            return boolean_operations()
        else:       #if user chooses wrong number
            print('Wrong choice.Please choose again:\n')


def boolean_comparison_operators():     #function for exploring different boolean comparison operators
    print('\nPlease select:')
    while True:
        print('1 - for comparison operator >')
        print('2 - for comparison operator <')
        print('3 - for comparison operator ==')
        print('4 - for previous menu')
        choice = input()
        if choice == '1':     #print example of using comparison operator ">"
            print("2 > 1\n")
        elif choice == '2':       #print example of using comparison operator "<"
            print("1 < 2\n")
        elif choice == '3':       #print example of using comparison operator "=="
            print("1 == 1\n")
            print("2 == 2\n")
        elif choice == '4':       #return to previous menu
            return boolean_operations()
        else:       #if user chooses wrong number
            print('Wrong choice.Please select again:\n')


def additional_data_types():    #functions for choosing between list,tuple and dictionary data types
    print('\nPlease select data type:')
    while True:
        print('1 - for lists')
        print('2 - for dictionaries')
        print('3 - for tuples')
        print('4 - for previous menu')
        choice = input()

        #here we handle different user choices
        if choice == '1':     #list data type
            return operations_with_list()
        elif choice == '2':       #dictionary data type
            return operations_with_dictionary()
        elif choice == '3':       #tuple data type
            return operations_with_tuple()
        elif choice == '4':       #returning to base menu
            return base_menu()
        else:       #when user select wrong number
            print('Wrong choice.Please select again:\n')


def operations_with_list():     #operations with list data types
    users_list = [ "keyboard", 3, 5.14, True]
    print(f'\nThis is our list:{users_list}')
    print('\nPlease select operation:')
    while True:
        print('1 - for append')
        print('2 - for access and print an element')
        print('3 - for length of list')
        print('4 - for previous menu')
        choice = input()

        if choice == '1':     #append an element to list
            print(f'Old list:{users_list}')
            users_list.append('new_item')
            print(f'New lost:{users_list}\n')
        elif choice == '2':    #print an element of list
            print(f'{users_list[0]}\n')
        elif choice == '3':   #print length of list
            print(f'Length of list is:{len(users_list)}\n')
        elif choice == '4':   #return to previous menu
            return additional_data_types()
        else:       #if user select invalid number
            print('Wrong choice.Please select again:\n')


def operations_with_dictionary():       #operations with dictionary data type
    user_dictionary = {'keyboard':'logy','count_pc':2,'country':'Bulgaria'}
    print(f'\nThis is our dictionary:{user_dictionary}')
    print('Please select operation:')
    while True:
        print('1 - for print a value')
        print('2 - for add a pair key:value')
        print('3 - for length of dictionary')
        print('4 - for previous menu')
        choice = input()

        if choice == '1':     #printing a value
            print(f'{user_dictionary['keyboard']}\n')
        elif choice == '2':    #adding new pair to dictionary
            user_dictionary['city'] = 'Sofia'
            print(f'New dictionary:{user_dictionary}\n')
        elif choice == '3':       #printing length of dictionary
            print(f'Length of dictionary:{len(user_dictionary)}\n')
        elif choice == '4':       #return to previous menu
            return additional_data_types()
        else:       #if user select invalid number
            print('Wrong choice.Please select again:\n')

def operations_with_tuple():        #operations with tuple data type
    user_tuple = ('keyboard', 2, 'Bulgaria')
    print(f'\nThis is our tuple:{user_tuple}')
    print('Please select operation:')
    while True:
        print('1 - for print a value')
        print('2 - for append')
        print('3 - for length of dictionary')
        print('4 - for previous menu')
        choice = input()

        if choice == '1':         #printing a value of tuple
            print(f'{user_tuple[2]}\n')
        elif choice == '2':      #try to modify tuple
            print('Tuples are immutable and cannot be modified\n')
        elif choice == '3':     #print length of tuple
            print(f'Length of tuple:{len(user_tuple)}\n')
        elif choice == '4':       #return to previous menu
            return additional_data_types()
        else:       #if user select invalid number
            print('Wrong choice.Please select again:\n')

def base_menu():        #initial user menu
    print('Please select:')
    while True:
        print('1 - for operations with strings')
        print('2 - for operations with numbers')
        print('3 - for operations with boolean operators')
        print('4 - for operations with additional data types')
        print('5 - for exit')
        choice = input()

        if choice == "1":     #sends user to operations with strings
            return operations_with_string()
        elif choice == "2":       #sends user to operations with numbers
            return operations_with_numbers()
        elif choice == '3':       #sends user to operations with boolean operators
            return boolean_operations()
        elif choice == '4':       #sends user to operations with additional data types
            return additional_data_types()
        elif choice == '5':       #to end program
            print("See you again")
            break
        else:
            print('Wrong choice.Please select again:\n')


print("Welcome to interactive data type operation system.\n")
base_menu()