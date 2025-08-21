class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance
        
    def _isValidAccount(self, account: int):
        return account - 1 < len(self.balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self._isValidAccount(account1) and self._isValidAccount(account2) and \
            self.withdraw(account1, money) and self.deposit(account2, money):
            return True
        else:
            return False
        

    def deposit(self, account: int, money: int) -> bool:
        if self._isValidAccount(account):
            self.balance[account - 1] += money
            return True
        else:
            return False
        

    def withdraw(self, account: int, money: int) -> bool:
        if self._isValidAccount(account) and self.balance[account - 1] >= money:
            self.balance[account - 1] -= money
            return True
        else:
            return False
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)