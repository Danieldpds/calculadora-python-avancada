import math

class Calculadora:
    def __init__(self):
        self.historico = []
    
    def adicionar_ao_historico(self, operacao, resultado):
        """Adiciona operação ao histórico"""
        self.historico.append(f"{operacao} = {resultado}")
    
    def somar(self, a, b):
        """Soma dois números"""
        resultado = a + b
        self.adicionar_ao_historico(f"{a} + {b}", resultado)
        return resultado
    
    def subtrair(self, a, b):
        """Subtrai dois números"""
        resultado = a - b
        self.adicionar_ao_historico(f"{a} - {b}", resultado)
        return resultado
    
    def multiplicar(self, a, b):
        """Multiplica dois números"""
        resultado = a * b
        self.adicionar_ao_historico(f"{a} * {b}", resultado)
        return resultado
    
    def dividir(self, a, b):
        """Divide dois números"""
        if b == 0:
            raise ValueError("Erro: Divisão por zero não é permitida!")
        resultado = a / b
        self.adicionar_ao_historico(f"{a} / {b}", resultado)
        return resultado
    
    def potencia(self, base, expoente):
        """Calcula potência"""
        resultado = base ** expoente
        self.adicionar_ao_historico(f"{base} ^ {expoente}", resultado)
        return resultado
    
    def raiz_quadrada(self, numero):
        """Calcula raiz quadrada"""
        if numero < 0:
            raise ValueError("Erro: Não é possível calcular raiz quadrada de número negativo!")
        resultado = math.sqrt(numero)
        self.adicionar_ao_historico(f"√{numero}", resultado)
        return resultado
    
    def raiz_n_esima(self, numero, indice):
        """Calcula raiz n-ésima"""
        if numero < 0 and indice % 2 == 0:
            raise ValueError("Erro: Não é possível calcular raiz par de número negativo!")
        if indice == 0:
            raise ValueError("Erro: Índice da raiz não pode ser zero!")
        resultado = numero ** (1/indice)
        self.adicionar_ao_historico(f"{indice}√{numero}", resultado)
        return resultado
    
    def fatorial(self, numero):
        """Calcula fatorial"""
        if numero < 0:
            raise ValueError("Erro: Fatorial não é definido para números negativos!")
        if not isinstance(numero, int):
            raise ValueError("Erro: Fatorial só é definido para números inteiros!")
        if numero > 170:
            raise ValueError("Erro: Número muito grande para calcular fatorial!")
        resultado = math.factorial(numero)
        self.adicionar_ao_historico(f"{numero}!", resultado)
        return resultado
    
    def seno(self, angulo_graus):
        """Calcula seno (ângulo em graus)"""
        angulo_radianos = math.radians(angulo_graus)
        resultado = math.sin(angulo_radianos)
        self.adicionar_ao_historico(f"sin({angulo_graus}°)", resultado)
        return resultado
    
    def cosseno(self, angulo_graus):
        """Calcula cosseno (ângulo em graus)"""
        angulo_radianos = math.radians(angulo_graus)
        resultado = math.cos(angulo_radianos)
        self.adicionar_ao_historico(f"cos({angulo_graus}°)", resultado)
        return resultado
    
    def tangente(self, angulo_graus):
        """Calcula tangente (ângulo em graus)"""
        angulo_radianos = math.radians(angulo_graus)
        resultado = math.tan(angulo_radianos)
        self.adicionar_ao_historico(f"tan({angulo_graus}°)", resultado)
        return resultado
    
    def logaritmo(self, numero, base=10):
        """Calcula logaritmo"""
        if numero <= 0:
            raise ValueError("Erro: Logaritmo não é definido para números negativos ou zero!")
        if base <= 0 or base == 1:
            raise ValueError("Erro: Base do logaritmo deve ser positiva e diferente de 1!")
        if base == 10:
            resultado = math.log10(numero)
            self.adicionar_ao_historico(f"log({numero})", resultado)
        else:
            resultado = math.log(numero, base)
            self.adicionar_ao_historico(f"log{base}({numero})", resultado)
        return resultado
    
    def logaritmo_natural(self, numero):
        """Calcula logaritmo natural (base e)"""
        if numero <= 0:
            raise ValueError("Erro: Logaritmo natural não é definido para números negativos ou zero!")
        resultado = math.log(numero)
        self.adicionar_ao_historico(f"ln({numero})", resultado)
        return resultado
    
    def porcentagem(self, valor, percentual):
        """Calcula percentual de um valor"""
        resultado = (valor * percentual) / 100
        self.adicionar_ao_historico(f"{percentual}% de {valor}", resultado)
        return resultado
    
    def modulo(self, a, b):
        """Calcula resto da divisão (módulo)"""
        if b == 0:
            raise ValueError("Erro: Divisão por zero não é permitida!")
        resultado = a % b
        self.adicionar_ao_historico(f"{a} % {b}", resultado)
        return resultado
    
    def mostrar_historico(self):
        """Mostra o histórico de operações"""
        if not self.historico:
            print("Histórico vazio.")
            return
        print("\n=== HISTÓRICO DE OPERAÇÕES ===")
        for i, operacao in enumerate(self.historico, 1):
            print(f"{i}. {operacao}")
    
    def limpar_historico(self):
        """Limpa o histórico de operações"""
        self.historico.clear()
        print("Histórico limpo!")

