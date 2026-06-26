# Contexto

# Una biblioteca necesita un programa para administrar los libros disponibles.
# Cada libro debe ser representado usando un diccionario,
# y todos los libros deben guardarse dentro de una lista.
# Al ignresar un libro, este tiene el atributo Prestado False, por defecto.
# El autor debe tener al menos nombre y apellido


def validartitulo(titulo):
    # mi titulo debe tener mas de 3 letras.
    if len(titulo) > 3:
        print("Titulo aceptado")
        return True
    else:
        print("Titulo invalido")
        return False


def validarautor(autor):
    return True


def validargenero(autor):
    return True


def validaraño(autor):
    return True


def validarcalificacion(autor):
    return True


inputs = ["1.- Ingresar libro",
          "2.- Eliminar libro",
          "3.- Cambiar estado de préstamo",
          "4.- Mostrar todos los libros",
          "5.- Mostrar solo los títulos",
          "6.- Mostrar libros disponibles",
          "7.- Mostrar libro mejor calificado",
          "8.- Contar libros por género",
          "9.- Salir"]

Libros = [
    {
        "titulo": "El principito",
        "autor": "Antoine de Saint-Exupéry",
        "genero": "Novela",
        "año": 1943,
        "prestado": False,
        "calificacion": 9.2},
    {
        "titulo": "Harry Potter y la piedra filosofal",
        "autor": "J. K. Rowling",
        "genero": "Fantasía",
        "año": 1997,
        "prestado": True,
        "calificacion": 8.8},
    {
        "titulo": "Papelucho",
        "autor": "Marcela Paz",
        "genero": "Infantil",
        "año": 1947,
        "prestado": False,
        "calificacion": 8.5}
    ]

print("Bienvenido!")
while True:
    print("En que lo puedo ayudar hoy?")
    for i in inputs:
        print(i)
    opcion = int(input("Escoga una opcion: "))
    if opcion == 1:  # Ingrese libro
        print("Ingresar Libro...")
        libro = {}
        titulo = input("Ingrese titulo del libro: ")
        if validartitulo(titulo) == True:
            libro["titulo"] = titulo
            autor = input("Ingrese autor del libro: ")
            if validarautor(autor) == True:
                libro["autor"] = autor
                genero = input("Ingrese genero del libro: ")
                if validargenero(genero) == True:
                    libro["genero"] = genero
                    año = int(input("Ingrese año del libro: "))
                    if validaraño(año) == True:
                        libro["año"] = año
                        libro["prestado"] = False
                        calificacion = float(input("Ingrese la calificacion del libro: "))
                        if validarcalificacion(calificacion) == True:
                            libro["calificacion"] = calificacion
                            Libros.append(libro)
                            print("Se ha registrado con exito tu libro!")
                            print(libro)
        else:
            print("No se pudo ingresar el Libro")

    elif opcion == 2:  # Eliminar libro"
        print ("Ingrese el nombre de el libro que desea eliminar....")
        libro= {}
        libro_eliminar= input("escriba el nombre del libro que desea eliminar: ")
        for libro in Libros:
            i
        
            










    elif opcion == 3:  # Cambiar estado de préstamo
        pass
    elif opcion == 4:  # Mostrar todos los libros
        pass
    elif opcion == 5:  # Mostrar solo los títulos
        pass
    elif opcion == 6:  # Mostrar libros disponibles (Los que tengan prestado false)
        pass
    elif opcion == 7:  # Mostrar libro mejor calificado
        pass
    elif opcion == 8:  # Contar libros por género
        pass
    elif opcion == 9:  # Salir
        print("Hasta Luego!")
        break
    else:
        print("Opcion invalida")
ejercicio.py