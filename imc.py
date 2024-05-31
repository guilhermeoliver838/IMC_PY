#Declaração das variáveis
peso = float
altura = float
imc = float

#Entrada de dados Peso e Altura
peso = float(input("Insira seu peso: "))
altura = float(input("Insira sua altura: "))

#Calculo para o IMC
imc = peso/(altura ** 2)

#Exibição do Resultado do Calculo do IMC
print("Seu IMC é: ", imc)

if imc >= 20:
    print("Tá igual a Moby Dyck")

elif imc <= 20:
    print("Olha a Olivia Palito")

#Guilherme de Carvalho Oliveira -