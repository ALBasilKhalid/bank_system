class BankAccount:
  """
  This class represents a bank account with attributes and methods.
  """

  def __init__(self, account_number, name, balance=0.0):
    """
    Initializes a BankAccount object.

    Args:
      account_number: The unique account number.
      name: The account holder's name.
      balance: The initial balance (default: 0.0).
    """
    self.account_number = account_number
    self.name = name
    self.balance = balance

  def deposit(self):
    """
    Deposits money into the account.

    Args:
      None (prompts user for input).
    """
    while True:
      try:
        amount = float(input("Enter amount to deposit (positive value): "))
        if amount <= 0:
          print("Invalid deposit amount. Please enter a positive value.")
        else:
          self.balance += amount
          print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
          break
      except ValueError:
        print("Invalid input. Please enter a numerical value.")

  def withdraw(self):
    """
    Withdraws cash from the account.

    Args:
      None (prompts user for input).
    """
    while True:
      try:
        amount = float(input("Enter amount to withdraw (positive value): "))
        if amount <= 0:
          print("Invalid withdrawal amount. Please enter a positive value.")
        elif amount > self.balance:
          print(f"Insufficient funds. Your balance is ${self.balance:.2f}.")
        else:
          self.balance -= amount
          print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
          break
      except ValueError:
        print("Invalid input. Please enter a numerical value.")

  def interest(self):
    """
    Applies a 5% interest to the account balance.
    """
    interest_amount = self.balance * 0.05
    self.balance += interest_amount
    print(f"Applied 5% interest. New balance: ${self.balance:.2f}")

  def display(self):
    """
    Displays the account details.
    """
    print(f"Account Number: {self.account_number}")
    print(f"Account Holder: {self.name}")
    print(f"Balance: ${self.balance:.2f}")


def find_account(accounts, account_number):
  """
  Finds an account by account number from a list of accounts.

  Args:
    accounts: A list of BankAccount objects.
    account_number: The account number to search for.

  Returns:
    The BankAccount object if found, otherwise None.
  """
  for account in accounts:
    if account.account_number == account_number:
      if(account.account_number=="138410"):
          print()
          print("-----------------------------------Welcome back my Owner-----------------------------------")
      return account
  return None


def main():
  """
  Main function to manage a specific bank account.
  """
  # Create bank accounts
  accounts = [
      BankAccount("138410", "ALBASIL ALRAWAHI", 1000.00),
      BankAccount("123456", "Abdul Rahman Aal Abdulsalam", 500.00),
  ]
  looping=True
  # User Interaction Loop
  while looping:
    account_number = input("Enter account number (or 'exit' to quit): ")

    if account_number == 'exit':
      print("Thank you for using (ALRAWAHI's Bank), wish you a wealthy life...")
      break

    account = find_account(accounts, account_number)

    if account:
      # Account found, display menu
      while looping:
        print("\nBank Account Menu")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Apply Interest")
        print("4. Display Account Details")
        print("5. Switch Account")  # Option to switch account
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
          account.deposit()
        elif choice == '2':
          account.withdraw()
        elif choice == '3':
          account.interest()
        elif choice == '4':
          account.display()
        elif choice == '5':
          break  # Break
        elif choice == '6':
          print("Thank you for using (Basil's Bank), wish you a wealthy life...")
          looping=False
if __name__ == "__main__":
  main()