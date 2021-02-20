class Bank_account:

    def __init__(self, account_no, balance, overdraft):
        self.account_no = account_no
        self.balance = balance
        self.overdraft = overdraft

        self.interest_rate = 0.04
        self.branch = "Vijaynagar"
    
    def credit(self, value):
        self.balance += value
    
    def debit(self, value):
        if self.balance <= 0:
            raise Exception
        self.balance -= value
    
    def comp_int(self, n):
        self.balance *= (1+self.interest_rate)*n   # n in years

    def __str__(self):
        return f"No.{self.account_no} with Total Balance(balance - overdraft) = Rs.{self.balance - self.overdraft}"


class Bank_account_with_exp(Bank_account):
    def __init__(self, account_no, balance, overdraft):
        super().__init__(account_no, balance, overdraft)
    
    def debit(self, value):
        if self.balance < value:
            raise InsufficientBalance(value)
        self.balance -= value
    
    def credit(self, value):
        if self.balance + value > 10000000:
            raise LimitExceeded(value)
        self.balance += value
    

class InsufficientBalance(Exception):
    def __init__(self, value):
        super().__init__()
        self.value = value
    
    def __str__(self):
        return f" Can't debit Rs.{self.value} Insufficient Balance!!!"

class LimitExceeded(InsufficientBalance):
    def __str__(self):
        return f"Can't credit more than Rs.{self.value} in a single day"

b1 = Bank_account_with_exp(23,1000,32)
b1.debit(500)
print(b1.debit(600))
