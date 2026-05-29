from armazenador import Armazenador
from armazenador_arquivo import ArmazenadorArquivo
from armazenador_banco import ArmazenadorBanco
from armazenador_nuvem import ArmazenadorNuvem
from salvavel import Salvavel

def executar_salvamento_formal(armazenador: Armazenador, dado: str):
    armazenador.salvar(dado)

def executar_salvamento_flexivel(objeto: Salvavel, dado: str):
    objeto.salvar(dado)

if __name__ == "__main__":
    arq = ArmazenadorArquivo()
    bd = ArmazenadorBanco()
    nuvem = ArmazenadorNuvem()

    executar_salvamento_formal(arq, "Registro A1")
    executar_salvamento_formal(bd, "Registro B2")

    executar_salvamento_flexivel(arq, "Registro C3")
    executar_salvamento_flexivel(bd, "Registro D4")
    executar_salvamento_flexivel(nuvem, "Registro E5")
