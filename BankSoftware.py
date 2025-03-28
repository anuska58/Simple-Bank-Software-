class BankAccount:
    def __init__(self,acc_number,name,phone,address,balance=0.00):
        self.account=acc_number
        self.name=name
        self.phone=phone
        self.address=address
        self.balance=balance

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"Deposited ${amount:.2f} in account number {self.account}. Your current balance is {self.balance:.2f}")
        else:
            print("Amount should be greater than 0")

    def withdraw(self,amount):
        if 0<amount <=self.balance:
            self.balance-=amount
            print(f"Withdrawn ${amount:.2f} from account number {self.account}. Your current balance is {self.balance:.2f}")
        else:
            print("Insufficient balance or invalid withdrawal amount")

    def get_balance(self):
        return f"Dear {self.name}, the account number {self.account} has balance: ${self.balance:.2f}"

ram=BankAccount("091234","Ram","9810290129","Birauta",100)
ram.deposit(5000)
ram.withdraw(1000)

print(ram.get_balance())
# acc1=BankAccount(0926182912, )
