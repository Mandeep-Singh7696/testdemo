#pattern 3
# i=1
# while i<5:
#     print('#',end="")
#     j=1
#     while j<i:
#         print('#',end="")
#         j=j+1
#     print()
#     i=i+1
#
for i in range(1,5):
    print("#",end="")
    j=1
    for j in range(i-1):
        print("#",end="")
    print()