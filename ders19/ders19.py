# OOP:
# Soyutlama (Abstraction) ✅
# Kapsülleme (Encapsulation) ✅
# Miras Alma (Inheritance) ✅
# Çok Biçimlilik (Polymorphism)


# class Car():

#     # yapici metot, initialize method, constructor method
#     def __init__(self,model,color):
#         # attribute - ozellik
#         self.model = model
#         self.color = color

# toyota_chr = Car('chr','red')
# toyota_chr.engine = 1.3
# toyota_chr.model = 'corolla'

# print(toyota_chr.model)



# ------------------------------------

# public => variable (Fully accessible from anywhere)
# protected => _variable (Is for developers to know should only access inside class or subclass) still allows so not enfored.
# private => __variable ,(is to prevent from accidential access ) outside of class: only accessible with special method.


# class Car():

#     # yapici metot, initialize method, constructor method
#     def __init__(self,model,color,engine):
#         # attribute - ozellik
#         self.model = model
#         self.color = color
#         self.__engine = engine

#     def engine_getter(self):
#         return self.__engine
    
#     def engine_setter(self,new_value):
#         self.__engine = new_value

# toyota_chr = Car('chr','red',1.6)
# porsche = Car('GT2','blue',3.8)

# porsche.engine_setter("4.0")

# print(toyota_chr.engine_getter())
# print(porsche.engine_getter())


# -----------------------------------------

# class BankAccount:
#     def __init__(self,owner,balance):
#         self.owner = owner
#         self.__balance = balance

#     def deposit(self,amount):
#         if amount > 0:
#             self.__balance += amount
#             print(f"deposited {amount}. new balance is {self.__balance}")
#         else:
#             print("deposit amount must be positive")
            
#     def __apply_interest(self):
#         self.__balance *= 1.02
#         return self.__balance
    
#     def get_balance(self):
#         self.__apply_interest()
#         return self.__balance
    
# account = BankAccount('Nova',1000)
# account.deposit(-100)
# # print('apply interest',account._BankAccount__apply_interest()) # bunu dogrudan kullanmak yanlis bir sey.

# print(account.get_balance())

# # deposited 100. new balance is 1100
# # apply interest 1122.0
# # 1144.44


# -----------------------------------------
# Miras Alma (Inheritance)


class Employees:
    def __init__(self,name,surname,age,email):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email


class Teachers(Employees):
    def __init__(self, name, surname, age, email,courses):
        super().__init__(name, surname, age, email)
        
        self.courses = courses


class Student(Employees):
    def __init__(self, name, surname, age, email,ortalama):
        Employees.__init__(self,name, surname, age, email)
        
        self.ortalama= ortalama


mudur = Employees('ahmet','gumus','50','ahmetgumus@nova.com')
ebg = Teachers('erfan','bahcivan','27','ebgdev@proton.me',['python','js','java'])
sevval = Student('sevval','unceli','20','sevval@proton.me',3.5)

print(mudur)
print(ebg)
print(sevval)

print(sevval.ortalama)