
matrizLibros=[

];


def agregarLibro():
    nuevoLibro=input("Ingrese el libreo que desea agregar: ");
    listaLibros=[nuevoLibro];
    matrizLibros.append(listaLibros);

def mostrarLibros():
    for i in matrizLibros:
        print(i);

def eliminarlibro():
    libroeliminar=input("Ingrese el libro que desea eliminar: ");
    if libroeliminar in matrizLibros:
        matrizLibros.remove(libroeliminar);


    



