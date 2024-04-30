# "______________Bank class___________"
class Bank:
    acc_holders = []
    bank_balance = 0
    def __init__(self,name):
        self.name = name


# "_____________User class________________"
class User:
    def __init__(self,name,email,address,account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.transaction = 0
        self.loan = 0
        Bank.acc_holders.append(self.name)

    def deposit_amount(self,amount):
        self.balance += amount
        self.transaction +=1
        Bank.bank_balance += amount

    def withdraw_amount(self,amount):
        if amount>self.balance:
            return  'Withdrawal amount exceeded'
        if amount>Bank.bank_balance:
            return "The Bank is bankrupt"
        self.balance-= amount
        self.transaction +=1

    def available_balance(self):
        return self.balance
    
    def transaction_history(self):
        return f"{self.transaction} amount of times has transaction happened"
    
    def take_loan(self,amount):
        if(self.loan!="OFF"):
            self.balance =+ amount
            Bank.bank_balance -= amount
            self.loan+=1

    def transfer_amount(self,acc,amount):
        if acc.name not in Bank.acc_holders:
            return "Account does not exist"
        acc.balance += amount
        self.balance - amount



# "_________________Admin Class_________________"
class Admin:
    def __init__(self,name):
        self.name = name

    def create_account(self,name,email,address,account_type):
        obj = User(name,email,address,account_type)
        Bank.acc_holders.append(obj.name)

    def delete_account(self,person):
        del person

    def see_user_list(self):
        return Bank.acc_holders
    
    def available_bank_balance(self):
        return Bank.bank_balance
    
    def loan_amount(self,person):
        return person.loan
    
    def loan_feature(self,person):
        if(person.loan==2):
            person.loan = "OFF"


# "___________________Replica System____________________"
while(True):
    a = int(input(f"WELCOME TO {Bank.__name__}!!!!!!"))
    print('1.Create Account:')
    print('2.Deposit Amount:')
    print('3.Withdraw Amount:')
    print('4.Transfer Amount:')
    print('5.Take Loan:')
    print("6.Exit")
    if a==1:
        name = input("Name: ")
        email = input("Email: ")
        address = input("Address: ")
        account_type = input("Account Type: ")
        obj1 = User(name,email,address,account_type)
    if a==2:
        amount = int(input("How much you want to depsoit?: "))
        obj1.deposit_amount(amount)
    if a==3:
        amount_withdraw = int(input("How much you want to withdraw?: "))
        obj1.withdraw_amount(amount)
    if a==4:
        transfer_amount = int(input("How much you want to transfer?: "))
        user_name = input("And who to?: ")
        obj1.transfer_amount(user_name,transfer_amount)
    if a==5:
        loan = int(input("How much you want to take loan?: "))
        obj1.take_loan(amount)
    if a==6:
        break