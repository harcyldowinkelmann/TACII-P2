# 1) Implemente em Python um programa que solicite um número indefinido de valores positivos via teclado 
# e insira tais valores em uma lista. A condição de parada é quando o usuário digitar o valor 0. 
# Imprima a média dos valores inseridos na lista.

class MediaValores:
    '''
    Classe que solicita ao usuário valores positivos via teclado, armazena-os em uma lista.
    Após isso, calcula a média dos valores inseridos. 
    A condição de parada é o valor 0.
    Apenas valores positivos são considerados.
    '''

    def __init__(self):
        '''
        Inicializa a lista de valores e chama o método para iniciar o processo
        de coleta de dados e cálculo da média
        '''
        self.valores = []
        self.calculaMedia()

    def calculaMedia(self):
        """
        Solicita ao usuário valores positivos, armazena-os na lista,
        e calcula a média dos valores inseridos. Imprime o resultado no final.

        Returns:
            None: Apenas imprime o resultado, sem retornar valores.
        """

        while True:
            try:

                numero = float(input("Digite número positivo - Ou '0' para encerrar e fazer o cálculo da média: "))

                if (numero == 0):
                    break

                if (numero > 0):
                    self.valores.append(numero)
                else:
                    print("Número inválido! Insira apenas números positivos.")

            except ValueError:
                print("Entrada inválida, digite um número positivo!")
        
        if (len(self.valores)):
            media = sum(self.valores) / len(self.valores)
            print(f"A média dos valores inseridos foi de: {media: .2f}")
        else:
            print("Nenhum valor foi inserido!")

if __name__ == '__main__':
    MediaValores()