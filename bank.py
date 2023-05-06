class   Bankaccount:
    bank = "Equity"

    def __init__(self, account_owner,account_number,balance):
        self.account_owner = account_owner
        self.account_number = account_number
        self.balance = balance

    def describe_account(self):
        return (f"{self.account_number} with {self.balance} is owned by {self.account_owner}")
    
    def deposit(self,amount):

        return(f"{self.account_owner} has deposited {amount}")
    
    def display_balance(self,amount):
        self.balance += amount 
        return((f"{self.account_owner} new balance is {self.balance}"))