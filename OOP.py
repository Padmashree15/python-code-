class Arithematic:
    def __init__(self,A,B):
        self.No1 = A
        self.No2 = B 

    def Add(self):
        return self.No1 + self.No2

    def Sub(self):
        return self.No1 - self.No2


def main():
    print("Enter first number")
    iValue1 = int(input())

    print("Enter second number")
    iValue2 = int(input())

    obj = Arithematic(iValue1,iValue2)

    Ans = obj.Add()
    print("Addition is : ",Ans)

    Ans = obj.Sub()
    print("Substraction is : ",Ans)

    
if __name__== "__main__":
    main()