from app import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(64))
  tasks = db.relationship("Task", backref="user", lazy="dynamic")

  def __repr__(self):
    return f"<User {self.username}>"

class Task(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(140))
  description = db.Column(db.Text())
  done = db.Column(db.Boolean, default=False)
  user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

  def __repr__(self):
    return f"<Task {self.title}>"