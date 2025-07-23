# class Car:
#     # constructor method - yapici method
#     def __init__(self,factory,model,engine,seat, door,vType):
#         self.factory = factory
#         self.model = model
#         self.engine = engine
#         self.seat = seat
#         self.door = door
#         self.vType = vType

#     @classmethod
#     def get_with_str(cls,astr):
#         factory,model,engine,seat,door,vType = astr.split(",")
#         return cls(factory,model,engine,seat,door,vType)
    

# with open("information.txt") as file:
#     lines = file.readlines()

# objects = {}
# for i in range(len(lines)):
#     line = lines[i]
#     objects[f"car{i}"] = Car.get_with_str(line.removesuffix("\n"))

# print(objects["car1"].vType)



# ----------------------------------------


