# OOPs - > Object oriented programming is a method of the writring the program
# in the classes and objects to connect with the real world intities 
#                 STUDENT
#                   │
#         ┌─────────┴─────────┐
#        Data               Behavior
#          │                   │
#      name = Raju          study()
#      age = 20             attend()
#      roll_no = 027         exam()


# Class 
# a class is a blue print / temple that can be use to creat the objects
#class Student:  -> class name is Student 
#   pass   curently not any thing at the class


# Object 
# Object is an intance of the calss 
#class Student:  -. class is the Student 
#    pass  

# student1 = Student()    -> this object instance of the class   
#             CLASS
#           Student
#              │
#       ┌──────┴──────┐
#       ↓             ↓
#   student1       student2
#    Object          Object

# Let the complete code of the of the class and the object
#class Student: # Create class with the name Student 
#    pass
#Student1=Student() # Create the first object same anemas class name 
#Student2=Student()  # Create the second objcet  same name as the class name
#print(Student1)  
#print(Student2)
#Student class
#     │
#     ├── student1
#     └── student2
#class Student:
#   pass
#Student1=Student()         |
#Student1.name='Raju Kumar' | 
#Student1.age=19            |____  Attributes
#Student1.dept='Software'   |
#                           |
#Student2=Student()
#Student2.name='Inder'
#Student2.age=20
#Student2.dept='Computer Science'

##print(Student1.dept)
#print(Student2.dept)


# Create the class car and print the brand , Model , year
#class Car:
#    pass
#Car1=Car()
#Car1.brand='Civic'
#Car1.model=26
#Car1.year=2026

#Car2=Car()
#Car2.brand='Altu'
#Car2.model=27
##Car2.year=2027

#print(Car1.brand,Car1.model,Car1.year)
#print(Car2.brand,Car2.model,Car2.year)
# Def __int___(slef) -> Function that aautomatically run the code 
#class Car:

#  def __init__(self):
#       print("Car object created")

#Car1 = Car()

# Function
#def greet(name):
#    return "Hello " + name

#greet("Sam")
#name = "sam"
#name.upper()
#print(name)


# Make  a software for the ATM
class Atm:
    def __init__(self):

#        print('Hello')

        self.pin=""
        self.balance=0

        self.menu()

    def menu(self):
     user_input=input("""
                 Hello , How would you like to proceed?
                 1.Enetr 1 to create pin
                 2.Enetr 2 to deposite 
                 3.Enetr 3 to withdraw
                 4.Enetr 4 to check balance 
                 5.Enter 5 to exit 

""")
     if user_input=="1":
         self.check_balance()
     elif user_input=="2":
        self.deposit()
     elif user_input=='3':
        self.withdraw()
     elif user_input=="4":
        self.check_balance()
     else:
        print("Bye")


    def create_pin(self):
       self.pin==input("Enetr your pin ")
       print("Pin set Successfully")

    def deposit(self):
       temp=input("Enetr your pin ")
       if temp==self.pin:
          amount=int(input("Enetr the amount"))
          self.balance=self.balance+amount
          print("Deposte Successful")
       else:
          print("Invalid pin")

    def withdraw(self):

      temp = input("Enetr your pin = ")
      if temp == self.pin:
         amount=int(input("Enetr the amount "))
         if amount<self.balance:
            self.balance = self.balance-amount
            print("Operation is sucessfull")
         else:
            print("Insufficient Funds")

    def check_balance(self):
       temp=input("Enetr your pin")
       if temp==self.pin:
          print(self.balance)
       else:
          print("Invalid pin")

sbi=Atm()

          
    

   



