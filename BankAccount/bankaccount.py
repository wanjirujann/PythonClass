from datetime import datetime


class BankAccount:
    bank = "Barclays"
    
    def __init__(self, first_name, last_name, phone_number, bank):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.bank = bank
        self.balance = 0
        self.deposits[]
        self.withdrawals[]
        self.loan = 0
        self.loan_repayments = []
        self.paybill_number2222 = []
        
    def account_name(self):
        name = "{} account for {} {}".format(self.bank, self.first_name, self.last_name)
        return name
    
    def deposit(self,amount):
        try:
            amount + 1
        TypeError:
        except:
            print("Please enter your amount in figures")
        if amount <= 0:
            print("You cannot deposit zero or negative")
         else:
            self.balance += amount:
            time = datetime.now()
            deposit = {
            "time": time
            "amount": amount
            }
            self.deposits.append(deposit)
            formatted_time = time.strftime("%H:%M%p %d/%m/%Y")
            print("You have deposited {} to {}".format(amount, self.account_name()))

    def get_balance(self):
        return("The balance for {} is {}".format(self.account_name(), self.balance))
        

    def withdraw(self, amount):
        try:
            amount - 1
       
        except TypeError:
            print("Please enter your amount in figures")
        if amount <= 0:            
            print("You cannot withdraw zero or negative")
        elif: 
            amount > self.balance
            print("Insufficient funds") 
        else:
            self.balance -= amount:
            self.withdrawals.append(amount)
            print("You have withdrawn {} from {}".format(amount, self.account_name()))

    def get_balance(self):
        return ("The balance for {} is {} ".format(self.account_name(),self.balance))

    def show_deposit_statement(self):
        for deposit in self.deposits:
            print(deposit)

    def show_withdrawal_statement(self):
        for withdrawal in self.withdrawals:
            print(withdrawal)
    
    def request_loan(self, loan):
        try:
            amount + 1
        except TypeError:
            print("Please enter your amount in figures")
        if amount <- 0:
            print("You cannot request a loan of that amount")
        else:
            self.loan = amount:
            print("You have received a loan of {}".format(amount))

    def repay_loan(self, amount):
        try:
            amount + 1
        except TypeError:
            print("You must enter the amount in figures")
            return

        if amount <= 0:
            print("Too low t repa your amount")
        elif self.loan == 0:
            print("You don't have a loan at the moment")
        elif amount > self.loan:
            print("Your loan is {} please enter an amount that is less or equal".format(self.loan))
        else:
            self.loan -= amount
            time = datetime.now()
            repayment = {
                "time": time,
                "amount": amount
            }
            self.loan_repayments.append(repayment)
            print("You have repaid you loan with {} your balance is {}".format(amount, self.loan))
    
    def loan_repayment_statement(self):
        for repayment in self.loan_repayments:
            time = repayment["time"]
            amount = repayment["amount"]
            formatted_time = self.get_formatted_time(time)
            statement = "You repaid {} on {} ".format(amount, formatted_time)
            print(statement)

class BankAccount(Account):
    def _init_(self, first_name, last_name,Phone_no, bank):
        self.bank = bank
        super()._init_(first_name, last_name, Phone_no)

class MobileMoneyAccount(Account):
    def _init_(self, first_name, last_name, Phone_no, service_provider):
        self.airtime = []
        super()._init_(first_name, last_name, Phone_no)

    def buy_airtime(self, amount):
        try:
            amount + 1
        except TypeError:
            print("Please enter the amount in figures")
            return
        if amount > self.balance:
            print("You dont have enough balance. Your balnce is {}".format(self.balance))
        else:
            self.balance -= amount 
            time =datetime.now()
            airtime = {
                "time": time,
                "airtime": amount
            }
            self.airtime.append(airtime)
            print("You have bought airtime worth of {} on {} ".format(amount, self.get_formatted_time(time)))




    
        
acc1 = BankAccount("Jann", "Wanjiru")
acc2 = BankAccount("Alma", "Maywah")       

acc1.deposit(2000)
acc2.deposit(1000)
acc1.deposit(4000)
acc2.deposit(-500)
acc1.withdraw(200)
acc2.withdraw(100)
acc1.withdraw(550)
acc2.deposit(150)


print(acc1.get_balance())
print(acc2.get_balance())

