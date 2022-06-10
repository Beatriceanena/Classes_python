class Account:
    def _init_(self,account_name,account_number):
         self.account_name=account_name
         self.account_number=account_number
         self.balance = 0
         self.deposits=[]
         self.withdrawal=[]


         
    def deposit(self,amount):
       
        if amount <= 0:
            return f" Deposit must be a positive number"
            
        else:
            self.balance += amount
            self.deposits.append(amount)
            print(self.deposits)
            return f"Your current balance is{self.balance}" 

    def withdraw(self,amount):
         if amount <=0:
            return f"withdrawal must be greater than zero"
         elif amount >= self.balance:
            return f"Your balance is {self.balance} you cant withdraw {amount}"
         else:  
             self.balance-=amount
             
             return  f"Hello {self.account_name} you have withdrwan {amount} your new balance is {self.balance}"     


