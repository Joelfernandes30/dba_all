class Bank:
    def __init__(self, balance):
        self.balance = balance

    def __str__(self):
        return f"Your balance is {self.balance}"

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount >= self.balance:
            return "insufficient balance"
        else:
            self.balance = self.balance - amount

    def show_balance(self):
        return self.balance


user1 = Bank(10000)
print(user1.show_balance())

# user1.withdraw(3000)
# print(user1.show_balance())

user1.withdraw(700000)
print(user1.show_balance())