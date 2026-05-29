# Respostas Teóricas - Sistema de Armazenamento

**Em qual parte há contrato por herança?**
Na Parte A, ao utilizar a classe abstrata `Armazenador`.

**Em qual parte há contrato estrutural?**
Na Parte B, ao adotar o protocolo `Salvavel`.

**Qual abordagem é mais rígida?**
A abordagem que utiliza ABC. Ela é explícita, força o uso de herança e bloqueia de forma nativa implementações que não estejam em conformidade com o modelo base.

**Qual abordagem é mais flexível?**
A abordagem com `Protocol`. Ela aceita objetos variados na mesma funcionalidade, desde que contenham a assinatura metodológica adequada.

**Em qual situação ABC faz mais sentido? E em qual Protocol faz mais sentido?**
O ABC faz sentido quando o cenário demanda compartilhamento formal de código, herança explícita ou o estabelecimento de uma base controlada entre classes da mesma família. O uso do `Protocol` faz sentido para modelar casos onde o comportamento e a flexibilidade são prioritários e a linhagem hierárquica das classes é irrelevante.
