# Solicita as informações ao usuário
nome = input("Qual o seu nome? ")
altura = float(input("Qual a sua altura (em metros)? "))
peso = float(input("Qual o seu peso (em kg)? "))

# Calcula o IMC
imc = peso / (altura ** 2)

# Exibe os resultados
print(f"\nOlá, {nome}!")
print(f"Seu IMC é: {imc:.2f}")

# Classifica o IMC
if imc < 18.5:
    print("Classificação: Abaixo do peso.")
elif imc < 24.9:
    print("Classificação: Peso normal.")
elif imc < 29.9:
    print("Classificação: Sobrepeso.")
else:
    print("Classificação: Obesidade.")