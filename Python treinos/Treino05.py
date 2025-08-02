#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math
import matplotlib.pyplot as plt

# Solicitar o raio ao usuário
raio = float(input("Digite o raio do círculo: "))

# Calcular a área
area = math.pi * raio ** 2

# Exibir a área
print(f'A área do círculo é: {area:.2f}')


circle = plt.Circle((0, 0), raio, fill=False)

fig, ax = plt.subplots()
ax.add_artist(circle)

ax.set_xlim(-raio-1, raio+1)
ax.set_ylim(-raio-1, raio+1)
ax.set_aspect('equal', 'box')

plt.title("Círculo")
plt.show()
