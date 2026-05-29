from midia import Midia

class TextoNarrado(Midia):
    def __init__(self, titulo: str, duracao: int, idioma: str):
        super().__init__(titulo, duracao)
        self.idioma = idioma

    def reproduzir(self):
        print(f" Lendo Texto Narrado: '{self.titulo}' no idioma {self.idioma}.")