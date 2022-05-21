#Remove empty string from list
list1=["apple","","orange","pineapple","","cherry",""]

#filer() function to remove None type from the list and converted result into list
#list1=list(filter(None,list1))
#print(list1)

while "" in list1:
    list1.remove("")
    
print(list1)