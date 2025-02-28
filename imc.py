def linhas():
    print("-----------------------------")

linhas()
print("  Vamos calcular o seu IMC!")
linhas()
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros (Ex.: 1.75): "))
imc = peso / (altura ** 2)

categorias = [
    (18.5, "Abaixo do peso"),
    (24.9, "Peso normal"),
    (29.9, "Sobrepeso"),
    (34.9, "Obesidade Grau I"),
    (39.9, "Obesidade Grau II"),
    (float("inf"), "Obesidade Grau III"),
]

linhas()
for limite, categoria in categorias:
    if imc <= limite:
        print(f"Seu IMC é de {imc:.2f}.")
        print("Categoria:", categoria)
        break
linhas()

# Fonte dos dados: https://ge.globo.com/eu-atleta/nutricao/post/2022/08/17/veja-qual-e-o-imc-ideal-e-como-calcular.ghtml