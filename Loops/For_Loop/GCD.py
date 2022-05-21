##GCD


num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))

if num1>num2:
    small=num1
else:
    small=num2

for i in range(1,small+1):
    if(num1%i == 0) and (num2%i==0):
        gcd=i
print("Gcd of ",num1 ,"and ",num2," = " ,gcd)
