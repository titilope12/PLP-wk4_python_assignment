class Person:
    name = "Victor"
    age = 25
    gender = "male"
    def introduce(self):
        print("My name is " + self.name)
        print("I am " + str(self.age) + " years old")
        print("I am a " + self.gender)

p1 = Person()
p1.introduce()