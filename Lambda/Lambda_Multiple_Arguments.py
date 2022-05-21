#Lambda

x=lambda a,b:a+b

print(x(4,5))

def function1(n):
    return lambda a:a*n

y=function1(2)

print(y(5))