# 🧮 Lista de Exercícios – Lógica de Programação

Repositório com uma coleção de **exercícios práticos para treinar lógica de programação**, baseados na lista publicada pela [DIO (Digital Innovation One)](https://www.dio.me/articles/lista-de-exercicios-para-treinar-logica-de-programacao).  
Esses exercícios são voltados para iniciantes e estudantes que desejam reforçar a base de raciocínio lógico usando linguagens como **Python**, **JavaScript**, **C**, ou qualquer outra linguagem imperativa.

O objetivo é desenvolver habilidades fundamentais em estruturas de controle, operadores, entrada e saída de dados e algoritmos básicos.

---

![Status](https://img.shields.io/badge/status-em%20andamento-yellow)
![Linguagem](https://img.shields.io/badge/foco-lógica%20de%20programação-blue)
![Versão](https://img.shields.io/badge/versão-1.0.0-green)
![Licença](https://img.shields.io/badge/licença-MIT-lightgrey)

---

## 📑 Sumário

- [📘 Sobre](#-sobre)
- [🧠 Conteúdo da Lista](#-conteúdo-da-lista)
- [⚙️ Requisitos](#️-requisitos)
- [🚀 Como Executar](#-como-executar)
- [📂 Estrutura do Projeto](#-estrutura-do-projeto)
- [💡 Sugestão de Linguagem](#-sugestão-de-linguagem)
- [🤝 Contribuição](#-contribuição)
- [📜 Licença](#-licença)
- [👨‍💻 Autor](#-autor)

---

## 📘 Sobre

Esta lista contém uma série de **exercícios de lógica** baseados no artigo original da DIO e abrangendo desde os fundamentos até desafios intermediários.  
São ideais para quem está iniciando no estudo de algoritmos e programação estruturada.

Cada exercício tem um **enunciado claro** e pode ser resolvido em qualquer linguagem.  
A pasta principal contém os arquivos numerados para facilitar o acompanhamento e versionamento.

> Fonte original: [DIO – Lista de Exercícios para Treinar Lógica de Programação](https://www.dio.me/articles/lista-de-exercicios-para-treinar-logica-de-programacao)

---

## 🧠 Conteúdo da Lista

Exemplos de tópicos abordados:

1. Operações matemáticas e condicionais  
2. Estruturas de decisão (`if`, `else`, `elif`)  
3. Estruturas de repetição (`for`, `while`)  
4. Entrada e saída de dados  
5. Vetores, matrizes e laços aninhados  
6. Funções e modularização de código  
7. Algoritmos de cálculo e tabulação  
8. Exercícios de lógica aplicada

Exemplo de enunciado:
> **Exercício 18:** Francisco tem 1,50m e cresce 2 cm por ano, enquanto Sara tem 1,10m e cresce 3 cm por ano.  
> Faça um algoritmo que calcule e imprima em quantos anos Sara será mais alta que Francisco.

---

## ⚙️ Requisitos

Para testar os códigos, é necessário ter instalada alguma das seguintes linguagens:

- **Python 3.10+**
- **Node.js 18+**
- **GCC (C/C++)**
- **Java 11+**

---

## 🚀 Como Executar

### Em Python:

```bash
# Clonar o repositório
git clone https://github.com/seuusuario/lista-logica-programacao.git

# Acessar o diretório
cd lista-logica-programacao

# Executar um exercício específico
python exercicio18.py
```

### Em JavaScript:

```bash
node exercicio18.js
```

### Em C:

```bash
gcc exercicio18.c -o exercicio18
./exercicio18
```

---

## 📂 Estrutura do Projeto

```
Lista-de-Exercicios/
├── Exercicios/
│   ├── exercicio01.py
│   ├── exercicio02.py
│   ├── exercicio03.py
│   ├── ...
│   └── exercicio25.py
├── README.md
└── Lista de Exercícios para treinar Lógica de Programação.pdf
```

---

## 💡 Sugestão de Linguagem

Os exercícios podem ser resolvidos em qualquer linguagem, mas o repositório pode conter exemplos em **Python**, por ser simples e ideal para aprendizado.

Exemplo de solução:

```python
# Exemplo - Exercício 18
francisco = 1.50
sara = 1.10
anos = 0

while sara <= francisco:
    francisco += 0.02
    sara += 0.03
    anos += 1

print(f"Sara será mais alta que Francisco em {anos} anos.")
```

---

## 🤝 Contribuição

Contribuições são bem-vindas!  
Caso queira adicionar novos exercícios ou soluções:

1. Crie uma *branch*:
   ```bash
   git checkout -b feature/novo-exercicio
   ```
2. Faça o commit:
   ```bash
   git commit -m "feat: adiciona exercício sobre estruturas de repetição"
   ```
3. Envie:
   ```bash
   git push origin feature/novo-exercicio
   ```
4. Abra um *Pull Request* no GitHub.

---

## 📜 Licença

Este projeto é licenciado sob a [MIT License](./LICENSE).  
Você pode usá-lo, estudar, modificar e compartilhar livremente, desde que mantenha os créditos e a referência à fonte original (DIO).

---

## 👨‍💻 Autor

**Igor**  
📧 contato@exemplo.com  
🌐 [GitHub](https://github.com/seuusuario)  
💼 [LinkedIn](https://linkedin.com/in/seuusuario)

---

### ✨ Agradecimento

Agradecimento especial à [DIO (Digital Innovation One)](https://www.dio.me/) pela disponibilização dos exercícios originais.  
> “A lógica é o alicerce de toda boa programação.” 🧩
