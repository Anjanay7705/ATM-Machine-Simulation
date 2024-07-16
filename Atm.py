class ATM:
    """
    This class simulates an ATM machine with basic functionalities.
    """

    def __init__(self, balance=0, pin=1234, transactions=[]):
        """
        Initializes the ATM object with starting balance, PIN, and transaction history.

        Args:
            balance (int): The initial account balance. Defaults to 0.
            pin (int): The default PIN for the account. Defaults to 1234.
            transactions (list): A list to store transaction history. Defaults to an empty list.
        """
        self.balance = balance
        self.pin = pin
        self.transactions = transactions

    def check_balance(self):
        """
        Displays the current account balance.
        """
        print(f"Your current balance is: {self.balance}")

    def withdraw_cash(self, amount):
        """
        Withdraws cash from the account if the balance is sufficient.

        Args:
            amount (int): The amount to withdraw.

        Returns:
            bool: True if withdrawal successful, False otherwise.
        """
        if amount > self.balance:
            print("Insufficient funds.")
            return False
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -{amount}")
            print(f"Withdrawal successful. New balance: {self.balance}")
            return True

    def deposit_cash(self, amount):
        """
        Deposits cash into the account.

        Args:
            amount (int): The amount to deposit.
        """
        self.balance += amount
        self.transactions.append(f"Deposit: +{amount}")
        print(f"Deposit successful. New balance: {self.balance}")

    def change_pin(self, new_pin):
        """
        Changes the account PIN.

        Args:
            new_pin (int): The new PIN.
        """
        self.pin = new_pin
        print("PIN changed successfully.")

    def view_transactions(self):
        """
        Displays the transaction history.
        """
        if not self.transactions:
            print("No transaction history available.")
        else:
            print("Transaction History:")
            for transaction in self.transactions:
                print(transaction)

def main():
    """
    The main function of the ATM simulation.
    """
    atm = ATM()
    while True:
        print("\nATM Machine")
        print("1. Check Balance")
        print("2. Withdraw Cash")
        print("3. Deposit Cash")
        print("4. Change PIN")
        print("5. View Transaction History")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            amount = int(input("Enter the amount to withdraw: "))
            atm.withdraw_cash(amount)
        elif choice == '3':
            amount = int(input("Enter the amount to deposit: "))
            atm.deposit_cash(amount)
        elif choice == '4':
            new_pin = int(input("Enter your new PIN: "))
            atm.change_pin(new_pin)
        elif choice == '5':
            atm.view_transactions()
        elif choice == '6':
            print("Thank you for using the ATM!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()