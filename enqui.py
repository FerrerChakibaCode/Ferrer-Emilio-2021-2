import enquiries
import graficos

opciones_victor = [f'{graficos.ahorcado_muerto}', 'matar a python', 'rica awita']
elegir = enquiries.choose('Que deseas hacer?', opciones_victor)

if elegir == opciones_victor[0]:
  print('alto ahorcado')

elif elegir == 'matar a python':
  print('error')

elif elegir == 'rica awita':
  print('aaaa')