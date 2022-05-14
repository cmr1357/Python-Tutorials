str=input("Enter your string")

half=int(len(str)/2)
print(half)

if half%2 == 0:#even string
    first_half=str[:half]
    second_half=str[half:]
    #check symmetry
    if first_half == second_half:
        print("String is symmetrical")
    else:
        print("String is not symmetrical")
#Palindrome
        print(second_half[::-1])
    if first_half == second_half[::-1]:
        print("palindrome")
    else:
        print("not palindrome")
else:
    print("String is not symmetrical")
    print("not palindrome")




