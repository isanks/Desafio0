def subconjuntos(valor):
    subsets = [[]] 

    for num in valor:
        subsets += [subset + [num] for subset in subsets]

    return subsets

valor = [1, 2]
resultado = subconjuntos(valor)
print(resultado)
