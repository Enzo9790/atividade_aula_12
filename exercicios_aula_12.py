#exercicio 1
import random

numero = random.randint(5, 10)
print(numero)

#exercicio 2
import random

numeros = [random.randint(1, 100) for _ in range(3)]
print(numeros)

#exercicio 3
import random

sequencia = range(10, 30)
numero = random.choice(sequencia)
print(numero)

#exercicio 4
for i in range(10, 0,-1):
    print(i)
print("Fogo!")

# exercicio 5

n = int(input("Digite um número inteiro positivo: "))
soma_pares = 0

for i in range(2, n + 1):
    if i % 2 == 0:
        soma_pares += i
print(f"A soma dos números pares de 2 até {n} é: {soma_pares}")

#exercicio 6
numero = int(input("Digite um número inteiro: "))

print(f"Tabuada de multiplicação do {numero}:")

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

#exercicio 7
for i in range(99, 0, -2):
    print(i)






