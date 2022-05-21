##Amstrong Number


def amstrong(): 

    num=input("Enter your number")

    power=len(num)
    result=0;

    num=int(num)
    temp=num

    while num !=0:

        result =result + (num%10)**power

        num=num//10

    if result == temp:

        print("The number you entered is an Amstrong number")
    else:

        print("not an amstrong number")



def main(): 
        
           amstrong()  

    
    
if __name__ =="__main__":
        main()
