#Convert two lists into a dictionary
#Method1-UsingZipmethod
Key=["January","February","March"]
values=[1,2,3]

dictionary=dict(zip(Key,values))
print(dictionary)

#Method2 using loop and update method
dict2=dict()

for i in range(len(Key)):
    dict2.update({Key[i]:values[i]})
print(dict2)
    