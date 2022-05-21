#Delete a list of keys from a dictionary
dict1={"Name":"John","Age":25,"Salary":8000,"City":"New york"}

keys=["Name","Salary"]

for k in keys:
    dict1.pop(k)
print(dict1)