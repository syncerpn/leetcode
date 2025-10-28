# easy
class Bank:

    def __init__(self, balance: List[int]):
        self.A = [0] + balance
        self.n = len(self.A)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 >= self.n or account2 >= self.n or self.A[account1] < money:
            return False
        self.A[account1] -= money
        self.A[account2] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if account >= self.n:
            return False
        self.A[account] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account >= self.n or self.A[account] < money:
            return False
        self.A[account] -= money
        return True
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)