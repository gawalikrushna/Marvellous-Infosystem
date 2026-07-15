class BankAccount:

    ROI = 10.5

    def __init__(self,Name,Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("\nAccount holder name : ",self.Name)
        print("Current balance : ",self.Amount)

    def Deposit(self, deposit):
        self.Amount = self.Amount + deposit
        print("Account balance after deposit : ",self.Amount)

    def Withdraw(self, withdraw):
        self.Amount = self.Amount - withdraw
        print("Account balance after withdraw : ",self.Amount)

    def CalInterest(self):
        CI = (self.Amount * BankAccount.ROI) / 100
        print("Interest is : ",CI)

bobj1 = BankAccount("Krushna",100000)
bobj2 = BankAccount("Deepak",150000)
bobj3 = BankAccount("Swapnil",50000)

bobj1.Display()
bobj1.Deposit(50000)
bobj1.Withdraw(5000)
bobj1.CalInterest()

bobj2.Display()
bobj2.Deposit(100000)
bobj2.Withdraw(7000)
bobj2.CalInterest()

bobj3.Display()
bobj3.Deposit(4000)
bobj3.Withdraw(5500)
bobj3.CalInterest()