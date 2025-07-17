class Pet:
    def __init__(self,name,age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def speak(self):
        return f"Pet created: {self.name} is {self.age} years old which is about {self.weight} kg"
    

# __name__
# __main__


if __name__ == "__main__":

    leo = Pet('Leo',2,5)
    print(leo.speak())