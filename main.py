import os
import hashlib
import csv

os.system('touch hash.csv')

def in_wallet(pwd):
    try :
            file = list(open('hash.csv'))
            i = 1
    except:
            i = 1
    j = 0
    while i < len(file):
        while j < 64 and i < len(file):
            if pwd[j] == file[i][j]:
                j+=1
                if j == 64 and pwd[63] == file[i][63]:
                    os.system('clear')
                    return 0
            else:
                i+=1
        j = 0 
    return 1

def pwd_check():
    pwd = list(input("Please enter a password : "))
    lenght = len(pwd)
    up = 0
    low = 0
    spe = 0
    num = 0

    i = 0
    while i < lenght:
        if lenght < 8:
            os.system('clear')
            print("This password is too short.")
            return (pwd,0)
        else :
            if pwd[i] >= 'A' and pwd[i] <= 'Z':
                i+=1
                up+=1
            elif pwd[i] >= 'a' and pwd[i] <= 'z':
                i+=1
                low+=1
            elif pwd[i] >= '0' and pwd[i] <= '9':
                i+=1
                num+=1
            elif pwd[i] == '!' or pwd[i] == '@' or pwd[i] == '#' or pwd[i] == '$' or pwd[i] == '%' or pwd[i] == '^' or pwd[i] == '&' or pwd[i] == '*':
                i+=1
                spe+=1
            else :
                os.system('clear')
                print("This password is wrong.")
                return (pwd,0)
    if up >= 1 and low >= 1 and spe >= 1 and num >= 1:
        return(pwd,1)

    else:
        os.system('clear')
        print("This password is too weak.")
        return (pwd,0)

def ft_check():
    os.system('clear')
    res,end = pwd_check()

    while end == 0:
        res,end = pwd_check()

    res = ''.join(res)

    os.system('clear')
    print('This password : "', res , '" is strong !\n')

    reshashed = res.encode('utf-8')
    hex_dig = hashlib.sha256(reshashed).hexdigest()

    into = in_wallet(hex_dig)

    while into == 0:
        print("This password is again already in the wallet.\n")
        try_again = int(input("Do you want to try a new password ?\n\n1) Yes\n2) No\n"))
        os.system('clear')
        if try_again == 1:

            res,end = pwd_check()

            while end == 0:
                res,end = pwd_check()

            res = ''.join(res)

            os.system('clear')
            print('This password : "', res , '" is strong !\n')

            reshashed = res.encode('utf-8')
            hex_dig = hashlib.sha256(reshashed).hexdigest()

            into = in_wallet(hex_dig)
        if try_again == 2:
            os.system('clear')
            exit()

    if into == 1:
        print('Your hashed password : \n"', hex_dig , '"\n is now saved in your wallet.')

        with open('hash.csv', 'a', newline='') as csvfile:
                fieldnames = ['hash']
                thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

                thewriter.writerow({'hash' : hex_dig})

def main():

    menu = int(input("1) Add a new password\n2) Check your password wallet\n"))

    if menu != 1 and menu != 2:
        os.system('clear')
        menu = int(input("1) Add a new password\n2) Check your password wallet\n"))

    if menu == 1:
        ft_check()
        
    if menu == 2 :
        os.system('clear')
        file = list(open('hash.csv'))
        i = 0
        lenght = len(file)
        print("Your hashed wallet :\n")
        while i < lenght:
                print(file[i])
                i+=1
        print("--------------------------\n")
        double_check = int(input("Do you want to add a password ?\n1)Yes\n2)No\n"))
        if double_check == 1:
            os.system('clear')
            ft_check()
        else :
            exit

main()