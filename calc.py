a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

operation=input("Choose an operation: add/sub/mul/div:")

if(operation=="add"):
    print(a+b)
elif(operation=="sub"):
    print(a-b)
elif(operation=="mul"):
    print(a*b)
elif(operation=="div"):
    if b == 0:
        print("denominator cant be zero.")
    else:
        print(a/b)
else:
    print("invalid operation")
    

