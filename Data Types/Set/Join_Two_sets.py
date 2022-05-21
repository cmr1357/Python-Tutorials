#Loop Items

set1={"Apple","Orange","Banana"}

for x in set1:
    print(x)
    
set2={1,2,3,4}

set3=set1.union(set2)

print(set3)



set4={1.34,2.14,8.0}

set1.update(set4)
print(set1)