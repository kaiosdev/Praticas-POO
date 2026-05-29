# Respostas Teóricas - Sistema de Mídias Educacionais

**Qual é a classe abstrata do sistema?**
A classe abstrata do sistema é a classe `Midia`.

**Onde aparece a hierarquia?**
A hierarquia é formada pela classe base `Midia` e pelas suas subclasses derivadas: `Video`, `Podcast` e `TextoNarrado`.

**Onde aparece o polimorfismo?**
O polimorfismo é demonstrado no método `reproduzir_todas()` da classe `Plataforma`. Ele percorre a lista de mídias e chama o método `reproduzir()` para cada objeto, resultando em comportamentos diferentes dependendo do tipo específico da mídia em tempo de execução.

**Por que Midia não deveria ser instanciada diretamente?**
Porque ela atua como um contrato ou molde para as subclasses. Ela é genérica demais e declara o método `reproduzir()` sem definir exatamente como a reprodução deve ser feita, delegando essa responsabilidade para as classes concretas.
