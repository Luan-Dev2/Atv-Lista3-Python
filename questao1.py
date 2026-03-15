from random import randint

tamanho = int(input('Informe o tamanho da lista: '))
lista = []
soma = 0

for c in range(tamanho):
    lista.append(randint(0, 10))
for c in lista:
    soma += c

print(f'A soma entre todos os elementos da lista {lista} é {soma}.')
