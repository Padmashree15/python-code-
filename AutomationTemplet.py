from sys import *
from os import *

def Script_Task(No):
    if((No % 2) == 0):
        print("It is even number")
    else:
        print("It is odd number")

def main():
    print("--------Marvellous Infosystem Automations---------")

    print("Automation script started with name :",argv[0])

    if(len(argv) != 2):
        print("Error : Insufficient arguments")
        print("Use -h for help and use -u for usage of the script")
        exit()

    if((argv[1] == "-h") or (argv[1] == "-H")):
        print("Help : This script is use to perform _____________")
        exit()

    elif((argv[1] == "-u") or (argv[1] == "-U")):
        print("Usage : Provide ____ number of arguments as")
        print("First Arguments as : __________")
        print("Second Arguments as : ___________")
        exit()

    else:
        Script_Task(int(argv[1]))

if __name__ == "__main__":
    main()