#initiate a class
class employee:
    #special method/magic method/Dunder methood - constructor
    def __init__(self):
        print("Started executing attributes/data")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("attrributes/data have been initiated")


    def travel(self, destination):
        print("This travel function was called manually")
        print(f"Employee is now traveling to {destination} ")    





#creating  an object/instance of the class 
sam = employee()
#print(sam.id)
#printing the attributes 
#calling a method
sam.travel("Ooty")

print(type(sam))
