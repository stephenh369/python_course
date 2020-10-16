from pprint import pprint as print

user = {
  "name": "Zsolt",
  "age": 31,
  "pets": [
    {"name": "Zelda", "type": "Hedgehog"},
    {"name": "Django", "type": "Dog"},
    {"name": "Yoda", "type": "Bearded Dragon"}
  ],
  "lucky_numbers": [3,6,9,12,27]
}
user2 = {"name": "Eugene", "age": 28}
print(user)
print(user2)

user["email"] = "example@codeclan.com"

print(list(user.keys())[0])
print(user["name"])

del(user["age"])
print(user)