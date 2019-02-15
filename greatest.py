#Find Greatest Among Three Numbers
num1=int(input("Enter the 1 Number :"))
num2=int(input("Enter the 2 Number :"))
num3=int(input("Enter the 3 Number :"))
if num1>num2:
    if num1>num3:
        print("Number {0} is Greater".format(num1))
    else:
        print("Number {0} is Greater".format(num3))
elif num2>num3:
    print("Number {0} is Greater".format(num2))
else:
    print("Number {0} is Greater".format(num3))
