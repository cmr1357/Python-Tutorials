#1.Remove first occurance
list1=['a','b','c','d','e','f','g','h','i','e','g','h','g']

#get the first occuranceindex

index=list1.index('e')

#update item present at location

list1[index]='l'
print(list1)


#2.Replace All occurance
#Using for loop and enumerate()-This function return two list, index number in a list and value in a list

for index,char in enumerate(list1):
    if char == 'g':
        list1[index]='o'
print(list1)
