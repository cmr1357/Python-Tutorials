#pop
dict1={"Color":"Yellow","Item No":123}

dict1.pop("Color")
print(dict1)

#popitem

dict1.popitem()
print(dict1)

#del
dict1={"Color":"Yellow","Item No":123,"Model":"Jade","Amount":1000}
del dict1["Model"]
print(dict1)

dict1.clear()
print(dict1)
