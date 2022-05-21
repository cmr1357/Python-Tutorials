#Factorial of a number

num=int(input("Enter the number: "));
fact=1

if num == 0:
    print("Factorial of the given number is 1")

while num !=0:

    fact=fact * num
    num=num-1;

print("Factorial of the given number is ", fact);
        


