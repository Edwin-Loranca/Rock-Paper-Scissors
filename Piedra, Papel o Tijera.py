'Piedra, Papel o Tijera'

import random

options = ('Piedra', 'Papel', 'Tijera')

print('*' * 54)
print('== BIENVENIDO AL JUEGO DE PIEDRA - PAPEL - TIJERA ==')
print('*' * 54)

marc_usuario = 0
marc_cpu = 0



while (marc_usuario < 2) and (marc_cpu < 2):

    usuario = input('|-----------------|\n'
                    '|  =>  Piedra <=  |\n'
                    '|  =>  Papel  <=  |\n'
                    '|  =>  Tijera <=  |\n' 
                    '|-----------------|\n'
                    'Elige una opción: ')
    print('                 --------')

    new_usuario = usuario.capitalize()
    if not new_usuario in options:
        print ('Opción invalida...')
        exit ()
        
    cpu = random.choice(options)

    print('*' * 50)

    print('Tu Elegiste:', new_usuario)
    print('La computadora escogio:',cpu)

    if new_usuario == cpu :
        print('Es Empate...')
        print ('  MARCADOR:','\n',
            '|*****************|','\n',
            '|  Usuario:', marc_usuario, '    |','\n',
            '|  Computadora:', marc_cpu, '|','\n'
            ' |*****************|')

    elif new_usuario == 'Piedra' and cpu == 'Tijera':
        print('Has Ganado!!')
        marc_usuario = marc_usuario + 1
        print ('  MARCADOR:','\n',
            '|*****************|','\n'
            ' |  Usuario:', marc_usuario, '    |','\n',
            '|  Computadora:', marc_cpu, '|','\n'
            ' |*****************|')

    elif new_usuario == 'Papel' and cpu == 'Piedra':
        print ('Has Ganado!!')
        marc_usuario = marc_usuario + 1
        print ('  MARCADOR:','\n',
            '|*****************|','\n'
            ' |  Usuario:', marc_usuario, '    |','\n',
            '|  Computadora:', marc_cpu, '|','\n'
            ' |*****************|')

    elif new_usuario == 'Tijera' and cpu == 'Papel':
        print('Has Ganado!!')
        marc_usuario = marc_usuario + 1
        print ('  MARCADOR:','\n',
            '|*****************|','\n'
            ' |  Usuario:', marc_usuario, '    |','\n',
            '|  Computadora:', marc_cpu, '|','\n'
            ' |*****************|')

    else:
        print ('Has perdido...')
        marc_cpu = marc_cpu + 1
        print ('  MARCADOR:','\n',
            '|*****************|','\n'
            ' |  Usuario:', marc_usuario, '    |','\n',
            '|  Computadora:', marc_cpu, '|','\n'
            ' |*****************|')
        

if (marc_usuario == 2) and (marc_cpu < 2 )  :
    print ('Felicidades, usuario gana 2 de 3')
else:
    print ('Felicidades, cumputadora gana 2 de 3')
