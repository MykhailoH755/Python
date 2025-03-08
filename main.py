num = int(input("Enter num:"))  

if num >= 55:
    print("Yes")
    if num == 100:
        print("Num is 100")
    elif num == 40:
        print("Num is 40")
    elif num == 46:
        print("Num is 46")
    elif num < 4:
        print("Num is 4")
    else:
        print("Else")
        isHappy = True  

if 'isHappy' in locals() and not isHappy:
    print("Yes, he is happy")
