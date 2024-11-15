class BankAccount:
    def __init__(self, account_holder: str, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        """
        This is to put money in the account
        Args:
            amount (int or float): money to add
        """
        if amount < 0:
            print("The amount has to be positive")
        else:
            self.balance = self.balance + amount
            return self.balance

    def withdraw(self, amount):
        """
        This is to withdraw money from the account
        Args:
            amount (int or float): money to remove
        """
        if self.balance < 0:
            print("You can't withdraw not enough money on the account !")
        elif (self.balance - amount) < 0:
            print(
                "Withdraw will put the account in negative, add money first.")
        else:
            self.balance = self.balance - amount
        return self.balance

    def display_balance(self):
        """
        Display the total of money in the account and the name of the owner.
        """
        print(f"Owner is {self.account_holder} and has {self.balance} euros.")


new_bank_account = BankAccount("Morticia Adams", 5000)
new_bank_account.display_balance()
new_bank_account.deposit(50)
new_bank_account.withdraw(200)
new_bank_account.display_balance()
print()
bank_account = BankAccount("Wednesday Adams", 10)
bank_account.display_balance()
bank_account.withdraw(200)
