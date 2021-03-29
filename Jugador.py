class Jugador:
  inventory = {}
  record = {}
  def __init__(self, username, password, age, avatar, record, inventory, clues):
    self.username = username
    self.password = password
    self.age = age
    self.avatar = avatar
    self.record = record
    self.inventory = inventory
    self.clues = clues