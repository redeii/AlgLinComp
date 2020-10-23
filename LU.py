import numpy as np


def find_x(L, U, b):  # FUNCAO QUE FAZ A SUBSTITUICAO PARA FRENTE E PARA TRAS, ENCONTRANDO VETOR X
    # FORWARD SUBSTITUTION
    # [L]y = {B}

    size = len(b)
    # inicializacao de Y (matriz composta de 0s)
    y = np.array([[0] for i in range(size)], float)
    for i in range(size):
        somaj = sum(L[i, j] * y[j] for j in range(i))
        y[i] = (b[i] - somaj)/L[i, i]

    # BACKWARD SUBSTITUTION
    # [U]{x} = y
    x = np.array([[0] for i in range(size)], float)  # inicializacao de X
    for i in range(size-1, -1, -1):
        somaj = sum(U[i, j]*x[j] for j in range(i+1, size))
        x[i] = (y[i] - somaj)/U[i, i]
    return x


def fact_lu(a, b):

    size = len(a)

    L = np.array([[0]*size for i in range(size)], float)

    # PIVOTAMENTO
    for k in range(size-1):
        if abs(a[k, k]) < 1.0e-11:
            for i in range(k+1, size):
                if abs(a[i, k]) > abs(a[k, k]):
                    a[[k, i]] = a[[i, k]]  # Trocando linhas de lugar
                    b[[k, i]] = b[[i, k]]
                    break
    U = np.copy(a)  # Inicializando U como a ja que U possui elementos de a

    # Definindo diagonal principal da matriz L
    for i in range(size):
        L[i, i] = 1

    for k in range(size):  # Definindo L e U
        for i in range(k+1, size):
            fator = a[i, k]/a[k, k]
            L[i, k] = fator

            for j in range(size):
                a[i, j] = a[i, j] - fator*a[k, j]
                U[i, j] = a[i, j]

    # Caso a funcao seja utilizada apenas para fazer a decomposicao
    x = find_x(L, U, b)

    # Checando se o numpy vai reclamar de divisao por 0, matriz singular.
    array_sum_L = np.sum(L)
    array_sum_U = np.sum(U)
    if (np.isnan(array_sum_L)) or (np.isnan(array_sum_U)):
        print('Matriz singular')
        return
    return L, U, x
