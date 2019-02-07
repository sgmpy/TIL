class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print(self.name + '안녕!')

    # @classmethod
    # def greeting(cls):
    #     pass

    # @staticmethod
    # def greeting():
    #     pass

p1 = Person('junwoo', 40)
p1.greeting()





class Passport:
    def __init__(self, person):
        self.person = person

# pp = Passport(p1)
# print(pp.person.age)