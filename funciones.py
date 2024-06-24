import csv
matrizLibros=[["Titulo","Autor","Año de publicación","Genero"],

];


def agregarLibritos(matrizLibros):
    nuevoLibro = input("\nIngrese el libro que desea agregar: ")
    autorLibro = input("Ingrese el autor del libro: ")
    añoLibro = input("Ingrese el año del libro: ")
    generoLibro = input("Ingrese el genero del libro: ")
    listaLibros = [nuevoLibro, autorLibro, añoLibro, generoLibro]
    matrizLibros.append(listaLibros)

def mostrarLibros(matrizLibros):
    if len(matrizLibros) == 1:
        print("\nNo hay libros para mostrar")
    else: 
        for i in matrizLibros:
            print(i)

def eliminarlibro(matrizLibros):
    libroeliminar = input("\nIngrese el libro que desea eliminar: ")
    for libro in matrizLibros:
        if libro[0] == libroeliminar:
            matrizLibros.remove(libro)
            print("Libro eliminado con éxito")
            return
    print("\nEl libro no se encuentra en la lista")

def modificarlibro(matrizLibros):
    libroModificar = input("\nIngrese el libro que desea modificar: ")
    for libro in matrizLibros:
        if libro[0] == libroModificar:
            matrizLibros.remove(libro)
            nuevoLibro = input("\nIngrese el libro que desea agregar: ")
            autorLibro = input("Ingrese el autor del libro: ")
            añoLibro = input("Ingrese el año del libro: ")
            generoLibro = input("Ingrese el genero del libro: ")
            listaLibros = [nuevoLibro, autorLibro, añoLibro, generoLibro]
            matrizLibros.append(listaLibros)
            print("\nLibro modificado con éxito")
            return
    print("\nEl libro no se encuentra en la lista")


def guardarlibroe(matrizLibros, nombreArchivo):    
    with open(nombreArchivo, 'w', newline='', encoding='utf-8') as archivo:
        archivo_csv = csv.writer(archivo)
        archivo_csv.writerows(matrizLibros)
        print("Se creó correctamente el archivo.")

    with open(nombreArchivo, 'r', newline='', encoding='utf-8') as archivo:
        archivo_csv = csv.reader(archivo)
        for x in archivo_csv:
            print(x)

