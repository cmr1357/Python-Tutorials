#Join Two List

list1=["Apple","Banana","Orange","Mango"]
list2=[1,2,3,4,5]

list3=list1+list2
print(list3)


#Using append method
for x in list2:
    list1.append(x)
print(list1)


#using extend method

list2.extend(list3)
print(list2)
