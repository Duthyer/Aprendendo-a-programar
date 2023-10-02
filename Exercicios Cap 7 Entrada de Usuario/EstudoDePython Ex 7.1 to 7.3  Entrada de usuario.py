#FAÇA VOCÊ MESMO
#7.1 – Locação de automóveis: Escreva um programa que pergunte ao usuário qual tipo de carro ele gostaria de alugar. 
# Mostre uma mensagem sobre esse carro, por exemplo, “Deixe-me ver se consigo um Subaru para você.”

#7.2 – Lugares em um restaurante: Escreva um programa que pergunte ao usuário quantas pessoas estão em seu grupo para jantar.
# Se a resposta for maior que oito, exiba uma mensagem dizendo que eles deverão esperar uma mesa. Caso contrário, informe que sua mesa está pronta.

#7.3 – Múltiplos de dez: Peça um número ao usuário e, em seguida, informe se o número é múltiplo de dez ou não.

#RESPOSTAS DOS EXERCICIOS
#7.1
carros = input("Qual tipo de carro você gostaria de alugar?") #aqui guardamos a entrada do usuario em uma variavel.
print("Vou ver se consigo um"+" "+carros+" "+"para você") #aqui apresentamos a variavel.

#7.2
pessoas = input("Quantas pessoas estão em seu grupo para jantar?")
if int(pessoas) > 8:
    print("Vocês deverão aguardar uma mesa.")
else:
    print("Sua mesa esta pronta!") 

#7.3

numero = input("Me informe um número!")
if int(numero) % 10 == int(0):
    print("O número"+" "+numero+" "+"é multiplo de 10!")
else:
    print("O"+" "+numero+" "+"não é multiplo de 10")