def obter_numero(mensagem):
    """Obtém um número válido do usuário"""
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Erro: Digite um número válido!")

def obter_numero_inteiro(mensagem):
    """Obtém um número inteiro válido do usuário"""
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Erro: Digite um número inteiro válido!")

def mostrar_menu():
    """Mostra o menu principal"""
    print("\n" + "="*50)
    print("           CALCULADORA PYTHON")
    print("="*50)
    print("1.  Soma (+)")
    print("2.  Subtração (-)")
    print("3.  Multiplicação (*)")
    print("4.  Divisão (/)")
    print("5.  Potência (^)")
    print("6.  Raiz quadrada (√)")
    print("7.  Raiz n-ésima")
    print("8.  Fatorial (!)")
    print("9.  Seno")
    print("10. Cosseno")
    print("11. Tangente")
    print("12. Logaritmo")
    print("13. Logaritmo natural (ln)")
    print("14. Porcentagem (%)")
    print("15. Módulo (%)")
    print("16. Ver histórico")
    print("17. Limpar histórico")
    print("0.  Sair")
    print("="*50)

def pausar():
    """Pausa a execução até o usuário pressionar Enter"""
    input("\nPressione Enter para continuar...")

def continuar_calculando():
    """Pergunta se o usuário quer continuar calculando"""
    while True:
        opcao = input("\nDeseja continuar calculando? (s/n): ").strip().lower()
        if opcao in ['s', 'sim', 'y', 'yes']:
            return True
        elif opcao in ['n', 'não', 'nao', 'no']:
            return False
        else:
            print("Digite 's' para sim ou 'n' para não.")

