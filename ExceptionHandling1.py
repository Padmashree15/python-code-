
def main():
    print("Enter first number ")
    No1 = int(input())

    print("Enter first number ")
    No2 = int(input())
    try:
        Ans = No1 / No2
        print("Division is : ",Ans)

    except ZeroDivisionError:
        print("Division of any number by zero is not practically possible. Please again run the code and enter non zero denominator")

if __name__ == "__main__":
    main()