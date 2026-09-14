
def Add(No):
    Cnt = 0
    while(No >= 0):
        Cnt = Cnt + No
        No = No - 1
    return Cnt

Ret = Add(4)

print("Result is : ",Ret)