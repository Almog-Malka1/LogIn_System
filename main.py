# ---- modules ----
import getpass
import os
import platform
import time

# ---- local vars ----
main_txt = r"""
  _                 _____          _____           _                 
 | |               |_   _|        / ____|         | |                
 | |     ___   __ _  | |  _ __   | (___  _   _ ___| |_ ___ _ __ ___  
 | |    / _ \ / _` | | | | '_ \   \___ \| | | / __| __/ _ \ '_ ` _ \ 
 | |___| (_) | (_| |_| |_| | | |  ____) | |_| \__ \ ||  __/ | | | | |
 |______\___/ \__, |_____|_| |_| |_____/ \__, |___/\__\___|_| |_| |_|
               __/ |                      __/ |                      
              |___/                      |___/  
                                               made by: @almog._.malka



 What you are looking for?
 1. LogIn  
 2. SingUp
 3. Exit

 Enter your option number.

 """

login_txt = r""" 
  _                    _____           
 | |                  |_   _|        _ 
 | |     ___   __ _     | |  _ __   (_)
 | |    / _ \ / _` |    | | | '_ \     
 | |___| (_) | (_| |   _| |_| | | |  _ 
 |______\___/ \__, |  |_____|_| |_| (_)
               __/ |                   
              |___/  
 """

singup_txt = r"""
   _____ _                _    _           
  / ____(_)              | |  | |        _ 
 | (___  _ _ __   __ _   | |  | |_ __   (_)
  \___ \| | '_ \ / _` |  | |  | | '_ \     
  ____) | | | | | (_| |  | |__| | |_) |  _ 
 |_____/|_|_| |_|\__, |   \____/| .__/  (_)
                  __/ |         | |        
                 |___/          |_|   


 """
#____vars____
option = None
run = None # var for while loops in funcs
location = r"C:\Users\almog\Documents\Python\projects\GUI_projects\LogIn_system\accounts.txt"
#____________

# -----GUI setup-----
def main_screen():
    # global vars
    global option

    # show main screen
    print(main_txt)
    option = input("Enter your number: " )
    option_list = ['1', '2', '3']

    while option not in option_list:
        print("Inviled input, use only in 1, 2, 3.\n")
        option = input("Enter your number: " )

    return option


def login_form():
    # global vars
    global login_txt
    global location

    # Log In text
    print(login_txt)

    # working with the files
    with open(location, 'r') as file:
        user_info = file.read()
        # take input from user
        mail = input("| Enter your gmail:  ")
        password = input("| Enter your password: ")

        # chack if the user info found in the system
        if mail in user_info:
            if password in user_info:
                print("|\n| You are logged in.")
        else:
            run = True
            while run:
                print("| \n* Erorr, The email or password is incorrect \n|")
                mail = input("| Enter your gmail:  ")
                password = input("| Enter your password: ")
                if mail in user_info:
                    if password in user_info:
                        print("|\n| You are logged in.")
                        run = False
        time.sleep(3)
        main()

        file.close()

                

def singup_form():
    # main sing up text
    print(singup_txt)    
    mail = input("| Enter your gmail: ")

    # check for correct mail adress
    if mail[-10:-1] == '@gmail.co':
        password = input("| Enter a new password: ")
        verify = getpass.getpass("| Vrify your password: ")
        if password != verify:
            print("|\n* Erorr, The passwords do not match.")
            while password != verify:
                print()
                password = input("| Enter a new password: ")
                verify = getpass.getpass("| Vrify your password: ")
                print("____________")
                print("|\n* Erorr, The passwords do not match.")
                print("____________")
    # if the user enter broke email adress     
    else:
        print("|\n" + "* Erorr, try to add '@gmail.com' to your adress \n|")
        # ask from user to correct mail adress
        while mail[-10:-1] != '@gmail.co':
            mail = input("| Enter your gmail: ")
        
        password = input("| Enter a new password: ")
        verify = getpass.getpass("| Vrify your password: ")

        if password != verify:
            print("|\n* Erorr, The passwords do not match.")
            while password != verify:
                print("| \n")
                password = input("| Enter a new password: ")
                verify = getpass.getpass("| Vrify your password: ")
                print("____________")
                print("|\n* Erorr, The passwords do not match.")
                print("____________")

    # working with accounts.txt
    a = open(location, 'a+')
    a.write('\n' + f"---\n{mail} , {verify}")
    a.close()
    print("|\n| Your account has been successfully created!")

    print("|\n| You can login right now!")
    login_form()
    

def main():
    # global vars
    global option

    # funcs config
    main_screen()
    if option == '1':
        login_form()
    elif option == '2':
        singup_form()
    elif option == '3':
        exit()


main()


#GUI MENU 

#TAKE INFO

#SAVE INFO FOR NEW USERS IN users.txt

#CHACK IF THE INFO IS CORRECT