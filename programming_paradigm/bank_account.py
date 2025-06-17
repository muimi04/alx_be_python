class BankAccount:
    def __init__(self, initial_balance=0.0):
        self.__account_balance = initial_balance

    def deposit(self, amount):
        self.__account_balance += amount
        self._save_balance()

    def withdraw(self, amount):
        if self.__account_balance >= amount:
            self.__account_balance -= amount
            self._save_balance()
            return True
        return False

    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance:.2f}")

    def get_balance(self):
        return self.__account_balance

    def _save_balance(self):
        with open("balance.txt", "w") as f:
            f.write(str(self.__account_balance))

    @staticmethod
    def load_from_file():
        try:
            with open("balance.txt", "r") as f:
                balance = float(f.read())
        except FileNotFoundError:
            balance = 100.0  # Default starting balance
        return BankAccount(balance)
