from random import randint

limite_inferior = int(input('Limite inferior: '))
limite_superior = int(input('Limite superior: '))
tamanho = int(input('Informe o tamanho da lista: '))
lista = [randint(limite_inferior, limite_superior) for _ in range(tamanho)]
positivos = 0
negativos = 0

for i in lista:
    if i > 0:
        positivos += 1
    elif i < 0:
        negativos += 1

print(f'Na lista {lista} existe {positivos} números positivos e {negativos} números negativos.')