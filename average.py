# n=int(input("Enter the Number :"))
def average(n):
    if n==1:
        return 1
    else:
        return (n+average(n-1))


n=int(input("Enter the Number :"))
print('average value of number ',average(n)/n)