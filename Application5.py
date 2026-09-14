def Multiplication(iValue1, iValue2):
    
    iOutput = iValue1 * iValue2

    return iOutput

def main():

    print("Enter first number : ")
    iNo1 = int (input())

    print("Enter second number : ")
    iNo2 = int (input())

    iRet = Multiplication(iNo1, iNo2)
    print("Multiplication is : ",iRet)

if __name__ == " __main__ ":
        main()

