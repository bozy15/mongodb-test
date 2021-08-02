def welcome_function():
    """
    This function is the welcome function, it is called
    first in the main_program_call function. The function
    prints a welcome message and instructions to the user.
    """
    print("WELCOME TO LEARNPULSE")
    print(
        "Through this program you can submit and search for \n"
        "staff training information"
    )
    print("\n")
    print("What would you like to do?")
    print("Please enter one of the following options to progress:")
    print('- Enter "input" to add trainee data to the database')
    print('- Enter "search" to search for trainee data')
    while True:
        user_branch_choice = input("Please input your command: ")
        if user_branch_choice == "input":
            return user_branch_choice
        elif user_branch_choice == "search":
            return user_branch_choice
        else:
            print("Sorry, that command was invalid please try again")
            print("\n")
            


# def program_branch():
def main_program_call():
    """
    This function is the main function in the program through which
    all other functions are called.
    """
    branching_variable = welcome_function()
    print(branching_variable)


main_program_call()
