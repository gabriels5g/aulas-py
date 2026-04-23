carteira = 200
dolar = 4.98
dinheiro = carteira / dolar
print(f"Com R${carteira}, você pode comprar ${dinheiro:.2f} dólares.")

#programa que le a largura e a altura de uma parede em metros, e calcula a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta 2 metros quadrados.
weight = float(input("Digite a largura da parede em metros: "))
height = float(input("Digite a altura da parede em metros: "))
area = weight * height
tinta = area / 3
print(f"A área da parede é de {area:.2f} metros quadrados.")
print(f"A quantidade de tinta necessária para pintar a parede é de {tinta:.2f} litros.")
