from sklearn import tree

def BallPredictor(weight,surface):

    Features = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]]
    Labels = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

    obj = tree.DecisionTreeClassfier()

    obj = obj.fit(Features, Lables)

    ret = obj.predict([[weight,surface]])
    if ret == 1:
        print("Your object looks like a tennis ball")
    else
        print("Your object looks like a cricket ball")
        
def main():
    print("-----------Ball Predictor Case Study----------------")

    print("Please enter the weight of object in grams")
    weight = int(input())

    print("Please enter the type of surface of your object (Rough / Smooth")
    surface = input()

    if:
        surface.lower() == "rough":
        surface = 1
    elif:
        surface.lowwr() == "smooth":
        surface = 0
    else:
        print("Invalid type of surface")
        exit()

    BallPredictor(weight,surface)

if __name__ == "__main__":
    main()