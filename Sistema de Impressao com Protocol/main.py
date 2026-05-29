from imprimivel import Imprimivel
from boleto import Boleto
from etiqueta import Etiqueta
from relatorio_simples import RelatorioSimples

def processar_impressao(item: Imprimivel) -> None:
    item.imprimir()

if __name__ == "__main__":
    boleto = Boleto("34191.09008 63571.277308 71444.640008 1 89770660015050", 150.50)
    etiqueta = Etiqueta("Jean", "Rua Quebra Cabeça, 67")
    relatorio = RelatorioSimples("Fechamento Mensal")

    processar_impressao(boleto)
    processar_impressao(etiqueta)
    processar_impressao(relatorio)