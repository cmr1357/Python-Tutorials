#Change the value of key in a nested dictionary

dict1={'emp1':{'name':'john','salary':7000},
       'emp2':{'name':'Rani','salary':8000},
       'emp3':{'name':'peter','salary':71000}}

dict1['emp3']['salary']=8500

print(dict1)