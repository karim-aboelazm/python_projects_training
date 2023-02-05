class ATM:
    def __init__(self, balance = 0):
        self.balance = balance
    
    def check_balance(self):
        print(f"Your current balance is : ${self.balance}")
    
    def deposit(self,amount):
        self.balance += amount
        print(f"You have deposited ${amount}.\nYour new balance is : ${self.balance}")
    
    def withdraw(self,amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            print(f"You have withdrawn ${amount}.\nYour new balance is : ${self.balance}")
        else:
            print(f"Not Allowed!, Your amount is bigger than Your balance.\nYour balance is : ${self.balance} ")

atm = ATM()
while True:
    print("""
ATM Using Python
-------------------------
1. Check Your Balance.
2. Deposit New Balance.
3. Withdraw Balance
4. Quit.
          """)
    choice = int(input("Enter Yout Choice : "))
    if choice == 1:
        atm.check_balance()
    elif choice == 2:
        amount = int(input("Enter amount to deposit : "))
        atm.deposit(amount)
    elif choice == 3:
        amount = int(input("Enter amount to withdraw : "))
        atm.withdraw(amount)
    elif choice == 4:
        print("Thank you for using the ATM. Have a great day!")
        break
    else:
        print("This choice not allowed..\n")