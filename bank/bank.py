import sqlite3
import random

def main():
    print('\n{}'.format(sep))
    mode=input("To Login as Adminstrator enter 1\nTo Login as existing bank customer enter 2\nTo register for bank account enter 3\nTo deposit into exist customer account enter 4\nEnter any other input to exit\n\nEnter response:    ")
    if mode=='1': #adminMode
        print(sep)
        adminMode()
        pass
    elif mode=='2': #existing user mode
        print(sep)
        existingUser()
        sayBye()
        pass
    elif mode=='3': #new registration
        print(sep)
        regNewCustomer()
        sayBye()
        pass
    elif mode=='4': #new registration
        print(sep)
        deposit()
        pass
    else: 
        sayBye()

sep="-----------------------------------------------------------------------------"

def isReal(value):
    try: float(value); return True
    except: return False
    
def createDbTable():
    dbFileName=input("Enter database file name: ")
    if dbFileName[-3:].upper()!=".DB":
        dbFileName=dbFileName+".db"
    dbFileNameFile=open("dbFileName.txt",'w')
    dbFileNameFile.write(dbFileName)
    dbFileNameFile.close()
    db=sqlite3.connect(dbFileName)
    name=dbFileName[:-3]
    db.execute('drop table if exists accounts')
    db.execute('create table accounts (fname text,sname text, accNum bigint, password text, balance float)')
    db.commit()
    return dbFileName

def loadDb():
    dbFileName=open("dbFileName.txt")
    dbFileName=dbFileName.read()
    db=sqlite3.connect(dbFileName)
    return db

def addToDatabase(fname,sname,accNum,password, balance):
    try:
        db=loadDb()
        db.execute("insert into accounts (fname,sname,accNum,password,balance) values ('{}','{}',{},'{}',{})".format(fname,sname,accNum,password,balance))
        db.commit()
    except:
        print("Error in connecting to database!!!")
        return False   
    

def selFromDb(accNum):
    db=loadDb()
    account=db.execute('select * from accounts where accNum = {}'.format(accNum))
    return account

def sayBye():
    print(sep)
    print("*********GOODBYE!!!*********".center(len(sep)))
    print(sep)
    exit(0)
    
def genAccNum():
    db=loadDb()
    check=None
    while check == None:
        accNum = random.randrange(8999999999)+1000000000
        accNum = int(accNum)
        check=db.execute('select * from accounts where accNum = {}'.format(accNum))
    return accNum

def regNewCustomer():
    print(sep)
    firstname = input("Enter first name: ")
    surname = input("Enter Surname:")
    print(sep)
    accNum = genAccNum()
    print("Your account number = ", accNum)
    check = False
    while check != True:
        password = input("Enter pasword: ")
        pword = input("Confirm password: ")
        if password != pword:
            print("Password didn't match!!!\nTry again!")
        else: check = True
    balance=0.0
    addToDatabase(firstname,surname,accNum,password,balance)
    print("**********Welcome, Thank you for using our bank!!!************")
    return

def getAccount():
    check = False
    while check == False:
        user=input("Enter account number: ")
        if (len(user) == 10 and user.isdigit()):
            user = int(user)
            if  list(selFromDb(user)) == []:
                print("Invalid account number!!!\n")
                ask = input("press (0) to exit or  (1) for main menu or any key to try again: ")
                if ask == "0":
                    sayBye()
                if ask == "1":
                    main()
            return selFromDb(user)
        else:
            print("Invalid account number!!!\n")
            ask = input("press (0) to exit or  (1) for main menu or any key to try again: ")
            if ask == "0":
                sayBye()
            if ask == "1":
                    main()
    
def updateBalance(accNum, balance):
    '''update account taking acc no and balance'''
    #'update test set i1 = ? where t1 = ?'
    db=loadDb()
    db.execute('update accounts set balance = {} where accNum = {}'.format(balance,accNum))
    db.commit()

def deleteCustomer():
    account = getAccount()
    if account == None :
        print("Account not registered")
        main()
    else: 
        account=tuple(account)
        firstname, surname, accNum, password, balance = account[0]
        print("\nFirst Name = {}\nSurname = {}\nAccount Number = {}\nBalance = {}\n".format(firstname, surname, accNum, balance))
        ask = input("Are you sure you want to delete account?\nEnter YES to confirm or any other entry to exit:     ")
        if ask.upper() == "YES":
            ldb=oadDb()
            db.execute('delete from accounts where accNum = {}'.format(accNum))

def adminMode():
    password=open("password.txt")
    password=password.read()
    askPassword=None
    while password != askPassword:
        askPassword=input("enter admin password: ")
        if password != askPassword:
            ask = input("press (0) to exit or  (1) for main menu or any key to try again: ")
            if ask == "0":
                sayBye()
            if ask == "1":
                main()
    option=input("\nEnter 1 to create database\nEnter 2 to delete from database\nEnter 3 to add to Database\nEnter 4 to exit")
    if option=='1':
        createDbTable()
        main()
    elif option=='2':
        regNewCustomer()
        main()
    elif option=='3':
        deleteCustomer()
        main()
    else: 
        sayBye()
def withdraw(accNum,balance):
    '''withdraw from account using accNum and balance passed from exists customer only to be called by exist customers mode'''
    amount = input("Amount to be withdrawn: ")
    if isReal(amount) and (float(amount) < balance) and (float(amount) > 0):
        balance -= float(amount)
        updateBalance(accNum,balance)
        main()
    else: 
        print("Invalid Amount!!!")
        main()

def cusDeposit(accNum,balance):
    '''deposits to account using accNum and balance passed from exists customer only to be called by exist customers mode'''
    max_deposit = 9000000.00
    amount = input("Amount to be Deposited: ")
    if isReal(amount) and (float(amount) < max_deposit) and (float(amount) >= 0):
        balance += float(amount)
        updateBalance(accNum,balance)
        main()
    else: 
        print("Invalid Amount!!!")
        main()
                        
def existingUser():
    ask=1
    while ask!='0': 
        account=getAccount()
        account=tuple(account)
        if account==None:
            ask=input("press (0) to exit or any key to try again: ")
        else:
            firstname,surname,accNum,password,balance=account[0]
            print('Welcome {} {}'.format(firstname, surname))
            askPassword=False
            chkPass=input("Enter password: ")
            if chkPass!=password:
                print("Incorrect password!!")
                
            else: askPassword=True
            if askPassword==False:
                ask=input("press (0) to exit or any key to try again: ")
            else:
                print('\n',sep)
                mode= input("Enter 1 to check balance\nEnter 2 to withdraw\nEnter 3 to deposit to your account\nEnter 4 to exit\n\nEnter response:    ")
                if mode=='1':
                    print("Your account balance is = #{}".format(balance))
                    main()
                elif mode == '2':
                    withdraw(accNum,balance)
                elif mode=='3':
                    cusDeposit(accNum,balance)
                else:
                    sayBye()
                    
    
def deposit():
    account = getAccount()
    if account == None :
        print("Account not registered")
        main()
    else: 
        account=tuple(account)
        firstname, surname, accNum, password, balance = account[0]
        print("\nFirst Name = {}\nSurname = {}\nAccount Number = {}\n".format(firstname, surname, accNum))
        ask=input("If this is the correct account enter YES if not enter any other input: ")
        if ask.upper() == "YES":
            cusDeposit(accNum,balance)
        else: main()
        

if __name__ == "__main__" :main()
