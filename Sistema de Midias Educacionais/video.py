from midia import Midia

class Video(Midia):
    def __init__(self, titulo: str, duracao: int, resolucao: str):
        super().__init__(titulo, duracao)
        self.resolucao = resolucao

    def reproduzir(self):
        print(f"▶️ Reproduzindo Vídeo: '{self.titulo}' em {self.resolucao}.")