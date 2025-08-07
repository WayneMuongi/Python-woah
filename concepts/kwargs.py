def greet(name,nationality):
    print("Name is",name)
    print("From",nationality)

greet("China","Xi_jinping")
greet(nationality="China",name="Xi_jinping")

#KWARGS PROFILE
def employee(**kwargs):
    print(kwargs)

employee(name="Wayne",age=19,country="china mainland")
employee(name="Ethan",age=10,country="KE")