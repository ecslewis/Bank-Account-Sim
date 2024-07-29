menu= """Welcome to the Bank Accounts Management App:
1- Print All Accounts (tabular format) (prints Code, Name, Bank, Type, Balance, last_access)
2- Create an account (Enter code, client name, bank name, account type and balance)
3- Create/update the password for an account (Enter account code)
4- Withdraw an amount from an account. (account code & amount)
5- Deposit an amount to an account (Enter account code & amount)
6- Transfer an amount between accounts (Enter from and to account codes and amount
7- Get balance of a given account (Enter account code)
8- Display the log file.
9- Exit
"""
import datetime
class BankAccount:
    Count=0
    def __init__(self,CODE,NAME,BANK,TYPE,BALANCE=0):
        self.Code = CODE
        self.Name = NAME
        self.Bank = BANK
        self.Type = TYPE
        self.Balance = BALANCE
        self.password =""
        self.last_access = datetime.datetime.now()
        BankAccount.Count += 1
    def __del(self):
        Student.Count -=1
        print("Deleting student instance!")
    def __repr__(self):
        #returns the string to print an object.
        #implicitely called when print(obj)
        fmt='{:6d} {:30s} {:10s} {:10s} {:8.2f} {}'
        x= fmt.format(self.Code,self.Name,self.Bank,self.Type,self.Balance,
                      self.last_access)
        return(x)
    def update_status(self,new_status):
        self.status = new_status
    def Add_interest(self, rate):
        rate=float(rate)
        if not 0<rate:
            print("wrong rate")
        elif not rate<=6.0:
            print("too high rate")
        else:
            self.Balance= self.Balance*(1+rate)
        self.last_access = datetime.datetime.now()
    def create_pwd(self):
        p=False #from lab6
        while not p:
            t= input("Enter your password:")
            if t[-1] =="#":
                if t[-5:-2].isdigit():
                    if 8 <= len(t) <= 15:
                        if (t[0].isupper()==True):
                            if t[:-1].isalnum()==True:
                                if t[0:-1].isupper()== False:
                                    print("Password Accepted")
                                    self.password=t
                                    p=True
                                else:
                                    print("Invalid, you must have at least 1 small letter")
                                    continue
                            else:
                                print("Invalid, please enter only digits or alphabetic")
                                continue
                        else:
                            print("Invalid, please start with a capital letter")
                            continue
                    else:
                        print("Please enter 8-15 digits")
                        continue
                else:
                    print("Invalid, please end with 4 numbers before #")
                    continue
            else:
                print("Invalid, no #")
                continue
        self.last_access = datetime.datetime.now()
        return t
    def deposit(self, amount):
        self.Balance+=amount
        print(amount,'$ successfully deposited into account', self.Code)
        self.last_access = datetime.datetime.now()
    def withdraw(self,amount):
        pwd=input('enter password to access')
        if pwd==self.password:
            if amount>self.Balance:
                print("No money available to withdraw.")
            else:
                self.Balance-=amount
                print(amount,"$ successfully withdrew")
        else:
            print("Wrong password.")
        self.last_access = datetime.datetime.now()
    def get_balance(self):
        print(self.Code,'has',self.Balance,'$')
        self.last_access = datetime.datetime.now()
    def transfer(self, other, amount):
        pwd=input('enter password to access')
        if pwd==self.password:
            if amount>self.Balance:
                print("Insufficient funds")
            else:
                self.Balance-=amount
                Accounts[other].Balance+=amount
                print(amount,"$ Transferred successfully from", self.Code,'to',Accounts[other].Code)
        self.last_access = datetime.datetime.now()

Accounts = {}
fp= open('accounts.txt')
L=[]
for line in fp:
    record=line.split(",")
    line=line.strip('\n')
    Accounts.setdefault(int(record[0]),BankAccount(int(record[0]),record[1],record[2],
                                                   record[3],float(record[4])))
Accounts[122156]= BankAccount(CODE=122156, NAME="Lea Smith", BANK="TD", TYPE="saving", BALANCE=195.20)
Accounts[222552] = BankAccount(222552, 'John Green', 'RBC', 'chequing')
fp.close()
def PrintAllAccounts(A):
    for k in A:
        print(Accounts[k])
def accountlog(x):
    log=open('AccountsLog.txt','a')
    print(Accounts[int(x)], file = log)
    log.close()
while True:
    print(menu)
    option=int(input("Enter your choice:"))
    #option 1
    if option==1:
        PrintAllAccounts(Accounts)
    elif option==2:
        info=input("Enter your account information:")
        account= info.split(",")
        new_code=int(account[0])
        print(account)
        Accounts[new_code]=BankAccount(new_code,account[1],account[2],account[3], int(account[4]))
        print(Accounts[new_code])
        accountlog(int(account[0]))
    elif option==3:
        account_code=int(input("Enter account code:"))
        if account_code in Accounts:
            if Accounts[account_code].password=="":
                Accounts[account_code].create_pwd()
            else:
                print("Account does not exist")
    elif option==4:
        withd=input("Enter account code and amount")
        lst=withd.split(",")
        lst[1]=int(lst[1])
        lst[0]=int(lst[0])
        Accounts[lst[0]].withdraw(lst[1])
        accountlog(lst[0])
    elif option==5:
        dep=input("Enter account code and amount")
        lst=dep.split(",")
        lst[1]=int(lst[1])
        lst[0]=int(lst[0])
        Accounts[lst[0]].deposit(lst[1])
        accountlog(lst[0])
    elif option==6:
        tran=input("Enter account code to transfer from and to and the amount")
        lst=tran.split(",")
        lst[1]=int(lst[1])
        lst[0]=int(lst[0])
        lst[2]=int(lst[2])
        Accounts[lst[0]].transfer(lst[1],lst[2])
        accountlog(lst[0])
        accountlog(lst[1])
    elif option==7:
        code=int(input("Enter account code to know the balance:"))
        Accounts[code].get_balance()
        accountlog(code)
    elif option==8:
        log=open("AccountsLog.txt")
        for line in log:
            print(line)
        log.close()
    elif option==9:
        Accounts[122156].get_balance()
        break

