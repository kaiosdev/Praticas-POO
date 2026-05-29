# Respostas Teóricas - Sistema de Funcionários

**Qual é a superclasse da hierarquia?**
A superclasse é a classe abstrata `Funcionario`.

**Quais são as subclasses?**
As subclasses são `FuncionarioAssalariado`, `FuncionarioHorista` e `FuncionarioComissionado`.

**Onde ocorre sobrescrita?**
A sobrescrita ocorre quando cada uma das subclasses implementa a sua própria versão do método `calcular_pagamento()`, redefinindo a regra estabelecida de forma abstrata pela superclasse `Funcionario`.

**Onde ocorre polimorfismo?**
Ocorre no método `mostrar_folha_pagamento()` da classe `Empresa`. Esse método itera sobre a lista genérica de funcionários e chama o método `calcular_pagamento()`, deixando a linguagem decidir de forma dinâmica qual cálculo aplicar.

**Qual a vantagem de usar ABC nesse caso?**
O uso de ABC impõe uma hierarquia clara e exige uma herança explícita. A principal vantagem é impedir que a classe `Funcionario` seja instanciada sem sentido e garantir que nenhuma subclasse seja criada caso não tenha a lógica de pagamento implementada.
