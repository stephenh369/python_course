class Person:

  def __init__(self, id, name, age):
    self.__id = id
    self.name = name
    self.age = age

  def talk(self):
    return f"Hi, my name is {self.name}"

person = Person(1, "Charlotte", 45)
person.id = 99
print(person.name)
print(person.id)
print(person.talk())

