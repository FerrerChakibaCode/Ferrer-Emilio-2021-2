import matplotlib.pyplot as plt



class Estadistica:
  def __init__(self, users_db):
    self.users_db = users_db

  # def mostrar_users_db(self):
  #   data
  #   for user in range(len(self.users_db)):
  #     records.append(self.users_db[list(self.users_db.keys())[user]])

  def plays_the_most(self):
    data = []
    records = []
    for user in range(len(self.users_db)):
      data.append(self.users_db[list(self.users_db.keys())[user]])
    labels = [data[x][0] for x in range(len(data))]
    values = [sum(data[x][-1]) for x in range(len(data))]
    print(values)
    # fig1, ax1 = plt.subplots()
    # ax1.pie(values, labels = labels, autopct='%1.1f%%', shadow = True, startangle = 90)
    # ax1.axis('equal')
    plt.axis('equal')
    plt.pie(values, labels = labels, radius = 1.5)

    plt.show()

    