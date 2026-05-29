from empresa import Empresa
from funcionario_assalariado import FuncionarioAssalariado
from funcionario_horista import FuncionarioHorista
from funcionario_comissionado import FuncionarioComissionado

if __name__ == "__main__":
    empresa = Empresa("Tech Solutions")

    func1 = FuncionarioAssalariado("Ricky Silva", "111.111.111-11", 5000.00)
    func2 = FuncionarioHorista("Gustavo Souza", "222.222.222-22", 160, 45.00)
    func3 = FuncionarioComissionado("Iasmim Dias", "333.333.333-33", 50000.00, 5.0)

    empresa.adicionar_funcionario(func1)
    empresa.adicionar_funcionario(func2)
    empresa.adicionar_funcionario(func3)

    empresa.listar_funcionarios()
    empresa.mostrar_folha_pagamento()