class employee:
    def __init__(self,name,ID,department):
        self.name=name
        self.ID=ID
        self.department=department
        
class software(employee):
    pass

software_programmer=software("Chithra",2018,"developer")

print(type(software_programmer))
        
        