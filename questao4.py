from random import randint

limite_inferior = int(input('Limite inferior: '))
limite_superior = int(input('Limite superior: '))
tamanho = int(input('Informe o tamanho da lista: '))
lista = [randint(limite_inferior, limite_superior) for _ in range(tamanho)]
menor= lista[0]

for i in range(1, tamanho):
    if menor > lista[i]:
        menor = lista[i]

print(f'O menor valor da lista {lista} é {menor}.')