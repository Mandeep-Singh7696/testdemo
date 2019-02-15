n=int(input("Enter the Number :"))
def average(n):
    if n==1:
        return 1
    else:
        return (n+average(n-1))/n
