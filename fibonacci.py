
n=int(input("Enter a digit to find the nth fibonacci number:"))
a=0
b=1
c=0
if n<0:
    print("Enter a positive Number :")
else :
    print("%d \n%d"%(a,b))
    for i in range(3,n+1):
        c=a+b
        a,b=b,c
        print(c)
