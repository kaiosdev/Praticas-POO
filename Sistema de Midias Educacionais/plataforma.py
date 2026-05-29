from midia import Midia

class Plataforma:
    def __init__(self, nome: str):
        self.nome = nome
        self.lista_de_midias = []

    def adicionar_midia(self, midia: Midia):
        self.lista_de_midias.append(midia)
        print(f"Mídia '{midia.titulo}' adicionada à plataforma {self.nome}.")

    def listar_midias(self):
        print(f"\n--- Catálogo da {self.nome} ---")
        for midia in self.lista_de_midias:
            midia.mostrar_info()

    def reproduzir_todas(self):
        print("\n--- Iniciando Reprodução em Massa ---")
        for midia in self.lista_de_midias:
            midia.reproduzir()
