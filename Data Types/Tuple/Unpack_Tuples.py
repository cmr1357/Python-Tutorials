#Unpack Tuples

tuple1=("Apple","Banana","Orange","Cherry")
(f1,f2,f3,f4)=tuple1

print(f1)
print(f2)
print(f3)
print(f4)


tuple1=("Apple","Banana","Orange","Cherry","Grapes","Watermelon")
(f1,f2,f3,*f4)=tuple1
print(f1)
print(f2)
print(f3)
print(f4)