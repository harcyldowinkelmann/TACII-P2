# A probabilidade de conseguir n caras em sequência ao lançar uma moeda não viciada n vezes é 2 elevado a –n. (Ou seja, 1 / (2 elevado a n)) 
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

print(prob(4))