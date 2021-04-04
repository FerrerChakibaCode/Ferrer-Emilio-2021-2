class Player:
  def __init__(self, username, password, age, avatar, difficulty, lives, clues, time, inventory, record):
    
    self.username = username
    self.password = password
    self.age = age
    self.avatar = avatar
    self.record = []
    self.difficulty = difficulty
    self.lives = lives
    self.clues = clues
    self.time = time
    self.inventory = inventory
    
  
  def show(self):
    return f'''USERNAME -> {self.username}
EDAD -> {self.age}
AVATAR -> {self.avatar}
VIDAS -> {self.lives}
PISTAS -> {self.clues}
INVENTARIO -> {self.inventory}
TIEMPO -> {self.time}
'''
# RECORD -> {self.record}
