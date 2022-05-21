n=int(input("Enter the number"))

i=0
j=0

while i<=n:
    if i%2 == 0:
        j=j+1
    i=i+1
if j == 2:
    print("prime")
else:
    print("not prime")