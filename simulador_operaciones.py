# Implemente un simulador de operaciones básicas de una biblioteca universitaria
# #, diseñando e implementando las clases y conceptos vistos en clase (encapsulamiento, 
# instanciación, atributos, objetos, etc.) que considere pertinentes.

# Requerimientos: Nuevos libros, nuevos usuarios, minimo de 3 categorias de libros

# El sistema debe mostrar un menú de opciones para cada uno de los requerimientos.

class Libro:
    def __init__(self, titulo, autor, categoria, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self._disponible = disponible

    def prestar(self):
        if self._disponible:
            self._disponible = False
            return True
        return False

    def devolver(self):
        self._disponible = True

    def esta_disponible(self):
        return self._disponible


class Usuario:
    def __init__(self, nombre, id_usuario):
        self._nombre = nombre
        self._id_usuario = id_usuario
        self._libros_prestados = []

    def tomar_libro(self, libro):
        if libro.prestar():
            self._libros_prestados.append(libro)
            return True
        return False

    def devolver_libro(self, libro):
        if libro in self._libros_prestados:
            libro.devolver()
            self._libros_prestados.remove(libro)
            return True
        return False

    def get_nombre(self):
        return self._nombre

    def get_id(self):
        return self._id_usuario

    def get_libros_prestados(self):
        return self._libros_prestados

class BibliotecaU:
    def __init__(self):
        self._libros = []
        self._usuarios = []

    def agregar_libro(self, libro):
        self._libros.append(libro)

    def agregar_usuario(self, usuario):
        self._usuarios.append(usuario)

    def buscar_libro(self, titulo):
        for libro in self._libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None

    def buscar_usuario(self, id_usuario):
        for usuario in self._usuarios:
            if usuario.get_id() == id_usuario:
                return usuario
        return None

    def mostrar_libros(self):
        if not self._libros:
            print("No hay libros en la biblioteca.")
        else:
            for libro in self._libros:
                if libro.esta_disponible():
                    estado = "Disponible"
                else:
                    estado = "Prestado"  
                print(f"Título: {libro.titulo}, Autor: {libro.autor}, Categoria: {libro.categoria}, Estado: {estado}")


if __name__ == "__main__":
    biblioteca = BibliotecaU()

    # Categorías existentes
    categorias = ["Ciencia", "Literatura", "Historia"]

    # Libros existentes
    biblioteca.agregar_libro(Libro("Fisica Basica", "Serway", "Ciencia"))
    biblioteca.agregar_libro(Libro("Cien años de soledad", "Gabriel Garcia Marquez", "Literatura"))
    biblioteca.agregar_libro(Libro("Historia Universal", "Juan Perez", "Historia"))

    # Usuarios existentes
    biblioteca.agregar_usuario(Usuario("Ana", "U001"))
    biblioteca.agregar_usuario(Usuario("Luis", "U002"))

    while True:
        print("\n--- Menu Biblioteca Universitaria ---")
        print("1. Mostrar libros")
        print("2. Agregar libro")
        print("3. Agregar usuario")
        print("4. Prestar libro")
        print("5. Devolver libro")
        print("6. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            biblioteca.mostrar_libros()
        # Menu para agregar nuevos libros
        elif opcion == "2":
            titulo = input("Titulo del libro: ")
            autor = input("Autor: ")
            print("Categorias disponibles:", ", ".join(categorias))
            categoria = input("Categoria: ")
            if categoria not in categorias:
                print("Categoria no valida. Se agregara a la lista de categorias.")
                categorias.append(categoria)
            biblioteca.agregar_libro(Libro(titulo, autor, categoria))
            print("Libro agregado correctamente.")
        # Menu para agregar nuevos usuarios 
        elif opcion == "3":
            nombre = input("Nombre del usuario: ")
            id_usuario = input("ID del usuario: ")
            if biblioteca.buscar_usuario(id_usuario):
                print("Ya existe un usuario con ese ID.")
            else:
                biblioteca.agregar_usuario(Usuario(nombre, id_usuario))
                print("Usuario agregado correctamente.")
        # Menu para prestar libros
        elif opcion == "4":
            id_usuario = input("ID del usuario: ")
            usuario = biblioteca.buscar_usuario(id_usuario)
            if not usuario:
                print("Usuario no encontrado.")
                continue
            titulo = input("Titulo del libro a prestar: ")
            libro = biblioteca.buscar_libro(titulo)
            if not libro or not libro.esta_disponible():  
                print("Libro no encontrado o no disponible.")
            else:
                usuario.tomar_libro(libro)
                print("Libro prestado correctamente.")
        # Menu para devolver libros
        elif opcion == "5":
            id_usuario = input("ID del usuario: ")
            usuario = biblioteca.buscar_usuario(id_usuario)
            if not usuario:
                print("Usuario no encontrado.")
                continue
            if not usuario.get_libros_prestados():
                print("El usuario no tiene libros prestados.")
                continue
            print("Libros prestados:")
            for indice, libro in enumerate(usuario.get_libros_prestados()):
                print(f"{indice+1}. {libro.titulo}")  
                # Es mas 1 para que no inicie en 0
            indice = int(input("Seleccione el numero del libro a devolver: ")) - 1

            if 0 <= indice < len(usuario.get_libros_prestados()):
                libro = usuario.get_libros_prestados()[indice]
                usuario.devolver_libro(libro)
                
                print("Libro devuelto correctamente.")
            else:
                print("Selección inválida.")
        # Menu para salir de la biblioteca
        elif opcion == "6":
            print("¡Has salido de la biblioteca U!")
            break
        else:
            print("Opcion no valida. Intente de nuevo.")

