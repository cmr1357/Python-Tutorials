num=int(input("Enter a number"))

sum=0
i=0
while(num!=0):
    sum=sum+num
    num=num-1
    i=i+1
print("sum=",sum);
average=sum/i
print("Average=",average);
