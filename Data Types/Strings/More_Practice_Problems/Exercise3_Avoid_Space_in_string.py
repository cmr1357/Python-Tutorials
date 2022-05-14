#Avoiding space in string
str1="heloo o o o o o 0 0 0 0"

res=sum( i.isspace()for i in str1)
print(res)
res=sum(not i.isspace()for i in str1)
print(res)
print(str(res))