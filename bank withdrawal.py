from sys import exit

def getAccNum():
    check=False
    while check==False:
        user=input("Enter account number: ")
        if (len(user)==10 and user.isdigit()):
            check==True
            return user
        else:
            print("Invalid account number!!!\n")
            ask=input("==================================================\nDo you want to try again.\n enter(1) for yes (0) for no: ")
            if ask=="0":
                print ("\n==================================================\nGood bye!!!")
                exit(0)
            elif ask=="1":
                    check==False
            else:
                    print("\n==================================================\nInvalid input!!!\n\nGood bye!!!")
                     exit(0)

def withdraw(curr_bal):
    amount=int(input("\n==================================================\nEnter amount to be withdrawn: "))
    if amount >curr_bal:
        print("\n==================================================\nInsufficient balance!!!\n")
        ask=input("==================================================\nDo you want to try again.\n enter(1) for yes (0) for no: ")
        if ask=='1':
            new_bal=withdraw(curr_bal)
        elif ask=='0':
            ("\n==================================================\n\nGood bye!!!")
        else:
            print("\n==================================================\nInvalid input!!!\n\nGood bye!!!")
            exit(0)
    else :
        new_bal=curr_bal-amount
        print("Successful Withdrawal!!!\n")
        print ("==================================================\nAmount withdrawn: ", amount)
    return new_bal
    
def deposit(curr_bal):
    max_bal=10000000
    amount=int(input("\n==================================================\nEnter amount to be deposited: "))
    if (amount+curr_bal) > max_bal:
        print("Maximum Balance will be exceed if deposit is made!!!")
        ask=input("==================================================\nDo you want to try again.\n enter(1) for yes (0) for no: ")
        if ask=='1':
            new_bal=deposit(curr_bal)
        elif ask=='0':
            ("\n==================================================\n\nGood bye!!!")
            exit(0)
        else:
            print("\n==================================================\nInvalid input!!!\n\nGood bye!!!")
            exit(0)
    else:
        new_bal=curr_bal+amount
        print("Successful Deposit!!!\n")
        print ("==================================================\nAmount Deposited: ", amount)
    return new_bal

def  main():
    curr_bal=1906*4
    new_bal=curr_bal
    getAccNum()
    print ("Current balance: ", curr_bal, end="\n\n")
    request=input("For withdrawal enter (1)\ndeposit enter (2): " )
    if request=='1':
        new_bal=withdraw(curr_bal)
    elif request=='2':
        new_bal=deposit(curr_bal)
    else:
        print("Invalid input!!!")
        ask=input("==================================================\nDo you want to try again.\n enter(1) for yes (0) for no: ")
        if ask=='1':
            main()
        elif ask=='0':
            ("\n==================================================\n\nGood bye!!!")
            exit(0)
        else:
            print("\nInavlid Input!!!\n")
    print ("New balance: ", new_bal)
    print("\n==================================================\n\nThank you for bank with us !!!\nGood Bye!!!")

if __name__=="__main__":main()
