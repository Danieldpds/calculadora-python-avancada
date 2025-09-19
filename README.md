# 🧮 Calculadora Python Avançada

Uma calculadora completa e moderna desenvolvida em Python com interface amigável e todas as operações matemáticas essenciais.

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg)

## ✨ Características

### 🔢 Operações Básicas
- ➕ **Soma** - Adição de dois números
- ➖ **Subtração** - Subtração de dois números  
- ✖️ **Multiplicação** - Multiplicação de dois números
- ➗ **Divisão** - Divisão de dois números

### 🚀 Operações Avançadas
- 🔢 **Potência** - Cálculo de potências (base^expoente)
- √ **Raiz Quadrada** - Raiz quadrada de um número
- ∛ **Raiz N-ésima** - Raiz de qualquer índice
- ! **Fatorial** - Cálculo de fatorial
- 📐 **Funções Trigonométricas** - Seno, Cosseno e Tangente
- 📊 **Logaritmos** - Logaritmo base 10 e natural (ln)
- % **Porcentagem** - Cálculo de percentuais
- 🔄 **Módulo** - Resto da divisão

### 🎯 Recursos Especiais
- 📋 **Histórico de Operações** - Mantém registro de todos os cálculos
- 🛡️ **Tratamento de Erros** - Validação robusta de entradas
- 🎨 **Interface Amigável** - Menu interativo com emojis e formatação clara
- ⏸️ **Controle de Fluxo** - Pausa após cada operação para melhor usabilidade
- ✅ **Validação de Entrada** - Garante que apenas números válidos sejam aceitos

## 🚀 Instalação e Uso

### Pré-requisitos
- Python 3.6 ou superior
- Módulo `math` (incluído na biblioteca padrão do Python)

### Instalação
1. Clone o repositório:
```bash
git clone https://github.com/Danieldpds/calculadora-python-avancada.git
cd calculadora-python-avancada
```

2. Execute a calculadora:
```bash
python calculadora.py
```

### Uso Rápido
```bash
# No terminal/PowerShell
python calculadora.py
```

## 📖 Como Usar

1. **Execute o programa** - A calculadora abrirá com um menu interativo
2. **Escolha uma operação** - Digite o número correspondente à operação desejada
3. **Digite os valores** - Forneça os números solicitados
4. **Veja o resultado** - O resultado será exibido com formatação clara
5. **Continue calculando** - Pressione Enter para voltar ao menu

### Exemplo de Uso
```
==================================================
           CALCULADORA PYTHON
==================================================
1.  Soma (+)
2.  Subtração (-)
3.  Multiplicação (*)
4.  Divisão (/)
5.  Potência (^)
6.  Raiz quadrada (√)
...

Escolha uma opção: 1

==============================
   ➕ SOMA
==============================
Digite o primeiro número: 15
Digite o segundo número: 25

✅ Resultado: 15 + 25 = 40

Pressione Enter para continuar...
```

## 🏗️ Estrutura do Projeto

```
calculadora-python-avancada/
├── calculadora.py          # Arquivo principal da calculadora
├── README.md              # Documentação do projeto
└── requirements.txt       # Dependências do projeto
```

## 🔧 Funcionalidades Técnicas

### Classe Calculadora
A calculadora é implementada como uma classe Python com os seguintes métodos:

- `somar(a, b)` - Soma dois números
- `subtrair(a, b)` - Subtrai dois números
- `multiplicar(a, b)` - Multiplica dois números
- `dividir(a, b)` - Divide dois números
- `potencia(base, expoente)` - Calcula potência
- `raiz_quadrada(numero)` - Calcula raiz quadrada
- `raiz_n_esima(numero, indice)` - Calcula raiz n-ésima
- `fatorial(numero)` - Calcula fatorial
- `seno(angulo_graus)` - Calcula seno
- `cosseno(angulo_graus)` - Calcula cosseno
- `tangente(angulo_graus)` - Calcula tangente
- `logaritmo(numero, base)` - Calcula logaritmo
- `logaritmo_natural(numero)` - Calcula logaritmo natural
- `porcentagem(valor, percentual)` - Calcula percentual
- `modulo(a, b)` - Calcula resto da divisão

### Tratamento de Erros
- ✅ Divisão por zero
- ✅ Raiz quadrada de números negativos
- ✅ Fatorial de números negativos
- ✅ Logaritmo de números negativos ou zero
- ✅ Validação de entrada de números

## 🧪 Testes

A calculadora inclui validação automática de erros e tratamento de casos especiais:

```python
# Exemplos de validação
calc.dividir(10, 0)        # ❌ Erro: Divisão por zero
calc.raiz_quadrada(-4)     # ❌ Erro: Raiz de número negativo
calc.fatorial(-5)          # ❌ Erro: Fatorial de número negativo
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor

**Daniel** - [@Danieldpds](https://github.com/Danieldpds)

## 🙏 Agradecimentos

- Python Software Foundation pela linguagem Python
- Comunidade Python pela biblioteca `math`
- Todos os contribuidores do projeto

## 📊 Estatísticas do Projeto

![GitHub stars](https://img.shields.io/github/stars/Danieldpds/calculadora-python-avancada)
![GitHub forks](https://img.shields.io/github/forks/Danieldpds/calculadora-python-avancada)
![GitHub issues](https://img.shields.io/github/issues/Danieldpds/calculadora-python-avancada)
![GitHub pull requests](https://img.shields.io/github/issues-pr/Danieldpds/calculadora-python-avancada)

---

⭐ **Se este projeto foi útil para você, considere dar uma estrela!** ⭐