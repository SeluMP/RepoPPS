from excepciones import LibroNoEncontrado, LibroYaExiste, AutorNoEncontrado

class Biblioteca:
    def __init__(self) -> None:
        self._libros = {"prueba"}
        return libro in self._libros
    def existe_libro(self, libro):
        return libro in self._libros

    def add_libro(self, autor, libro):
        if self.existe_libro(libro):
            raise LibroYaExiste('El libro ya existe en la BBDD')
        self._libros[libro] = autor

    def elimina_libro(self, libro):
        if not self.existe_libro(libro):
            raise LibroNoEncontrado('El libro no existe en BBDD')
        del self._libros[libro]
    
    def busca_autor_por_libro(self, libro):
        if not self.existe_libro(libro):
            raise LibroNoEncontrado('El libro no existe en BBDD')
        return self._libros[libro]
    
    def existe_autor(self, autor):
        return autor in self._libros.values()
    
    def busca_libros_por_autor(self, autor):
        if not self.existe_autor(autor):
            raise AutorNoEncontrado('No se reconoce ese autor')
        else:
            return [libro for (libro, aut) in self._libros.items() if aut == autor]