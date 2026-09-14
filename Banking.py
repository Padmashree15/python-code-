#Instance variables : Name, Amount, Address, AccountNo
#Instance method : CreateAccount, DisplayAccountInfo
#Class Variables : Bank_Name, ROI_On_FD
#Class method : DisplayBankInfo
#Static method : DisplayKYCInfo
class Bank_Account():
    
    Bank_Name = "HDFC bank PVT LTD"
    ROI_On_FD = 6.7

    def __init__(self):
        self.Name = ""
        self.Amount = 0
        self.Address = ""
        self.AccountNo = 0

    def CreateAccount(self):
        print("Enter your Name : ")
        self.Name = input()

        print("Enter your Initial Amount : ")
        self.Amount = int(input())

        print("Enter your Address : ")
        self.Address = input()

        print("Enter your Account Number : ")
        self.AccountNo = int(input())

    def DisplayAccountInfo(self):
        print("-----Your Account information is as below -----")
        print("Name of Accout Holder : ",self.Name)
        print("Account Number of Accout Holder : ",self.AccountNo)
        print("Address of Accout Holder : ",self.Address)
        print("Current Amount in account : ",self.Amount)

    @classmethod
    def DisplayBankInfo(cls):
        print("Welcome to Banking console")
        print("Name of our Bank : ",cls.Bank_Name)
        print("Rate of Interest we offer on fixed deposite is : ",cls.ROI_On_FD)

    @staticmethod
    def DisplayKYCInfo():
        print("Please consider below KYC Information")
        print("According to the rules of Governmetnt of India you have to submit below documents")
        print("1 : Clear and recent passport size photo")
        print("2 : Photo of Aadhar card")
        print("3 : Photo of PAN card")

    def Deposite(self,value):
        print("Enter the amount you want to Deposite : ",value)
        self.Amount = self.Amount + value

    def Withdraw(self,value):
        self.Amount = self.Amount - value

def main():

    print("---------------Banking Application-----------------")

    print("----------Calling Static method to display KYC Info-----------")
    Bank_Account.DisplayKYCInfo()

    print("Name of Bank : ",Bank_Account.Bank_Name)
    print("Rate of Interest on Fixed deposite : ",Bank_Account.ROI_On_FD)

    Bank_Account.DisplayBankInfo()

    User1 = Bank_Account()
    User2 = Bank_Account()

    print("Creating the first Account---")
    User1.CreateAccount()
    print("Creating the second Account---")
    User2.CreateAccount()

    print("-----Calling instance method to display information of first account---------")
    
    print("First Account")
    User1.DisplayAccountInfo()
    print("                                        ")
    print("Second Account")
    User2.DisplayAccountInfo()

    User1.Deposite(500)
    User2.Deposite(1200)

    print("Amount of {} after deposite is {}: ".format(User1.Name, User1.Amount)
    print("Amount of {} after deposite is {}: ".format(User2.Name, User2.Amount)

    User1.Withdraw(200)
    User2.Withdraw(3000)

    print("Amount of {} after deposite is {}: ".format(User1.Name, User1.Amount)
    print("Amount of {} after deposite is {}: ".format(User2.Name, User2.Amount)


if __name__ == "__main__":
    main()
