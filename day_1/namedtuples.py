from collections import namedtuple

Person = namedtuple("Person", "name age job_title is_vegetarian")

person_1 = Person("Zsolt", 31, "instructor", False)
person_2 = Person("Eugene", 28, "instructor", False)


print(person_1.name)
print(person_2.age)