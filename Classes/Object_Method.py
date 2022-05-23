class employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def function1(self):
        print("hi"+self.name)
p1=employee("Abhinav",16)

print(p1.name)
print(p1.age)
p1.function1()