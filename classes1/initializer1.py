# def deco(yoh):
#     def wrapper(*args,**kwargs):
#         print("The function China is calling")
#         yoh(*args,**kwargs)
#         print("This is a call from sichuan university")
#     return wrapper



# @deco
class Human():

    # @deco
    def __init__(self,name,gender):# initializer is called automatically
        print("The function China is calling")
        # print(gender)
        # print(name)
        self.name=name
        self.gender=gender
        if self.gender =="Male":
            self.ribs = 23
            self.curse ="Suffer"
        else:
            self.ribs=24
            self.curse="Pain"
    # @deco
    def another_one(self,school,age):#you have to call this one individually
        print("This is a call from sichuan university")
        print(school)
        print(age)

wayne=Human(name="Wayne",gender="Male") 
print("name",wayne.name)
print("gender",wayne.gender)
print("ribs",wayne.ribs)
print("curse",wayne.curse)
print("")

shaki=Human(name="Shaki",gender="female")
print("name",shaki.name)
print("gender",shaki.gender)
print("ribs",shaki.ribs)
print("curse",shaki.curse)

#object from a class
#use kwargs to add info
# wayne.__init__()#called automatically

# wayne.another_one(school="Sichuan university",age=19)

