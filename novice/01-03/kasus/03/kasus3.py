class BankAccount:

    def __init__(self):
        self.balance = 0

    def deposit(self):
        amount=float(input("Enter amount to be Deposited: ")) 
        self.balance += amount
        print('Your current balance is ',amount)
        

    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: ")) 
        if self.balance>=amount: 
            self.balance-=amount 
            print("\n You Withdrew:", amount) 
        else: 
            print("\n Insufficient balance  ")

    def display(self):
        print('Your current balance',self.balance)

    def print_balance(self):
        return self.balance
    
account = BankAccount()
Invalid_input = True
def start():
    print("====================================================")
    print("\tWelcome to this simple ATM machine")
    print("====================================================")
    print("    Please select ATM Transaction    ")
    print("""
    1)        Deposit
    2)        Withdraw
    3)        Balance Inquiry
    4)        Quit


    """)


    Option=int(input("Enter Option: "))

    if Option==1:
        print("Balance ",account.balance)
        account.deposit()
        

    if Option==2:
        print('Balance  ',account.balance)
        account.withdraw()

    if Option==3:
        account.display()
        

    if Option==4:
        exit()


while Invalid_input:
    start()
