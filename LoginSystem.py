import requests


def have_account():
    return input("Do you have an account: ").lower().startswith("y")


def signup():
    new_username = input("Please enter your new username: ")
    new_password = input("Please enter your new password: ")
    while True:
        with open("username.txt", "a") as new_u:
            new_u.write(new_username)
            new_u.write("\n")
        with open("password.txt", "a") as new_p:
            new_p.write(new_password)
            new_p.write("\n")
        with open("username.txt", "r") as new_uu:
            u = new_uu.read()
        with open("password.txt", "r") as new_pp:
            p = new_pp.read()
        if new_username not in u or new_password not in p:
            break
        else:
            print("Username or password already taken")
            continue


"""
def check():
    with open('username.txt','r') as check_u:
        check_username = check_u.read()
    with open('password.txt','r') as check_p:
        check_password = check_p.read()

    if username in
"""


def login():
    while True:
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")

        with open("username.txt", "r") as accounts_u:
            accounts_username = accounts_u.read()
        with open("password.txt", "r") as accounts_p:
            accounts_password = accounts_p.read()

        if username not in accounts_username:
            print("Username or Password is incorrect. Please try again")
        elif username in accounts_username and password not in accounts_password:
            print("Username or Password is incorrect. Please try again")
        elif username in accounts_username and password in accounts_password:
            print("Welcome")
            break
        else:
            print("this is not your account")


while True:
    if have_account():
        print("Login Please")
        print()
        login()
        break
    else:
        print("Please make an account")
        print()
        signup()
        print()
        print("Please login in with your new credentials")
        print()
        login()
        break