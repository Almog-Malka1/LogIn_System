# ---- modules ----
import getpass
import os
import platform


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

option = None

# -----GUI setup-----
def main_screen():
    #global vars
    global option

    #show main screen
    print(main_txt)
    option = input("Enter your number: " )
    option_list = ['1', '2', '3']

    while option not in option_list:
        print("Inviled input, use only in 1, 2, 3.\n")
        option = input("Enter your number: " )

    return option

def login_form():
    print("log in.")

def singup_form():
    print("sing up.")



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