from webserver.models import User as UserModel

class User:
  def __init__(self):
    pass

  def get_user(self, id):
    if id == "1":
      return UserModel(id=id, name="Raka", email="raka@email.com")
    else:
      return UserModel(id=id, name=f"Roko_{id}", email=f"roko_{id}@email.com")

  def get_last_users(self):
    return [UserModel(id=id, name="Raka", email="raka@email.com")]

  async def create_user(self, name, email):
    return UserModel(id=100, name="Raka", email=email)

