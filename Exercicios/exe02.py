# Autor: Harcyldo Leonardo Viana Winkelmann
# Disciplina: Tópicos Avançados em Computação II

# A probabilidade de conseguir n caras em sequência ao lançar uma moeda não viciada n vezes é 2 elevado a –n.
# Implemente em Python a função “prob(n)” que aceita um inteiro não negativo n como
# entrada e retorna a probabilidade de n caras em seguida ao lançar uma moeda não viciada n vezes.
# >>> prob(1) 0.5
# >>> prob(2) 0.25.

def prob(n):
    """
    Calcula a probabilidade de obter n caras consecutivas ao lançar uma moeda não viciada n vezes.
    
    Parâmetros:
    n (int): Número de lançamentos e também o número de caras consecutivas desejadas.
    
    Retorna:
    float: A probabilidade de obter n caras consecutivas.
    """
    # A probabilidade é dada por 2 elevado a -n
    return 2 ** (-n)

def main():
    """
    Função principal que solicita ao usuário um valor inteiro positivo e calcula a
    probabilidade de obter n caras consecutivas.
    """
    while True:
        try:
            # Solicita o valor de 'n' ao usuário
            n = int(input("Digite um número inteiro não negativo (n): "))
            
            # Verifica se o número é não negativo
            if n >= 0:
                # Calcula e exibe a probabilidade
                print(f"A probabilidade de obter {n} caras consecutivas é: {prob(n):.4f}")
                break
            else:
                print("Por favor, digite um número inteiro não negativo.")
        
        except ValueError:
            # Trata erros de conversão quando o usuário não digita um número inteiro
            print("Entrada inválida. Por favor, digite um número inteiro válido.")

# Executa a função principal
if __name__ == "__main__":
    main()
