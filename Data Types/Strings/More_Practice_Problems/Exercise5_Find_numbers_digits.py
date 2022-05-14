str1=input("Enter your string")
flag1=False
flag2=False
for i in str1:
   if i.isalpha():
   
       flag1=True
    
   if i.isdigit():
       flag2=True
if flag1:
    print("Yep alphabets are their")
if flag2:
    print("Yep numbers are their")
else:
    print("No numbers")
