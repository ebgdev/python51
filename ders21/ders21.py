from side import Pet

class Dog(Pet):
    def __init__(self,name,age,weight):
        super().__init__(name,age,weight)

    def speak(self):
        # return super().speak()
        return f"My dog {self.name} can do hav hav"

dog = Dog('alex', 3, '10')



class Cat(Pet):
    def __init__(self,name,age,weight):
        super().__init__(name,age,weight)

    # def speak(self):
        # return super().speak()
        # return f"My cat {self.name} which is {self.age} years old can do miav miav"

if __name__ == "__main__":

    cat = Cat('elsa',2,'5')
    print(dog.speak())
    print(cat.speak())