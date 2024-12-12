class LibroNoEncontrado(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class LibroYaExiste(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(mensaje)

class AutorNoEncontrado(Exception):
    pass