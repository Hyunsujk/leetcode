class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance
        self.accounts = len(self.balance)
        

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 < 1 or account1 > self.accounts or account2 < 1 or account2 > self.accounts:
            return False
        if self.balance[account1 - 1] < money:
            return False
        else:
            self.withdraw(account1, money)
            self.deposit(account2, money)
            return True
        

    def deposit(self, account: int, money: int) -> bool:
        if account < 1 or account > self.accounts:
            return False
        else:
            self.balance[account - 1] += money
            return True
        

    def withdraw(self, account: int, money: int) -> bool:
        if account < 1 or account > self.accounts or self.balance[account - 1] < money:
            return False
        else:
            self.balance[account - 1] -= money
            return True
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)