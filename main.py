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
user_mail = "user@gmail.com"
user_pass = "user1234"
run = None # var for while loops in funcs
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
    global user_mail
    global user_pass
    global login_txt

    # Log In text
    print(login_txt)

    # take input from user
    mail = input("| Mail: ")
    password = getpass.getpass("| Password: ")
    tries = 1 # var for the loop

    if mail == user_mail:
            if password == user_pass:
                print("\n You are logged in.")
    else:
        print("Inviled info, Try again.")
        # check the user input
        while True:
            print("\n_______________\n")
            mail = input("| Mail: ")
            password = getpass.getpass("| Password: ")
            print("\n_______________\n")
        
            if mail == user_mail:
                if password == user_pass:
                    print("\n You are logged in.")
                    break
            elif tries == 3:
                print("You trid to meny times.")
                sleep = time.sleep(5) # wait 5 seconds
                print(sleep)
                tries = 1
                main()
            else:
                print(f"Inviled info, Try again. ({tries})")

            # tries var   
            tries = tries + 1


def singup_form():
    # main sing up text
    print(singup_txt)    
    mail = input("| Enter your gmail: ")

    # check for correct mail adress
    if mail[-10:-1] == '@gmail.co':
        password = input("| Enter a new password: ")
        verify = getpass.getpass("| Vrify your password: ")
        if password != verify:
            print("| Erorr, The passwords do not match.")
            while password != verify:
                print()
                password = input("| Enter a new password: ")
                verify = getpass.getpass("| Vrify your password: ")
                print("____________")
                print("| Erorr, The passwords do not match.")
                print("____________")
    # if the user enter broke email adress     
    else:
        print("|\n" + "| Erorr, try to add '@gmail.com' to your adress \n")
        # ask from user to correct mail adress
        while mail[-10:-1] != '@gmail.co':
            mail = input("| Enter your gmail: ")
        
        password = input("| Enter a new password: ")
        verify = getpass.getpass("| Vrify your password: ")

        if password != verify:
            print("| Erorr, The passwords do not match.")
            while password != verify:
                print("| \n")
                password = input("| Enter a new password: ")
                verify = getpass.getpass("| Vrify your password: ")
                print("____________")
                print("| Erorr, The passwords do not match.")
                print("____________")


    # working with accounts.txt
    a = open(r"C:\Users\almog\Documents\Python\projects\GUI_projects\LogIn_system\accounts.txt", 'a+')
    a.write('\n' + f"---\n{mail} , {verify}")
    a.close()
    print(" Your account has been successfully created!")
    

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