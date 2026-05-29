from funcionario import Funcionario

class Empresa:
    def __init__(self, nome: str):
        self.nome = nome
        self.lista_de_funcionarios = []

    def adicionar_funcionario(self, funcionario: Funcionario):
        self.lista_de_funcionarios.append(funcionario)

    def listar_funcionarios(self):
        print(f"\n--- Quadro de Funcionários: {self.nome} ---")
        for funcionario in self.lista_de_funcionarios:
            funcionario.mostrar_dados()


    def mostrar_folha_pagamento(self):
        print(f"\n--- Folha de Pagamento: {self.nome} ---")
        for funcionario in self.lista_de_funcionarios:
            pagamento = funcionario.calcular_pagamento()
            print(f"{funcionario.nome}: R$ {pagamento:.2f}")
