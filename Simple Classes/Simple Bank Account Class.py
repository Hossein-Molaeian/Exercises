class Account():

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Unavailable funds.")
        else:
            self.balance -= amount
            print(f"You have withdrawn {amount} from your balance.")

    def deposit(self, amount):
        self.balance += amount
        print(f"We added {amount} to your balance.")

    def __str__(self):
        return f"Account owner:     {self.owner}\nAccount balance:   ${self.balance}"


acc1 = Account('Hossein', 100)
acc1.deposit(50)
acc1.withdraw(75)
print(acc1)
