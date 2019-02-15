# printing Pattern 2
# for i in range(1,5):
#     print("#",end="")
#     for j in range(4,i,-1):
#         print("#",end="")
#     # print()
i=1
while i<5:
    print("#",end="")
    j=4
    while j>i:
        print("#",end="")
        j=j-1

    print()
    i=i+1