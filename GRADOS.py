def fahrenheit_celsius():
    '''convierte temperatura en grados fahrenheit a grados celsius'''

    fahrenheit = int(input('Ingrese la temperatura en grados Fahrenheit: '))
    celsius = (fahrenheit -32 ) * 5.0/9.0
    return '{} grados Fahrenheit son {} grados Celsius'.format(fahrenheit, celsius)

def celsius_fahrenheit():
    '''convierte temperatura en grados celsius a fahrenheit'''

    celsius = int(input('Ingrese la temperatura en grados Celsius: '))
    fahrenheit = 9.0/5.0 * celsius +32
    return '{} grados Celsius son {} grados Fahrenheit'.format(fahrenheit, celsius)

while True:
    print('1.- Fahrenheit a Celsius')
    print('2.- Celsius a Fahrenheit')

    try:
        opcion = int(input('Seleccione una opción: '))
        if opcion == 1:
            print(fahrenheit_celsius())
        elif opcion == 2:
            print(celsius_fahrenheit())
        elif opcion == 3:
            print('Hasta luego')
        else:
            raise ValueError
    except ValueError:
        print('Ingrese solo números.(1/2)')
