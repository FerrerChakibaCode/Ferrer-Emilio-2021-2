class Jugador:
  inventory = {}
  def __init__(self, username, password, age, avatar, record, inventory):
    self.username = username
    self.password = password
    self.age = age
    self.avatar = avatar
    self.record = record
    self.inventory = inventory
    