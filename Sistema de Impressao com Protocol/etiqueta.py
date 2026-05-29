class Etiqueta:
    def __init__(self, destinatario: str, endereco: str):
        self.destinatario = destinatario
        self.endereco = endereco

    def imprimir(self) -> None:
        print(f"Etiqueta: {self.destinatario} - Destino: {self.endereco}")