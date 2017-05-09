class Customer():
    '''creates a customer object and take 5 optinal arguments
       firstname,surname,accNum,email,age
    '''
    _sep = '------------------------------------------------------------------------------'
    accFile = "accNum.txt"
    balFile = "balance.txt"
    fnameFile = "fname.txt"
    snameFile =  "sname.txt"
    emailFile ="email.txt"
    ageFile = "age.txt"
    pwordFile = "password.txt"
    
    def __init__(self,firstname = None,surname= None, accNum = None, email = None, age = None, password = None):
        self._firstname = firstname
        self._surname = surname
        self._accNum = accNum
        self._email = email
        self._age = age
        self._password = password
        self._balance = 0.0
        
    def isReal(self, num):
        try: 
            float(num)
            return True
        except: return False

    def genAccNum(self):
        """generates unique accNum by checking database"""
        import random
        accNums=self.fileSplit("accNum.txt")
        invalid=True
        while invalid:
            accNum = random.randint(1000000000,9999999999)
            if accNum not in accNums: invalid = False
        return accNum
        
    def regAccount(self):
        if self._accNum == None:
            print(self._sep)
            self._firstname = input("Enter first name: ")
            self._surname = input("Enter surname: ")
            self._email = input("Enter email: ")
            print(self._sep)
            self._accNum = self.genAccNum()
            print("Account Number: {}".format(self._accNum))
            self._balance = 0.0
            invalid = True
            while invalid:
                print(self._sep)
                self._age = input("Enter Age: ")
                if self._age.isdigit() and int(self._age) >= 18:
                    break
                else: 
                    print("Invalid Age!!!")
            while invalid:
                print(self._sep)
                self._password = input("Enter password: ")
                test_password = input("Confirm Password: ")
                if self._password == test_password:
                    break
                else: 
                    print("Password does not match!!!\nTry again")
        self.updateAcc()
    
    def fileSplit(self,x):
        file = open(x)
        file = file.read()
        file = file.split("\n")
        return file
    
    def updateAcc(self):
        '''Add update current object to file'''
        accNums = self.fileSplit(self.accFile)
        if str(self._accNum) in accNums:
            ID = accNums.index(str(self._accNum))
            firstnames = self.fileSplit(self.fnameFile)
            surnames = self.fileSplit(self.snameFile)
            emails = self.fileSplit(self.emailFile)
            ages =  self.fileSplit(self.ageFile)
            balances = self.fileSplit(self.balFile)
            passwords = self.fileSplit(self.pwordFile)
            
            firstnames[ID] = self._firstname
            surnames[ID] = self._surname
            emails[ID] = self._email
            balances[ID] = self._balance
            ages[ID] = self._age
            passwords[ID] = self._password
            
            firstnameFile = open(self.fnameFile,'w')
            surnameFile = open(self.snameFile,'w')
            emailFile = open(self.emailFile,'w')
            accNumFile = open(self.accFile,'w')
            ageFile =  open(self.ageFile,'w')
            balanceFile = open(self.balFile,'w')
            pwordFile = open(self.pwordFile,'w')
            
            for x in range(len(accNums)):
                firstnameFile.write(str(firstnames[x])+"\n")
                surnameFile.write(str(surnames[x])+"\n")
                emailFile.write(str(emails[x])+"\n")
                accNumFile.write(str(accNums[x])+"\n")
                ageFile.write(str(ages[x])+"\n")
                balanceFile.write(str(balances[x])+"\n")
                pwordFile.write(str(passwords[x])+"\n")
                
            
        else:
            firstnameFile = open(self.fnameFile,'a')
            surnameFile = open(self.snameFile,'a')
            emailFile = open(self.emailFile,'a')
            accNumFile = open(self.accFile,'a')
            ageFile =  open(self.ageFile,'a')
            balanceFile = open(self.balFile,'a')
            pwordFile = open(self.pwordFile,'a')
        
            firstnameFile.write(str(self._firstname)+'\n')
            surnameFile.write(str(self._surname)+'\n')
            emailFile.write(str(self._email)+'\n')
            accNumFile.write(str(self._accNum)+'\n')
            ageFile.write(str(self._age)+'\n')
            balanceFile.write(str(self._balance)+'\n')
            pwordFile.write(str(self._password)+"\n")
            return
        

    def getAmount(self):
        invalid = True
        while invalid:
            amount = input("Enter Amount: ")
            if self.isReal(amount): break
            else:
                ask = input("Please enter a number!!!\nEnter 0 to exit or any key to retry: ")
                if ask == '0': return False
        return float(amount)
    
    def loadUser(self):
        '''load user in put via Account number and password'''
        accNums =  self.fileSplit(self.accFile)
        invalid = True
        while invalid:
            accNum = input("Enter Account Number: ")
            if accNum in accNums:
                ID = accNums.index(accNum)
                break
            else:
                ask = input("Account does not exist!!!\nEnter 0 to exit or any key to retry: ")
                if ask == '0': return False 
        passwords = self.fileSplit(self.pwordFile)
        while invalid:   
            print(self._sep)
            test_password = input("Enter password: ")
            if test_password == passwords[ID]:
                break
            else: 
                ask = input("Incorrect password!!!\nEnter 0 to exit or any key to retry: ")
                if ask == '0': return False
        firstnames = self.fileSplit(self.fnameFile)
        surnames = self.fileSplit(self.snameFile)
        balances = self.fileSplit(self.balFile)
        ages = self.fileSplit(self.ageFile)
        emails = self.fileSplit(self.emailFile)
        
        self._accNum = accNums[ID]
        self._firstname = firstnames[ID]
        self._surname = surnames[ID]
        self._balance = float(balances[ID])
        self._age = ages[ID]
        self._email = emails[ID]
        self._password = passwords[ID]
        
    def authenticate(self):
        accNums = self.fileSplit(self.accFile)
        passwords = self.fileSplit(self.pwordFile)
        if (self._accNum in accNums) and  (self._password == passwords[accNums.index(self._accNum)]):
            ID = accNums.index(self._accNum)
            return ID
        else: 
            print("Invalid login credentials!!!")
            return False
    def updataBal(self, ID):
        #auth = self.authenticate()
        #if auth != False:
        balances = self.fileSplit(self.balFile)
        balances[ID] = self._balance
        balancesWrite = open(self.balFile,'w')
        for  x in range(len(balances)):
            balancesWrite.write(str(balances[x])+"\n")
                
    def withdraw(self,Type = None):
        '''withdraw using and exist Account requires a log in user i.e loadUser function should have been called'''
        auth =  self.authenticate()
        if Type == None:
            print(self._sep)
            print("************ WITHDRAW ************".center(len(self._sep)))
        print(self._sep)
        if auth != False:
            amount = self.getAmount()
            if amount == False:
                return False
            elif amount > self._balance:
                print("Insufficent Fund!!!")
                return False
            else:
                self._balance -= amount
                self.updataBal(auth)
                if Type == None:
                    print("Your new balance = {}".format(self._balance))
                return amount
        else: return False
                
    def deposit(self, amount = None):
        auth =  self.authenticate()
        print(self._sep)
        print("************ DEPOSIT ************".center(len(self._sep)))
        print(self._sep)
        if auth != False:
            if amount == None:
                amount = getAmount()
            if amount == False:
                return
            else: 
                self._balance += amount
                self.updataBal(ID)
                print("Your new balance = {}".format(self._balance))
                return
    
    def extDeposit(self, accNum = None, amount = None):
        if accNum == None:
            accNum = input("Enter Account Number: ")
        accNums = self.fileSplit(self.accFile)
        if accNum in accNums: 
            ID = accNums.index(accNum)
            firstnames = self.fileSplit(self.fnameFile)
            surnames = self.fileSplit(self.snameFile)
            print("Account Number {}\nFirst Name: {}\nSurname {}".format(accNums[ID],firstnames[ID],surnames[ID]))
            ask = input("To enter any number to exit enter (0): ")
            if ask == '0':
                print("Process cancelled")
                return False
            else: 
                balances = self.fileSplit(self.balFile)
                self._balance = float(balances[ID])
                if amount == None:
                    amount = self.getAmount()
                self._balance += amount
                self.updataBal(ID)
                return True 
        else: 
            print("User does not exist")
            return False
        
    def transfer(self):
        auth = self.authenticate()
        accNums =  self.fileSplit(self.accFile)
        fund = self.withdraw("transfer")
        if fund != False:
            recAccNum =input("Enter Receiver Account Number: ")
            if recAccNum in accNums:
                recObj = Customer(recAccNum)
                status = recObj.extDeposit(recAccNum, fund)
                if status == False: 
                    self.deposit(fund) #refund
                    print('Transfer Failed!!!')
                else:
                    print('Successful Transfer for #{} to {}'.format(fund,recAccNum)
                    return
    
    def updateInfo():
        pass
    
    def closeAcc():
        pass
    
            
emma = Customer()
emma.loadUser()
emma.transfer()
#emma.withdraw()
#emma=Customer()
##emma.regAccount()
 
