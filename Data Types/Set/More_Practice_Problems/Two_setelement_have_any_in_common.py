#Check if two set have any element in common
set1={1,2,3,4,5,6,7,8,9}
set2={10,20,30,40,50,60,70,8,90}

#disjoint -Two set are sed to be disjoint if they do not have any common element

if set1.isdisjoint(set2):
    print("Two sets have no item in common")
else:
    print("Two sets have items in common")
    print(set1.intersection(set2))
