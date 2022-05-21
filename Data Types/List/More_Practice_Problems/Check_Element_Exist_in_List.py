#Check if element exist in list
list=[1,2,3,4,5]
item=int(input("Enter a number"))

if( item in list):
    print(item,"exists")
else:
    print("Item not present")