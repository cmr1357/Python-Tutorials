str1=input("Enter a string")

length=int(len(str1))
half=int(length/2)
str2=str1[half:].upper()

newstr=str1[:half]+str2
print(newstr)