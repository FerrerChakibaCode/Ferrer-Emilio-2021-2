class Player:
  def __init__(self, username, password, age, avatar, lives, clues, inventory = []):
    self.username = username
    self.password = password
    self.age = age
    self.avatar = avatar
    # self.record = record
    self.lives = lives
    self.clues = clues
    self.inventory = inventory
  
  def show(self):
    return '''USERNAME -> {self.username}
EDAD -> {self.age}
AVATAR -> {self.avatar}
VIDAS -> {self.lives}
PISTAS -> {self.clues}
INVENTARIO -> {self.inventory}
'''
# RECORD -> {self.record}
