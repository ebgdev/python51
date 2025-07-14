# class Parent:
#     pass

# class Child(Parent):
#     pass


# new_kid = Child()

# print(new_kid)

# print(isinstance(new_kid,Child))
# print(isinstance(new_kid,Parent))

# print("alt sinifi mi 1 ?",issubclass(Child,Parent))
# print("alt sinifi mi 2 ?",issubclass(Parent,Child))

# print("alt sinifi mi 3 ?",issubclass(new_kid,Child)) # Hata verir , her iki argumanda sinif olmak zorunda.

# var = True

# print(isinstance(var,bool))

# --------------------------------
# polymorphism (miras-alma)
# DRY : Dont Repeat Yourself

# class User:

#     def sign_in(self):
#         return "logged in"
    
#     # instance method
#     def konus(self):
#         return(f"user sinifindan uretilen obje konusur")

# class Ogrenci(User):
#     def __init__(self,name,gereksinim):
#         self.name = name
#         self.gereksinim = gereksinim

#     def konus(self):
#         return f"bir ogrencinin gereksinimi: \n-lise seviyesi \n-en az {self.gereksinim*1} saat calismasi"
    

# class Ogretmen(User):
#     def __init__(self,name,gereksinim):
#         self.name = name
#         self.gereksinim = gereksinim

#     def konus(self):
#         # ister miras aliriz , ister farkli bicim tanimlariz
#         # return super().konus()
#         # return User.konus(self)
#         return f"bir ogretmenin gereksinimi: \n-lisans seviyesi \n-en az {self.gereksinim*2} saat calismasi"
    
# user1 = User()
# ogrenci1 = Ogrenci('sena',4)
# ogretmen1 = Ogretmen('erfan',4)

# def user_speak(obj):
#     return obj.konus()

# print('ogrenci1:',user_speak(ogrenci1))
# print("--------")
# print('ogretmen1:',user_speak(ogretmen1))
# print("--------")
# print('user1:',user_speak(user1))
# print("--------")
# # print(ogrenci1.konus())


# --------------------------------------

# class User:

#     # initialize method , constructor method (TR: Yapici metot)
#     def __init__(self,email) -> None:
#         # attribute - ozellik --> email
#         self.email = email

#     def sign_in(self):
#         return('logged in')
    
#     # def konus(self):
#     #     print(f"User sinifindan uretilen obje konusur")

# class Ogrenci(User):
#     def __init__(self,name,gereksinim,email) -> None:
#         User.__init__(self,email)
#         self.name = name
#         self.gereksinim = gereksinim

#     def konus(self):
#         # User.konus(self)
#         return f"bir ogrencinin gereksinimi: \n-lise seviyesi\n-en az {self.gereksinim*1} saat calismasi."

# class Ogretmen(User):
#     def __init__(self,name,gereksinim,email) -> None:
#         super().__init__(email)
#         self.name = name
#         self.gereksinim = gereksinim

#     def konus(self):
#         return f"bir ogretmenin gereksinimi: \n-lisans seviyesi\n-en az {self.gereksinim*2} saat calismasi."


# ogrenci1 = Ogrenci("fatih",5,"fatih.stu.nova@gmail.com")
# ogretmen1 = Ogretmen("erfan",5,"erfan.nova@gmail.com")


# print(ogretmen1.konus())
# print(ogrenci1.email)
# print(ogretmen1.email)



# -------------------dunder-methods-------------------
# magic methods
# double underscore methods

# __main__
# __name__
# __init__
# __dir__

# name = 'damla'
# print(type(name))

# print(dir(name))
# print(len(dir(name)))


# num = 11
# print(type(num))

# print(len(dir(num)))


# my_tuple = (1,)
# my_list = [1]
# print(type(my_tuple))
# print(type(my_list))

# print(len(dir(my_tuple)))
# print(len(dir(my_list)))


# print(id(my_tuple))
# print(id(my_list))

# ----------------------

class Toy():
    def __init__(self,color,age):
        self.color = color
        self.age = age
        

action_figure = Toy('red',0)
print(action_figure)

print(action_figure.__str__)
print(action_figure.__str__())

# print(dir(action_figure))