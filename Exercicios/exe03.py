# A distância entre dois pontos P e Q em um plano cartesiano pode ser calculada usando o teorema de Pitágoras c2 = a2 + b2 
# no qual a hipotenusa c seria a distância entre um ponto P e Q. 
# Os valores de a e b seriam a diferença entre os pontos para os eixos x e y, respectivamente. 
# Para resolver o problema de determinar o acerto dentro de um alvo de dardos com raio R,
# considerando P como centro do alvo e Q como o dardo atirado, podemos usar uma adaptação do
# teorema de tal forma que o resultado é determinado por (Q. x − P. x)2 + (Q. y − P. y)2 <= R2. 
# Escreva em Python uma função chamada “acerto_dardo(R,P,Q)” que retorna verdadeiro caso
# Q acertou a área de raio 5 a partir de P ou falso caso contrário. Por exemplo, para R=5, P=(0,0) e
# Q=(4,4) deve retornar falso, enquanto um dardo Q=(3,3) resulta em verdadeiro.

import math

def acerto_dardo(R, P, Q):
    """
    Verifica se o dardo no ponto Q acertou o alvo com raio R e centro no ponto P.
    
    Parâmetros:
    R (float): O raio do alvo.
    P (tuple): Coordenadas do centro do alvo (P.x, P.y).
    Q (tuple): Coordenadas do ponto onde o dardo atingiu (Q.x, Q.y).
    
    Retorna:
    bool: True se o dardo acertou o alvo, False caso contrário.
    """
    # Calcula a distância entre os pontos P e Q usando o teorema de Pitágoras
    distancia = math.sqrt((Q[0] - P[0])**2 + (Q[1] - P[1])**2)
    
    # Verifica se a distância é menor ou igual ao raio R
    return distancia <= R

# Teste
R = 5
P = (0, 0)  # Centro do alvo
Q1 = (4, 4)  # Dardo fora do alvo
Q2 = (3, 3)  # Dardo dentro do alvo

print(acerto_dardo(R, P, Q1))
print(acerto_dardo(R, P, Q2))
