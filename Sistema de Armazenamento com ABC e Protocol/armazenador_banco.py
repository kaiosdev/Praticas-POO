from armazenador import Armazenador

class ArmazenadorBanco(Armazenador):
    def salvar(self, dado: str):
        print(f"Salvando '{dado}' no banco de dados")