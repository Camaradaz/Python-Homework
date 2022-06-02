def entrarNombre():
    """ funcion para añadir un nombre """
    while True:
        nombre = input("Ingrese el nombre del estudiante a añadir: ")
        if nombre=="":
            print("el nombre no puede estar vacio")
        else:
            return nombre
 
 
def entrarNota():
    """ funcion para añadir una nota """
    while True:
        try:
            nota = float(input("Ingrese la nota del estudiante (0-10):"))
            if 0<=nota<=10:
                return nota
            else:
                print("la nota tiene que estar entre 0 y 10")
        except:
            print("la nota tiene que ser un valor numerico")
 
 
def devolverEstudiante():
    nombre=entrarNombre()
    for el in estudiantes:
        if el[0] == nombre:
            print("La nota del estudiante '{}' es {}".format(nombre, el[1]))
            return True
    print("No se encuentra el estudiante")
    return False
 
 
def modificarNota():
    nombre=entrarNombre()
    indice=buscarEstudiante(nombre)
    if indice==-1:
        print("No se ha encontrado el estudiante '{}'".format(nombre))
        return False
 
    # al no poder modificar un elemento de una tupla, lo convertimos
    # temporamente en una lista.
    tmp=list(estudiantes[indice])
    tmp[1]=entrarNota()
    estudiantes[indice]=tuple(tmp)
    print("Se ha actualizado la nota al estudiante '{}'".format(nombre))
    return True
 
 
def listarEstudiantesNombre():
    estudiantes.sort()
    print("\n".join(i[0]+" - "+str(i[1]) for i in estudiantes))
 
 
def listarEstudiantesNota():
    """ lista los estudiantes ordenados por su nota descendente """
    estudiantes.sort(key=lambda x: x[1], reverse=True)
    print("\n".join(i[0]+" - "+str(i[1]) for i in estudiantes))
 
 
def notaMedia():
    """ funcion para mostrar la nota media de los estudiantes """
    if len(estudiantes)==0:
        print("No hay estudiantes")
        return
 
    media=sum([i[1] for i in estudiantes])/len(estudiantes)
    print("La nota media de todos los estudiantes es '{}'".format(media))
 
 
def borrarEstudiante():
    """ funcion para borrar un estudiante """
    nombre=entrarNombre()
    indice=buscarEstudiante(nombre)
    if indice==-1:
        print("No se ha encontrado el estudiante '{}'".format(nombre))
        return False
 
    print("Se ha eliminado el estudiante '{}' con nota {}".format(nombre, estudiantes[indice][1]))
    del estudiantes[indice]
    return True
 
 
def buscarEstudiante(nombre):
    """
    Funcion que devuelve el indice de un estudiante en la lista
    Devuelve -1 si no ha encontrado el estudiante
    """
    for i,e in enumerate(estudiantes):
        if e[0]==nombre:
            return i
    return -1
 
 
def Menú():
    print("---------------------------------------------------------------")
    print ("Selecciona una opción...")
    print ("\t1 - Añadir estudiante")
    print ("\t2 - Buscar estudiante")
    print ("\t3 - Modificar nota")
    print ("\t4 - Listado de los estudiantes ordenador por el nombre")
    print ("\t5 - Listado de los estudiantes ordenador por su nota")
    print ("\t6 - Mostrar la media de las notas")
    print ("\t7 - Borrar un estudiante")
    print ("\n\t0 - Salir")
 
# definimos la lista que contendra una lista con cada estudiante
estudiantes=[]
 
while True:
    Menú ()
 
    try:
        opcion = int(input("Ingrese el número de la opción escogida: "))
    except:
        opcion=-1
 
    if opcion == 1:
        estudiantes.append((entrarNombre(), entrarNota()))
    elif opcion == 2:
        devolverEstudiante()
    elif opcion == 3:
        modificarNota()
    elif opcion == 4:
        listarEstudiantesNombre()
    elif opcion == 5:
        listarEstudiantesNota()
    elif opcion == 6:
        notaMedia()
    elif opcion == 7:
        borrarEstudiante()
    elif opcion == 0:
        break
    else:
        print("La opción ingresada no es correcta, indica una opción correcta")
