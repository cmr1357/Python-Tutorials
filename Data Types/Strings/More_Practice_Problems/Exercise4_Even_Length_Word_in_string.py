str1=input("Enter the string")

word=str1.split(" ")

for i in word:
    if len(i)%2 == 0:
        print(i)
