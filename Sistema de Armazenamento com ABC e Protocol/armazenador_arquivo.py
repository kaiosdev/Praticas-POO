from armazenador import Armazenador

class ArmazenadorArquivo(Armazenador):
    def salvar(self, dado: str):
        print(f"Salvando '{dado}' em arquivo local")