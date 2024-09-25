# 🏦 Controle Bancário em Python

![Python](https://img.shields.io/badge/Python-3.12%2B-blue.svg) ![Status](https://img.shields.io/badge/Status-Completed-green)

Bem-vindo ao **Controle Bancário em Python**! Este é um projeto simples que simula um sistema de controle bancário. Aqui você pode realizar operações básicas como **Depósito**, **Saque** e **Extrato**.

## 📋 Funcionalidades

- 📥 **Depósito:** Permite ao usuário adicionar saldo à conta.
- 💸 **Saque:** Realize saques respeitando limites diários e de saldo.
- 📜 **Extrato:** Visualize um resumo de todas as transações realizadas.
- ❌ **Saída:** Encerre a operação do sistema.

## 🚀 Tecnologias Utilizadas

- **Python 3.12+** 🐍
  - Estruturas de controle como `while`, `if-elif-else`
  - Operações com strings e números float
  - Interação via `input()` e `print()`

## 🎯 Objetivo

Este projeto tem o objetivo de praticar conceitos fundamentais de programação Python como loops, condicionais e manipulação de dados. Ele foi desenvolvido como parte de um **exercício prático** para consolidar as aulas do Bootcamp NTT DATA - Engenharia de Dados com Python, da DIO.

## 🛠️ Como Executar

1. Certifique-se de ter o **Python 3.12+** instalado em sua máquina.

2. Clone o repositório:
    ```bash
    git clone https://github.com/josealexandre87/controle-bancario-python.git
    ```
3. Acesse a pasta do projeto:
    ```bash
    cd controle-bancario-python
    ```
4. Execute o script:
    ```bash
    python sistema_bancario_com_python.py
    ```

## 🎉 Exemplo de Execução

```bash
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> d
Informe o valor do depósito: 100
Depósito: R$ 100.00

=> s
Informe o valor do saque: 50
Saque: R$ 50.00

=> e
================ EXTRATO ================
Depósito: R$ 100.00
Saque: R$ 50.00

Saldo: R$ 50.00
=========================================
