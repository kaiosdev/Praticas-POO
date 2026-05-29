# Respostas Teóricas - Sistema de Notificações

**Qual classe representa o contrato formal?**
A classe abstrata `Notificador`.

**Onde há polimorfismo?**
No método `enviar_para_todos()` da `CentralNotificacoes`. O laço de repetição aciona o método `notificar()` e o sistema se adapta à implementação da classe concreta (email, SMS ou aplicativo) correspondente ao objeto.

**Por que faz sentido usar ABC nesse caso?**
Faz sentido porque há uma relação familiar forte e direta entre as classes. Todas compartilham do mesmo domínio e propósito, de modo que estabelecer uma estrutura comum e um contrato rigoroso organiza a arquitetura.

**O que aconteceria se uma subclasse de Notificador não implementasse notificar()?**
O programa apresentaria um erro de tipo (`TypeError`) ao tentar instanciar o objeto. Para o Python, qualquer subclasse que não preencha todos os requisitos de métodos abstratos continua sendo tratada como uma classe abstrata.
