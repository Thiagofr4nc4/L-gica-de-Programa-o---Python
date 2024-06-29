numero_campeoes = int(input())
lista_campeoes = [0] * numero_campeoes
for i in range(numero_campeoes):
    lista_campeoes[i] = int(input())

maior_numero = max(lista_campeoes)
print(maior_numero)

