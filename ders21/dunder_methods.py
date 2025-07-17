# # Dunder , magic method
# # Double Underscore methods = Dunder methods

# class Toy:
#     def __init__(self,color,age):
#         self.color = color
#         self.age = age

#     def __str__(self):
#         return f'toy color: {self.color} and toy age: {self.age} , id: {id(self)}'



# action_figure = Toy('Red',1)
# action_figure2 = Toy('White',20)

# # print(action_figure)
# # print(action_figure.__str__())
# # print(action_figure.__str__) # <bound method Toy.__str__ ...
# # print(str(action_figure))
# # print(str(action_figure2))


# print(action_figure)
# print(action_figure2)


# ----------------------------------

# class Language:
#     def __init__(self,author,age, name):
#         self.author = author
#         self.age = age
#         self.name = name
#         self.frameworks = {
#             'Web': 'Django',
#             'API' : "FastAPI"
#         }

#     def __str__(self):
#         return f"Author: {self.author} , age: {self.age} , name: {self.name}"
    
#     def __repr__(self):
#         pass
    
#     def __len__(self):
#         return len(self.author)
    
#     def __call__(self):
#         return "obje fonksiyon gibi cagirilir"
    
#     def __getitem__(self,key):
#         return self.frameworks[key]
    

# python = Language("Guido van Rossum",35,'Python')

# print(python)
# print(len(python))
# print(python())

# print(python['Web'])
# print(python['API'])

