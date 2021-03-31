class Player:
  def __init__(self, username, password, age, avatar, lives, clues, inventory = []): #TODO ver cómo guardar record en el .txt
    self.username = username
    self.password = password
    self.age = age
    self.avatar = avatar
    # self.record = record
    self.lives = lives
    self.clues = clues
    self.inventory = inventory
  
  def show(self):
    print(f'''USERNAME -> {self.username}
EDAD -> {self.age}
AVATAR -> {self.avatar}
VIDAS -> {self.lives}
PISTAS -> {self.clues}
INVENTARIO -> {self.inventory}
''')
# RECORD -> {self.record}
