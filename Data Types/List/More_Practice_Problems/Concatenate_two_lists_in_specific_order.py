##Concatenate two lists in specific order
list1=["Hello","Dear"]
list2=["Jack","Peter"]

list1=[x+y for x in list1 for y in list2]

print(list1)
