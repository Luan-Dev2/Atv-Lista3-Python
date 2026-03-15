from random import randint

limite_inferior = int(input('Limite inferior: '))
limite_superior = int(input('Limite superior: '))
tamanho = int(input('Informe o tamanho da lista: '))
lista = [randint(limite_inferior, limite_superior) for _ in range(tamanho)]
impares = 0

for i in lista:
    if i % 2 == 1:
        impares += 1

print(f'Na lista {lista} existe {impares} números ímpares.')