#Fibo Series using Recursion
num=int(input("Enter the Size for the series :"))
first=0
second=1
temp=0
for i in range(num):
    print(first)
    temp=first
    first=second
    second=temp+second
