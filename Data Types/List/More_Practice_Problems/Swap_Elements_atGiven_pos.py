##Swap elements at given position
newlist=[2,3,4,5,6,10]
pos1=int(input("Enter the first position"))
pos2=int(input("Enter the second position"))

print("Before swapping")
print(newlist)

length=int(len(newlist))
newlist[pos1],newlist[pos2]=newlist[pos2],newlist[pos1]
print("After swapping")
print(newlist)