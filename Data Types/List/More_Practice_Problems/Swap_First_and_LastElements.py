##Swap first and Last Element of List
newlist=[12,13,14,15,16]
print("Befor swapping")
print(newlist)
length=int(len(newlist))
temp=newlist[0]
newlist[0]=newlist[length-1]
newlist[length-1]=temp

print("After swapping")
print(newlist)

