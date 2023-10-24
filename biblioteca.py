"""
Paginas y videos utilizados para realizar el trabajo:
Pagina:
https://thedataschools.com/python/set/eliminar-elementos-conjunto/
Videos:
https://www.youtube.com/watch?v=HtKqSJX7VoM&ab_channel=SoyDalto
https://www.youtube.com/watch?v=JVNirg9qs4M&ab_channel=BitBoss
"""


class libro:
    def __init__(self, titulo, autor, año, genero):

        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.genero = genero

    def dartitulo(self):
        return self.titulo

    def darautor(self):
        return self.autor

    def daraño(self):
        return self.año

    def dargenero(self):
        return self.genero


class Biblioteca:
    def __init__(self):
        self.libros = []

    def mostrar_libros(self):
        if len(self.libros) != 0:
            for libro in self.libros:
                print(f"Título:{libro.dartitulo()}")
                print(f"Autor:{libro.darautor()}")
                print(f"Año de publicación:{libro.daraño()}")
                print(f"Genero:{libro.dargenero()}")
                print(" ")
        else:
            print("la biblioteca está vacia")

    def buscar_libro_por_titulo(self, titulo):
        for libro in self.libros:
            if libro.dartitulo() == titulo:
                return libro

        return None

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(
            f"Se ha añadido el libro a la biblioteca el libro: {libro.dartitulo()}")

    def eliminar_libro(self, titulo):
        for libro in self.libros:
            if libro.dartitulo() == titulo:
                self.libros.remove(libro)
                print("Libro eliminado con exito")
                return self.libros
        return None


biblioteca = Biblioteca()
libro0 = libro("Nacidos de la bruma",
               "Brandon sanderson", 2006, "Ficción")
libro1 = libro("Once minutos", "Paulo Coelho", 2003, "Novela")
libro2 = libro("Harry potter", "J.k.rowling", 1997, "Ficción")
libro3 = libro("El principito", "Antoine de saint-exupery", 1943, "Fantasía")
biblioteca.agregar_libro(libro0)
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

confirmacion = 0

while confirmacion == 0:
    try:
        accion = int(input("""¿Que desea hacer?
1 Mostrar libro
2 Buscar libro
3 Añadir libro
4 Eliminar un libro
0 salir app
"""))
    except ValueError:

        print("El valor debe ser tipo numerico")

        accion = 10
# cerrar app
    if accion == 0:

        print("Gracias por utilizar nuestra biblioteca")

        confirmacion = 1

        break
# mostrar todos los libros
    elif accion == 1:

        biblioteca.mostrar_libros()

# buscar un libro en especifico

    elif accion == 2:
        librobuscado = input("""¿Que libro esta buscando?
""").capitalize()
        nombre = biblioteca.buscar_libro_por_titulo(librobuscado)
        if nombre:
            print(f"Si esta disponible el libro: \n{nombre.dartitulo()}")
        else:
            print("No contamos con ese libro")

# añadir un libro nuevo

    elif accion == 3:

        titulo = input("Introduce el titulo del libro ").capitalize()

        autor = input("Introduce el autor ").capitalize()

        año = int(input("Introduce el año en el que fue publicado "))

        genero = input("Introduce el genero ").capitalize()

        libro4 = libro(titulo, autor, año, genero)

        biblioteca.agregar_libro(libro4)
# borrar un libro
    elif accion == 4:
        librobuscadoeliminar = input("""¿Titulo del libro a eliminar?
""").capitalize()
        nombreeliminar = biblioteca. eliminar_libro(librobuscadoeliminar)
        if nombreeliminar == None:
            print("No encontrado")

    else:
        print("Acción fallida")
