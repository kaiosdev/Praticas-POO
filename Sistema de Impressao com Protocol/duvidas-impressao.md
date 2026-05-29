# Respostas Teóricas - Sistema de Impressão

**Onde está o contrato nesse caso?**
O contrato está no protocolo `Imprimivel`.

**Por que as classes podem funcionar sem herdar explicitamente do protocolo?**
Porque a abordagem utilizando `Protocol` define um contrato de cunho estrutural e não hierárquico. O Python apenas verifica se os objetos oferecem a interface requerida (neste caso, o método `imprimir()`).

**Esse caso se aproxima mais de ABC ou de duck typing?**
Aproxima-se da filosofia do duck typing. O foco recai na compatibilidade do método oferecido pelo objeto e não na sua origem de herança formal.

**Qual a principal diferença entre esse caso e o da Questão 1?**
Na Questão 1, a regra foi imposta através de uma herança formal, exigindo que as classes derivadas estendessem explicitamente de uma base. Neste caso, os objetos funcionam de forma livre em tempo de execução, exigindo unicamente a existência da estrutura de método estabelecida.
