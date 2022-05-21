#Rename key of a dictionary

dict1={"Name":"John","Age":25,"Salary":8000,"City":"New york"}
dict1["location"]=dict1.pop("City")
print(dict1)