# -------------------------------------------------------
# # OPP : NYP
# # Pascal Case

# import uuid

# class Employess():

#     # class attribute
#     class_counter = 0

#     def __init__(self,name,surname,birth_date):
#         self.name = name
#         self.surname = surname
#         self.birth_date = birth_date
#         # hidden attribute
#         self.email = f"{name+surname}@novaakademi.com"
#         self.id = uuid.uuid1()
#         Employess.class_counter += 1

#     # instance method
#     def p_info(self):
#         return f"name {self.name} ,surname:{self.surname} ,birth:{self.birth_date}, email:{self.email} id:{self.id}"
    

# py_hoca = Employess('erfan','bahcivan','1997')
# print(py_hoca.email)
# print(py_hoca.id)


# junior_hocasi = Employess('seda','gumus','2000')
# print(junior_hocasi.p_info())

# print(Employess.class_counter)


# -------------------------------------------------------
# static methods

# class Apple:
#     def __init__(self,model):
#         self.model = model

#     @staticmethod
#     def about_apple():
#         print("Apple Inc. is a tech company")

# Apple.about_apple()
# iphone = Apple("iphone5")
# iphone.about_apple()


# --------------------------------------------------------

# class Person:

#     obj_counter = 0

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         Person.obj_counter += 1

#     @classmethod
#     def get_with_str(cls,astr):
#         name , age = astr.split(',')
#         return cls(name,age)
    
# person1 = Person('nova',10)

# person2 = Person.get_with_str('mikail,30')

# print(person1.name)
# print(person2.name)

# print(Person.obj_counter)


# --------------------------------------------------------
import datetime

class Person:

    obj_counter = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        Person.obj_counter += 1

    @classmethod
    def get_with_birth_date(cls,astr):
        name, birth_date = astr.split(',')
        age = datetime.datetime.today().year - int(birth_date)
        return cls(name,age)



person1 = Person('nova',10)

person2 = Person.get_with_birth_date('mikail,1990')

print(person1.name)
print(person2.name)
print(person2.age)

print(Person.obj_counter)
