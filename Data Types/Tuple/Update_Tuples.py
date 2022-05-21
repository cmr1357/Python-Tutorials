#Change Tuple

tuple1=("Apple","Banana","Orange","Cherry")

tuple2=list(tuple1)

tuple2[1]="Kiwi"

tuple1=tuple(tuple2)

print(tuple1)



#Add Items

tuple1=("Apple","Banana","Orange","Cherry")
tuple2=list(tuple1)
tuple2.append("Mango")
tuple1=tuple(tuple2)

print(tuple1)


#Add tuple to a tuple

tuple1=("Apple","Orange","Banana")
tuple2=("Mango",)

tuple1 += tuple2
print(tuple1)