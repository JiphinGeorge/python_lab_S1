a=int(input("Enter a Digit to Find the Factorial ,  :"))
fact=1
if a<0:
    print("Enter a Positive Digit! ")
elif a==1 or a==0:
    print("Enter a digit Greater than 1")
else:
    for i in range(1,a+1):
        fact*=i
    print("Factorial of %d is %d"%(a,fact))

