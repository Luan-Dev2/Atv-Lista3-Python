from random import randint

limite_inferior = int(input('Limite inferior: '))
limite_superior = int(input('Limite superior: '))
tamanho = int(input('Informe o tamanho da lista: '))
lista = [randint(limite_inferior, limite_superior) for _ in range(tamanho)]

soma = 0
media = 0

for c in lista:
    soma += c
    media = soma / tamanho

print(lista)
print(f'A média de todos os elementos da lista é {media:.2f}')