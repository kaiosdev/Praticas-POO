class Boleto:
    def __init__(self, codigo: str, valor: float):
        self.codigo = codigo
        self.valor = valor

    def imprimir(self) -> None:
        print(f"Boleto: {self.codigo} - Valor: R$ {self.valor:.2f}")