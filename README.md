<div align="center">
  <h1>🐍 Lista de Exercícios II (Parte 1) - POO</h1>
  <p><i>Implementações práticas de Classes Abstratas, Protocolos e Polimorfismo</i></p>

  <img src="https://img.shields.io/badge/Linguagem-Python_3-blue?style=for-the-badge&logo=python" alt="Linguagem">
  <img src="https://img.shields.io/badge/Disciplina-Sistemas de Informação-green?style=for-the-badge" alt="Disciplina">
  <img src="https://img.shields.io/badge/Instituição-ICET--UFAM-orange?style=for-the-badge" alt="Instituição">
</div>

---

## 📝 Sobre o Projeto

Este repositório armazena as implementações em Python das cinco questões da **Lista de Exercícios II (Parte 1)**. O objetivo principal é consolidar a transição entre herança clássica, classes abstratas e interfaces estruturais no desenvolvimento de software.

> **Foco de Aprendizagem:** O projeto explora a criação de contratos formais utilizando o módulo `abc.ABC` e contratos estruturais (Duck Typing) utilizando `typing.Protocol`, além de aplicar os conceitos de herança, especialização e ligação dinâmica.

---

## 🚀 Questões Implementadas

- **Q1. Sistema de Mídias Educacionais:** Hierarquia de classes (`Video`, `Podcast`, `TextoNarrado`) baseadas em uma classe abstrata `Midia`, com reprodução gerenciada de forma polimórfica pela classe `Plataforma`.
- **Q2. Sistema de Funcionários:** Polimorfismo aplicado ao cálculo de pagamentos com uma classe base `Funcionario` e diferentes tipos de contratos de trabalho, geridos pela classe `Empresa`.
- **Q3. Sistema de Notificações:** Criação de um contrato formal e explícito através da classe abstrata `Notificador`, forçando subclasses de envio a implementarem o método de notificação.
- **Q4. Sistema de Impressão:** Mudança de paradigma para *Duck Typing* utilizando `Protocol` para criar um contrato estrutural `Imprimivel`.
- **Q5. Sistema de Armazenamento:** Comparação prática na modelagem de um mesmo problema sob duas óticas: herança formal com `ABC` (`Armazenador`) e tipagem estrutural com `Protocol` (`Salvavel`).

---

## 🛠️ Ferramentas Utilizadas

- **Linguagem:** Python 3
- **Editor de Código:** Visual Studio Code (VS Code)
- **Versionamento:** Git e GitHub
- **Ambientes Virtuais:** `venv`

---

## 📁 Estrutura do Repositório

O código-fonte foi modularizado separando cada classe em seu próprio arquivo para aplicar boas práticas de desenvolvimento.

| Diretório | Descrição |
| :--- | :--- |
| [`Sistema de Midias Educacionais/`](Sistema%20de%20Midias%20Educacionais/) | Sistema de Mídias Educacionais (Classes Abstratas e Polimorfismo). |
| [`Sistema de Funcionarios de uma Empresa/`](Sistema%20de%20Funcionarios%20de%20uma%20Empresa/) | Sistema de Funcionários (Hierarquia e Polimorfismo no cálculo de salários). |
| [`Sistema de Notificacoes com ABC/`](Sistema%20de%20Notificacoes%20com%20ABC/) | Sistema de Notificações (Contrato explícito com `ABC`). |
| [`Sistema de Impressao com Protocol/`](Sistema%20de%20Impressao%20com%20Protocol/) | Sistema de Impressão (Contrato estrutural com `Protocol`). |
| [`Sistema de Armazenamento com ABC e Protocol/`](Sistema%20de%20Armazenamento%20com%20ABC%20e%20Protocol/) | Sistema de Armazenamento (Comparação direta entre `ABC` e `Protocol`). |

---

## ⚙️ Como Executar os Códigos

Para executar e reproduzir os códigos localmente, siga os passos abaixo:

**1. Clone o repositório:**
```bash
git clone [https://github.com/kaiosdev/Praticas-POO.git](https://github.com/kaiosdev/Praticas-POO.git)
cd Praticas-POO
