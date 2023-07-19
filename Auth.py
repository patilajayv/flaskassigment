import re

def check_password_strength():
    print("\033[34mPassword set Policy: \n1)The password should be at least 8 characters long\n2)Should have both uppercase and lowercase letters.\n3)Should have at least one digit (0-9).\n4)Should have at least one special character (e.g., !, @, #, $, %).\033[0m")
    A = input("\033[35mEnter New Password : \033[0m")
    lenghtCheck = False
    upperCase = False
    lowerCase = False
    numbers = False
    charCheck= False
    if len(A)>=8:
        lenghtCheck = True
    if re.search(r'[a-z]',A):
         lowerCase=True
    if re.search(r'[A-Z]',A):
         upperCase = True
    if re.search(r'[!@#$%]',A):
         charCheck = True
    if re.search(r'\d',A):
         numbers = True
    if lenghtCheck and upperCase and lowerCase and numbers and charCheck :
            print("\033[32m!!!Password set !!!!\033[0m")
    else:
         print("\033[31mPlease refer policy to set password,Please try again\033[0m")
         check_password_strength()
check_password_strength()