class Numbers:

    def __init__(self):
        self.Value = int(input("\nEnter number : "))

    def ChkPrime(self):
        if self.Value <= 1:
           return False
        
        for i in range(2,self.Value):
            if self.Value % 2 == 0:
                return False
            
        return True
       
    def ChkPerfect(self):
        Sum = 0

        for i in range(1,self.Value):
            if self.Value % i == 0:
                Sum = Sum + i

        if Sum == self.Value:
            return True
        else:
            return False
        
    def Factors(self):
        print("Factors : ")
        for i in range(1,self.Value + 1):
            if self.Value % i == 0:
                print(i)

    def SumFactors(self):
        Sum = 0

        for i in range(1,self.Value + 1):
            if self.Value % i == 0:
                Sum = Sum + i

        print("Sum of Factors : ",Sum)

nobj1 = Numbers()
print("Prime : ",nobj1.ChkPrime())
print("Perfect : ",nobj1.ChkPerfect())
nobj1.Factors()
nobj1.SumFactors()

nobj2 = Numbers()
print("Prime : ",nobj2.ChkPrime())
print("Perfect : ",nobj2.ChkPerfect())
nobj2.Factors()
nobj2.SumFactors()