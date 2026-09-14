
def Fact(No):
    if(No <= 1):
        return 0
    else:
        return(No * Fact(No-1))
        
Ret = Fact(4)

print("Result is : ",Ret)