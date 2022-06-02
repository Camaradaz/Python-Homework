usuarios = []
usuarios_asteriscos = []
 
cantidad = int(input("Ingrese la cantidad de usuarios de la Academia Club del Código: "))
 
for x in range(cantidad):
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    #usuarios.append((nombre,apellido))
    contrasena = input("Ingrese una contraseña, la cuál debe tener 8 ó más caracteres: ")
 
    mail = (nombre.lower()[0]+apellido.lower()+"@clubdelcodigo.com.ar")
 
    usuarios.append(("Usuario: "+nombre + " " + apellido + " - " + "Mail: " + mail + " - " + "Contraseña: " + contrasena))
    usuarios_asteriscos.append(("Usuario: " + nombre + " " + apellido  + " - " + "Mail: " + mail + " - " + "Contraseña: ",len(contrasena)*"*"))
 
    while len(contrasena) < 8:
        print("Error, la contraseña debe tener como mínimo 8 caracteres.")
        contrasena = input("Ingrese una contraseña, la cuál debe tener 8 ó más caracteres: ")
 
op = input("Desea mostrar las contraseñas, si/no?: ")
 
for x in range(cantidad):
 
    if op == "si":
        print(usuarios[x])
    elif op == "no":
        print(usuarios_asteriscos[x])

usuarios = [('nombre', 'correo'),('nombre1', 'correo1')]
 
# Mapeo de correos a una lista
correos = list(map(lambda x: x[1], usuarios))
 
if 'correo' in correos:
    pos = correos.index('correo')
    usuario = (usuarios[pos][0], 'nuevo correo')
    usuarios[pos] = usuario
