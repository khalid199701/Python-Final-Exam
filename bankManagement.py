class User:
    def __init__(self, name, email, address, account_type, nid, bank) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.nid = nid
        self.bank = bank
        self.account_no = len(bank.users)+1
        self.history = []
        self.loan_no = 0
    
    def deposit(self, amount, bank):
        if amount > 0:
            i = self.balance
            self.balance += amount
            bank.bank_balance += amount
            self.history.append(f"{i} + {amount} = {self.balance}")

    def withdraw(self, amount, bank):
        if self.balance >= amount:
            if bank.bank_balance >= amount:
                i = self.balance
                self.balance -= amount
                bank.bank_balance -= amount
                self.history.append(f"{i} - {amount} = {self.balance}")
            else:
                print(f"The {bank.name} bank is bankrupt")
        else:
            print("Withdrawal amount exceeded")
    def check_balance(self):
        print(self.balance)
    
    def transaction_history(self):
        print(self.history)

    def transfer_money(self, bank, user, amount):
        if isinstance(bank, Bank):
            if user in bank.users:
                if self.balance >= amount:
                    if bank.bank_balance >= amount:
                        i = self.balance
                        self.balance -= amount
                        bank.bank_balance -= amount
                        user.balance += amount
                        self.history.append(f"{i} - {amount} = {self.balance}")
            else:
                print("Your account info is incorrect")
    
    def take_loan(self, amount, bank):
        if bank.loan_flag == True:
            if bank.bank_balance >= amount:
                if self.loan_no <= 2:
                    if bank.loan_flag:
                        self.loan_no += 1
                        self.balance += amount
                        bank.bank_balance -= amount
                    else:
                        print(f"{bank.name} Bank is not giving any loan right now")
                else:
                    print("Your loan limit gone")
            else:
                print(f"{bank.name} bank is bankrupt right now")
        else:
            print("Bank is not giving loan right now")
        


class Admin:
    def __init__(self, email, password) -> None:
        self.email = email
        self.password = password


class Bank:
    def __init__(self, name, initial_balance) -> None:
        self.name = name
        self.admins = []
        self.users = []
        self.bank_balance = initial_balance
        self.loan_given = 0
        self.loan_flag = True

    def add_admin(self, email, password):
        admin = Admin(email, password)
        self.admins.append(admin)

    def add_account(self, name, email, address, account_type, nid, bank):
        user = User(name, email, address, account_type, nid, bank)
        self.users.append(user)

    def delete_account(self, user, bank):
        if user in self.users:
            for user in self.users:
                self.users.remove(user)
    
    def all_users(self):
        for user in self.users:
            print(user.name, user.account_no)

    def bank_balance_check(self):
        print(self.bank_balance)

    def loan_turn_off(self):
        self.loan_flag = False
    

dbbl = Bank("Dutch-Bangla", 10000000)
admin = dbbl.add_admin("abu@gmail.com", 12345)
sakib = dbbl.add_account("Sakib", "sakib@gmail.com", "Dhaka", "Saving", 112233, dbbl)

while True:
    print("1: Login as Admin")
    print("2: Login as User")
    print("3 or other: Exit")

    ch = int(input())
    if ch == 1:
        em = input("Give me the email: ")
        ps = input("Give me the password: ")
        currentuser = None
        for i in dbbl.admins:
            if i.email == em and i.password == ps:
                currentuser = i
        while True:
            print("1: Create an Account")
            print("2: Delete an Account")
            print("3: See all users Account")
            print("4: The total available balance of the bank")
            print("5: The total loan amount given by the bank")
            print("6: Turn off loan")
            print("7: Exit")
            i = int(input())
            if i == 1:
                # sakib = dbbl.all_users("Sakib", "sakib@gmail.com", "Dhaka", "Saving", 112233, dbbl)
                nme = input("Give me your name: ")
                eml = input("Give me your email id: ")
                adrs = input("Give me your address: ")
                tpe = input("Give me your account type: ")
                nd = input("Give me your nid: ")
                nme = dbbl.add_account(nme, eml, adrs, tpe, nd, dbbl)

            elif i == 2:
                nme = input("Give me the name: ")
                eml = input("Give me the email id: ")
                nm = input("Give me the account number: ")
                for j in dbbl.users:
                    if j.name == nme and j.email == eml and j.account_no == nm:
                        dbbl.delete_account(j, dbbl)
            elif i == 3:
                dbbl.all_users()
            elif i == 4:
                dbbl.bank_balance_check()
            elif i == 5:
                print(dbbl.loan_given)
            elif i == 6:
                print("Current Status of loan given: ", dbbl.loan_flag)
                dbbl.loan_turn_off()
                print("Current Status of loan given: ", dbbl.loan_flag)
            else:
                break
    elif ch == 2:
        nm = input("Input your account name: ")
        n = int(input("Input your account number: "))
        currentuser = None
        for u in dbbl.users:
            if nm == u.name and n == u.account_no:
                currentuser = u
        while currentuser:
            print("1: Deposit in your account")
            print("2: Withdraw money")
            print("3: Balance check")
            print("4: Check my account history")
            print("5: Transfer money")
            print("6: Want to take a loan")
            print("7 or others to exit")
            i = int(input())
            if i == 1:
               amount = int(input("Give me a amount to diposit: "))
               currentuser.deposit(amount, dbbl)
            elif i == 2:
                amount = int(input("Give me a amount to withdraw: "))
                currentuser.withdraw(amount, dbbl)
            elif i == 3:
                print(currentuser.balance)
            elif i == 4:
                currentuser.transaction_history()
            elif i == 5:
                nme = input("Give me the account name you want to transfer: ")
                nb = int(input("Give me the account number you want to transfer: "))
                amount = int(input("Give me the amount you want to transfer: "))
                for j in dbbl.users:
                    if j.name == nme and j.account_no == nb:
                        break
                currentuser.transfer_money(dbbl, j, amount)
            elif i == 6:
                amount = int(input("Give me a amount of loan: "))
                currentuser.take_loan(amount, dbbl)
            else:
                break
    else:
        break