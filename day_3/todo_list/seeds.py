from app import db
from app.models import User, Task

Task.query.delete()
User.query.delete()

user1 = User(username="Stephen")
user2 = User(username="Zsolt")
db.session.add(user1)
db.session.add(user2)
db.session.commit()

users = User.query.all()
print(users)

first_user = User.query.get(1)

task1 = Task(title="Learn Python", description="Learn how to code in Python.", done=True, user=first_user)
task2 = Task(title="Buy milk", description="Need it for tea.", done=True, user=first_user)

db.session.add(task1)
db.session.add(task2)
db.session.commit()

