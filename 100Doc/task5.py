def SqrSum():
    a=int(input("enter the total num:"))
    c=0
    for i in range(0,a):
        b=int(input("enter the nums:"))
        c+=b**2
    return c
print(SqrSum())
