##Swapping of first and last element second method

newlist=[2,3,4,5,6,10]
print("Before swapping")
print(newlist)
length=int(len(newlist))
newlist[0],newlist[length-1]=newlist[length-1],newlist[0]
print("After swapping")
print(newlist)