def main():
    """Função principal"""
    calc = Calculadora()
    resultado_anterior = None
    
    print("="*60)
    print("           🧮 CALCULADORA PYTHON AVANÇADA 🧮")
    print("="*60)
    print("Bem-vindo à calculadora mais completa!")
    print("Você pode usar o resultado anterior em novas operações.")
    print("="*60)
    
    while True:
        mostrar_menu()
        
        try:
            opcao = input(f"\nEscolha uma opção: ").strip()
            
            if opcao == "0":
                print("\n" + "="*50)
                print("Obrigado por usar a calculadora!")
                print("Até a próxima! 👋")
                print("="*50)
                break
            
            elif opcao == "1":  # Soma
                print("\n" + "="*30)
                print("   ➕ SOMA")
                print("="*30)
                a = obter_numero("Digite o primeiro número: ")
                b = obter_numero("Digite o segundo número: ")
                resultado = calc.somar(a, b)
                print(f"\n✅ Resultado: {a} + {b} = {resultado}")
                resultado_anterior = resultado
                pausar()
            
            elif opcao == "2":  # Subtração
                print("\n" + "="*30)
                print("   ➖ SUBTRAÇÃO")
                print("="*30)
                a = obter_numero("Digite o primeiro número: ")
                b = obter_numero("Digite o segundo número: ")
                resultado = calc.subtrair(a, b)
                print(f"\n✅ Resultado: {a} - {b} = {resultado}")
                resultado_anterior = resultado
                pausar()
            
            elif opcao == "3":  # Multiplicação
                print("\n" + "="*30)
                print("   ✖️ MULTIPLICAÇÃO")
                print("="*30)
                a = obter_numero("Digite o primeiro número: ")
                b = obter_numero("Digite o segundo número: ")
                resultado = calc.multiplicar(a, b)
                print(f"\n✅ Resultado: {a} × {b} = {resultado}")
                resultado_anterior = resultado
                pausar()
            
            elif opcao == "4":  # Divisão
                print("\n" + "="*30)
                print("   ➗ DIVISÃO")
                print("="*30)
                a = obter_numero("Digite o primeiro número: ")
                b = obter_numero("Digite o segundo número: ")
                resultado = calc.dividir(a, b)
                print(f"\n✅ Resultado: {a} ÷ {b} = {resultado}")
                resultado_anterior = resultado
                pausar()
            
            elif opcao == "5":  # Potência
                print("\n" + "="*30)
                print("   🔢 POTÊNCIA")
                print("="*30)
                base = obter_numero("Digite a base: ")
                expoente = obter_numero("Digite o expoente: ")
                resultado = calc.potencia(base, expoente)
                print(f"\n✅ Resultado: {base}^{expoente} = {resultado}")
                resultado_anterior = resultado
                pausar()
            
            elif opcao == "6":  # Raiz quadrada
                print("\n" + "="*30)
                print("   √ RAIZ QUADRADA")
                print("="*30)
                numero = obter_numero("Digite o número: ")
                resultado = calc.raiz_quadrada(numero)
                print(f"\n✅ Resultado: √{numero} = {resultado}")
                resultado_anterior = resultado
                pausar()
            
            elif opcao == "7":  # Raiz n-ésima
                print("\n" + "="*30)
                print("   ∛ RAIZ N-ÉSIMA")
                print("="*30)
                numero = obter_numero("Digite o número: ")
                indice = obter_numero("Digite o índice da raiz: ")
                resultado = calc.raiz_n_esima(numero, indice)
                print(f"\n✅ Resultado: {indice}√{numero} = {resultado}")
                resultado_anterior = resultado
                pausar()
            
            elif opcao == "8":  # Fatorial
                print("\n" + "="*30)
                print("   ! FATORIAL")
                print("="*30)
                numero = obter_numero_inteiro("Digite um número inteiro: ")
                resultado = calc.fatorial(numero)
                print(f"\n✅ Resultado: {numero}! = {resultado}")
                resultado_anterior = resultado
                pausar()
            
            elif opcao == "9":  # Seno
                print("\n" + "="*30)
                print("   📐 SENO")
                print("="*30)
                angulo = obter_numero("Digite o ângulo em graus: ")
                resultado = calc.seno(angulo)
                print(f"\n✅ Resultado: sin({angulo}°) = {resultado:.6f}")
                resultado_anterior = resultado
                pausar()
            
            elif opcao == "10":  # Cosseno
                print("\n" + "="*30)
                print("   📐 COSSENO")
                print("="*30)
                angulo = obter_numero("Digite o ângulo em graus: ")
                resultado = calc.cosseno(angulo)
                print(f"\n✅ Resultado: cos({angulo}°) = {resultado:.6f}")
                resultado_anterior = resultado
                pausar()
            
            elif opcao == "11":  # Tangente
                print("\n" + "="*30)
                print("   📐 TANGENTE")
                print("="*30)
                angulo = obter_numero("Digite o ângulo em graus: ")
                resultado = calc.tangente(angulo)
                print(f"\n✅ Resultado: tan({angulo}°) = {resultado:.6f}")
                resultado_anterior = resultado
                pausar()
            
            elif opcao == "12":  # Logaritmo
                print("\n" + "="*30)
                print("   📊 LOGARITMO")
                print("="*30)
                numero = obter_numero("Digite o número: ")
                base = input("Digite a base (Enter para base 10): ").strip()
                if base == "":
                    resultado = calc.logaritmo(numero)
                    print(f"\n✅ Resultado: log({numero}) = {resultado:.6f}")
                else:
                    base = float(base)
                    resultado = calc.logaritmo(numero, base)
                    print(f"\n✅ Resultado: log{base}({numero}) = {resultado:.6f}")
                resultado_anterior = resultado
                pausar()
            
            elif opcao == "13":  # Logaritmo natural
                print("\n" + "="*30)
                print("   📊 LOGARITMO NATURAL")
                print("="*30)
                numero = obter_numero("Digite o número: ")
                resultado = calc.logaritmo_natural(numero)
                print(f"\n✅ Resultado: ln({numero}) = {resultado:.6f}")
                resultado_anterior = resultado
                pausar()
            
            elif opcao == "14":  # Porcentagem
                print("\n" + "="*30)
                print("   % PORCENTAGEM")
                print("="*30)
                valor = obter_numero("Digite o valor: ")
                percentual = obter_numero("Digite o percentual: ")
                resultado = calc.porcentagem(valor, percentual)
                print(f"\n✅ Resultado: {percentual}% de {valor} = {resultado}")
                resultado_anterior = resultado
                pausar()
            
            elif opcao == "15":  # Módulo
                print("\n" + "="*30)
                print("   🔄 MÓDULO")
                print("="*30)
                a = obter_numero("Digite o primeiro número: ")
                b = obter_numero("Digite o segundo número: ")
                resultado = calc.modulo(a, b)
                print(f"\n✅ Resultado: {a} % {b} = {resultado}")
                resultado_anterior = resultado
                pausar()
            
            elif opcao == "16":  # Ver histórico
                print("\n" + "="*30)
                print("   📋 HISTÓRICO")
                print("="*30)
                calc.mostrar_historico()
                pausar()
            
            elif opcao == "17":  # Limpar histórico
                print("\n" + "="*30)
                print("   🗑️ LIMPAR HISTÓRICO")
                print("="*30)
                calc.limpar_historico()
                pausar()
            
            else:
                print("\n❌ Opção inválida! Tente novamente.")
                pausar()
        
        except ValueError as e:
            print(f"\n❌ Erro: {e}")
            pausar()
        except KeyboardInterrupt:
            print("\n\n👋 Programa interrompido pelo usuário.")
            break
        except Exception as e:
            print(f"\n❌ Erro inesperado: {e}")
            pausar()

if __name__ == "__main__":
    main()