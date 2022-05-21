#update the first set with items that don't exist in second set
set1={10,20,30}
set2={10,20,40}
set1.difference_update(set2)
print(set1)
