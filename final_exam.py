# "______________Bank class___________"
class Bank:
    acc_holders = []
    balance = 1000000000
    bankrupt = False
    if(balance==0):
        bankrupt = True



# "_____________User class________________"
class User:
    def __init__(self,name,email,address,account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.transaction = []
        self.loan = 0
        Bank.acc_holders.append(self.name)
        self.acc_number = self.name + self.email 
        self.is_bankrupt = False
        self.is_loan_active = True

    def deposit_amount(self,amount):
        self.balance += amount
        self.transaction +=1
        deposit_statement = f"Withdrawed amount - ${amount} "
        self.transaction.append(deposit_statement)

    def withdraw_amount(self,amount):
        if Bank.bankrupt:
            return "The Bank is bankrupt"
        if amount>self.balance:
            return  'Withdrawal amount exceeded'
        self.balance-= amount
        withdraw_statement = f"Withdrawed amount - ${amount} "
        self.transaction.append(withdraw_statement)
        if(self.balance==0):
            self.is_bankrupt = True

    def available_balance(self):
        return self.balance
    
    def transaction_history(self):
        return self.transaction
    
    def take_loan(self,amount):
        if(Bank.bankrupt):
            "The Bank is bankrupt"
        if(self.is_loan_active):
            self.balance =+ amount
            Bank.balance -= amount
            self.loan+=1
            if(self.loan>=2):
                self.is_loan_active = False
        else:
            "Maximum loan time exceeded"

    def transfer_amount(self,acc,amount):
        if acc.name not in Bank.acc_holders:
            return "Account does not exist"
        acc.balance += amount
        self.balance -= amount
        transfered_statement = f"Transfered amount - ${amount} "
        self.transaction.append(transfered_statement)
        



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
        if(person.loan>=2):
            person.is_loan_active = False


# "___________________Replica System____________________"
admin = Admin("admin")
while(True):
    print(f"!!!!!!  WELCOME TO {Bank.__name__}  !!!!!!")
    ad_us = int(input("press 1 for User,2 for Admin: "))
    if(ad_us==1):
        print('1.Create Account:')
        print('2.Deposit Amount:')
        print('3.Withdraw Amount:')
        print("4.Check balance: ")
        print("5.Check Transaction history: ")
        print('6.Transfer Amount:')
        print('7.Take Loan:')
        print("8.Exit")
        a = int(input("Your choice: "))
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
            obj1.available_balance()
        if a==5:
            obj1.transaction_history()
        if a==6:
            transfer_amount = int(input("How much you want to transfer?: "))
            user_name = input("And who to?: ")
            obj1.transfer_amount(user_name,transfer_amount)
        if a==7:
            loan = int(input("How much you want to take loan?: "))
            obj1.take_loan(amount)
        if a==8:
            break
    else:
        admin_name = input("Enter Admin name: ")
        if(admin_name == 'admin'):
            admin_pass = int(input("Enter password: "))
            if(admin_pass == 1234):
                print('1.Create User account:')
                print('2.Delete User:')
                print('3.See all user list')
                print('4.Available balance of bank:')
                print('5.Total loan amount:')
                print("6.Loan feature of the bank")
                print("7.Exit:")
                a = int(input("Your choice: "))
                if a==1:
                    name = input("Name: ")
                    email = input("Email: ")
                    address = input("Address: ")
                    account_type = input("Account Type: ")
                    admin.create_account(name,email,address,account_type)
                if a==2:
                    acc_name = input("Give the account obj name to delete: ")
                    admin.delete_account(acc_name)
                if a==3:
                    print(Bank.acc_holders)
                if a==4:
                    print(Bank.balance)
                if a==5:
                    acc_name = input("Give the account obj name to check the loan amount: ")
                    admin.loan_amount(acc_name)
                if a==6:
                    acc_name = input("Give the account obj name to turn the loan feature off: ")
                    admin.loan_feature(acc_name)
                if a==7:
                    break
