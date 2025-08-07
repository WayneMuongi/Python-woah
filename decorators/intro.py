#takes a function as an arguement 
def my_deco(func):
    def wrapper():
        print("China is calling")
        func()
        print("Sichuan University")

    return wrapper    

@my_deco
def hello():
    print("Hello China")

@my_deco
def results():
    print("A plain grade attained")



results()
hello()
