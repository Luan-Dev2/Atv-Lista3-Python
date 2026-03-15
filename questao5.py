from random import randint

limite_inferior = int(input('Limite inferior: '))
limite_superior = int(input('Limite superior: '))
tamanho = int(input('Informe o tamanho da lista: '))
lista = [randint(limite_inferior, limite_superior) for _ in range(tamanho)]
pares = 0

for i in lista:
    if i % 2 == 0:
        pares += 1

print(f'Na lista {lista} existe {pares} números pares.')