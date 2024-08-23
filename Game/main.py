import random


def choose_options():
  options = (1, 2, 3)
  user_option = int(input('1.- piedra,\n2.- papel\n3.- tijera \nIngrese el numero correspondiente a su eleccion=> '))
  #user_option = user_option.lower()

  if not user_option in options:
    print('ELIJA SOLO UNA DE LAS 3')
    # continue
    return None, None

  computer_option = random.choice(options) #selecciona una opcion aleatoria choice entre una serie de opciones

  if user_option==1:
    print('User option =>', "piedra")
  elif user_option==2:
    print('User option =>', "papel")
  else:
    print('User option =>', "tijera")
  
  if computer_option==1:
    print('Computer option =>', "piedra")
  elif computer_option==2:
    print('Computer option =>', "papel")
  else:
    print('Computer option =>', "tijera")

  return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins):
  if user_option == computer_option:
    print('Empate!')
  elif user_option == 1:
    if computer_option == 3:
      print('piedra gana a tijera')
      print('user gano!')
      user_wins += 1
    else:
      print('Papel gana a piedra')
      print('computer gano!')
      computer_wins += 1
  elif user_option == 2:
    if computer_option == 1:
      print('papel gana a piedra')
      print('user gano')
      user_wins += 1
    else:
      print('tijera gana a papel')
      print('computer gano!')
      computer_wins += 1
  elif user_option == 3:
    if computer_option == 2:
      print('tijera gana a papel')
      print('user gano!')
      user_wins += 1
    else:
      print('piedra gana a tijera')
      print('computer gano!')
      computer_wins += 1
  return user_wins, computer_wins

def run_game():
  computer_wins = 0
  user_wins = 0  
  rounds = 1
  opcion_salida = ('s','n')

  while True:
    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)

    print('computer_wins', computer_wins)
    print('user_wins', user_wins)
    rounds += 1

    user_option, computer_option = choose_options()
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)

    opcion_salida_manual=input("Desea Seguir Jugando? SI (s) o NO (n)=>")
    opcion_salida_manual=opcion_salida_manual.lower()
    
    if not opcion_salida_manual in opcion_salida:
      print('esa opcion no es valida')

    if opcion_salida_manual == 'n':
      print('computer_wins', computer_wins)
      print('user_wins', user_wins, '\nHasta Luego')
      break

    '''if computer_wins == 2:
      print('El ganador es la computadora')
      break

    if user_wins == 2:
      print('El ganador es el usuario')
      break'''

run_game()