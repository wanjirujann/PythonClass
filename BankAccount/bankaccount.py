class BankAccount:
    bank = "Barclays"
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 0
        
    def account_name(self):
        name = "{} account for {} {}".format(self.bank, self.first_name, self.last_name)
        return name
    
    def deposit(self,amount):
        self.balance += amount
        if amount > 0:
            print("You have deposited {} to your account".format(amount))
        else: 
            print("Insufficient funds deposited")          
    
    def get_balance(self):
        return("The balance for {} is {}".format(self.account_name(), self.balance))
        

    def withdraw(self, amount):
        if amount > 0:            
            self.balance -= amount
            print("You have withdrawn {} from your account".format(amount))
        else: 
            print("Insufficient funds") 
    def get_balance(self):
        return ("The balance for {} is {} ".format(self.account_name(),self.balance))
        
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