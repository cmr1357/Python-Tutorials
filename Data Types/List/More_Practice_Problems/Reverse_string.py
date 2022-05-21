#Reversing a list
#using len method
list=[1,2,3,4,5]
length=len(list)
length=length-1
limit=length/2
for i in range(0,length):
    if length!=limit:
        temp=list[i]
        list[i]=list[length]
        list[length]=temp
        length=length-1

print(list)