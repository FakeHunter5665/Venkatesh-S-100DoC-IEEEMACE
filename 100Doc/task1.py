A=input("enter the string:")
B=" "
for i in A:
    i=i.lower()
    if i.isalpha():
        a= ord(i)-96
        B=B+str(a)+" "
print(B)
