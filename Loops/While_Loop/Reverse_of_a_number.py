#Reverse of Number

num=int(input("Enter the number you want to reverse"));

reverse=0
temp=num
print(type(num))
while num !=0:
    reverse= reverse *10
    reverse=reverse+(num%10)
    num=num//10
    print(num)

print("Reverse =", reverse)
