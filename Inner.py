def Demo():
    print("Inside the demo")

    def Hello():
        print("Inside Demo")

def Fun():
    print("inside fun")
    
def Hello(FPTR):
    print("Inside Hello")

    
Hello(Demo)
Hello(Fun)
Hello(11)

