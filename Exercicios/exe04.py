# Autor: Harcyldo Leonardo Viana Winkelmann
# Disciplina: Tópicos Avançados em Computação II

# Implemente em Python a função de jogo de computador round_collision() que verifica se dois
# objetos circulares colidem; ela retorna True se eles colidirem e False se não colidirem. Cada objeto
# circular será dado pelo seu raio e as coordenadas (x, y) do seu centro. Assim, a função apanhará
# seis números como entrada: as coordenadas (x1, y1) do centro e o raio r1 do primeiro círculo, e
# as coordenadas (x2, y2) do centro e o raio r2 do segundo círculo.
# >>> round_collision (0, 0, 3, 0, 5, 3)
# True
# >>> round_collision (0, 0, 1.4, 2, 2, 1.4)
# False

import math

def round_collision(x1, y1, r1, x2, y2, r2):
    """
    Verifica se dois objetos circulares colidem.
    
    Parâmetros:
    x1, y1 (float): Coordenadas do centro do primeiro círculo.
    r1 (float): Raio do primeiro círculo.
    x2, y2 (float): Coordenadas do centro do segundo círculo.
    r2 (float): Raio do segundo círculo.
    
    Retorna:
    bool: True se os círculos colidirem, False caso contrário.
    """
    # Calcula a distância entre os dois centros usando o teorema de Pitágoras
    distancia_centros = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    # Verifica se a soma dos raios é maior ou igual à distância entre os centros
    return distancia_centros <= (r1 + r2)

# Testes
print(round_collision(0, 0, 3, 0, 5, 3))
print(round_collision(0, 0, 1.4, 2, 2, 1.4))
