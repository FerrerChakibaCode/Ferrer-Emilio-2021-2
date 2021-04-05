    while ganador == None:
      if n == 0: #Juega primero el user
        for x in range(len(matriz)):
          if matriz[x][0] == 'X' and  matriz[x][1] == 'X' and  matriz[x][2] == 'X':
            ganador = 0
            break
          elif matriz[0][x] == 'X' and  matriz[1][x] == 'X' and  matriz[2][x] == 'X':
            ganador = 0
            break
          elif matriz[x][x] == 'X' and  matriz[x][x] == 'X' and  matriz[x][x] == 'X':
            ganador = 0
            break