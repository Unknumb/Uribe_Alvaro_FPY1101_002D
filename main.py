#importacion de funciones y declaracion de listas
import funciones as funcion
matrizLibros=funcion.matrizLibros;
eleccionSalir=0
#while que mantiene el bucle hasta que se seleccione la opcion salir
while True:
    #Menu interactivo de opciones para agregar lo deseado
    print("\nLibreria");

    print("\n1. Agregar un libro")
    print("2. Ver todos los libros")
    print("3. Modificar un libro")
    print("4. Eliminar un libro.")
    print("5. Guardar colección en un archivo")
    print("6. Salir del programa")
    while True:
        eleccionMenu=input("\nOpción -> ");

        if eleccionMenu in ["1","2","3","4",'5','6']:
            break
        else:
            print("Opción invalida")
#llamado de la primera opcion ejecutando la funcion con parametro para agregar libro
    if eleccionMenu=="1":
        funcion.agregarLibritos(matrizLibros)
#llamado a la segunda funcion 
    elif eleccionMenu=="2":
        print("")
        funcion.mostrarLibros(matrizLibros)
#llamado a la tercera funcion
    elif eleccionMenu=="3":
        funcion.modificarlibro(matrizLibros)
#llamado a la cuarta funcion        
    elif eleccionMenu=='4':
        funcion.eliminarlibro(matrizLibros)
#llamado a la quinta funcion
    elif eleccionMenu=='5':
        funcion.guardarlibroe(matrizLibros)
#llamado a la sexta funcion y termino del ciclo while
    elif eleccionMenu=="6":
        while True:
           #pregunta de confirmacion de cierre del menu
            eleccionSalir=input("¿Está seguro qué desea salir?\n1. Sí\n2. No\n\nOpción -> ");
            if eleccionSalir in ["1","2"]:
                break
            else:
                print("Opción invalida")

    if eleccionSalir=="1":
        break