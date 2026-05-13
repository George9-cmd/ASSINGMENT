from Accounts import Account

class Savings(Account):
    def __init__(self, owner, balance=0):
      super().__init__(owner, balance)        
      self.interest_rate = 0.02  # 
      self.withdrawal_limit = 100  
    
    def withdraw(self, amount):
        if amount > self.withdrawal_limit:
            print(f"Withdrawal amount exceeds the limit of ${self.withdrawal_limit}.")
        elif amount > self.get_balance():
            super().withdraw(amount)  
        else: 
            print( "Invalid withdrawal amount or insufficient funds.")

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Applied interest: ${interest}. New balance: ${self.get_balance()}")

#Test the Savings account
print("~~.Savings Account ~~.") 
savings = SavingsAccount( owner:"Alice" , balance: 1000) 
print (f"Initial balance: ${savings.get_balance()}")
savings.deposit(500) 
savings.withdraw(200)#Should be denied (exceeds $100 limit) 
savings.withdraw(50) #Should succeed
    
       
                  
    