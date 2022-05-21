def multiply(*numbers):
    print(numbers)
    
    total=1
    
    for number in numbers:
        total=total*number
    print(total)
        
    
multiply(2,3,4,5)
