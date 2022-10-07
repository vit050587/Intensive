class Animal:
    name = 'Name'
    __age = 0

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value > 0:
            self.__age = value
        else:
            print('Wrong data')

    # age = property(fget=get_age, fset=set_age)

    @classmethod
    def info(cls):
        print(cls.name, cls.__age)
        cls.voice()

    def voice(self):
        print('Voice')

    @staticmethod
    def eat():
        Animal.__age += 10
        print('Eating')


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def voice(self):
        super().voice()
        print('Meow')

    @staticmethod
    def eat():
        print('Eating2')

    def info(self):
        print(self.name, self.age, self.color)


class Dog(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def voice(self):
        super().voice()
        print('Woof')

    @staticmethod
    def eat():
        print('Eating3')

    def info(self):
        print(self.name, self.age)

    # def __repr__(self):
    #     return self.name + ' ' + str(self.age) + ' ' + self.color

    def __str__(self):
        return self.name + ' ' + str(self.age) + ' ' + self.color


# cat = Animal(name='Vaska', age=3)
# dog = Animal(name='Reks', age=5)

cat = Cat(name='Vaska', age=3, color='red')
dog = Dog(name='Reks', age=5, color='black')
print(cat.__dict__)
