#FAÇA VOCÊ MESMO
#5.3 – Cores de alienígenas #1: Suponha que um alienígena acabou de ser atingido em um jogo. 
#Crie uma variável chamada alien_color e atribua-lhe um valor igual a 'green', 'yellow' ou 'red'.
# • Escreva uma instrução if para testar se a cor do alienígena é verde. 
# Se for, mostre uma mensagem informando que o jogador acabou de ganhar cinco pontos.
# • Escreva uma versão desse programa em que o teste if passe e outro em que ele falhe. 
#(A versão que falha não terá nenhuma saída.) 
# 5.4 – Cores de alienígenas #2: Escolha uma cor para um alienígena, como foi feito no Exercício 5.3, e escreva uma cadeia if-else.
#• Se a cor do alienígena for verde, mostre uma frase informando que o jogador acabou de ganhar cinco pontos por atingir o alienígena.
#• Se a cor do alienígena não for verde, mostre uma frase informando que o jogador acabou de ganhar dez pontos.
#• Escreva uma versão desse programa que execute o bloco if e outro que execute o bloco else.

#5.5 – Cores de alienígenas #3: Transforme sua cadeia if-else do Exercício 5.4 em uma cadeia if-elif-else.
#• Se o alienígena for verde, mostre uma mensagem informando que o jogador ganhou cinco pontos.
#• Se o alienígena for amarelo, mostre uma mensagem informando que o jogador ganhou dez pontos.
#• Se o alienígena for vermelho, mostre uma mensagem informando que o jogador ganhou quinze pontos.
#• Escreva três versões desse programa, garantindo que cada mensagem seja exibida para a cor apropriada do alienígena.

#5.6 – Estágios da vida: Escreva uma cadeia if-elif-else que determine o  estágio da vida de uma pessoa. Defina um valor para a variável age e então: 
#• Se a pessoa tiver menos de 2 anos de idade, mostre uma mensagem dizendo que ela é um bebê.
#• Se a pessoa tiver pelo menos 2 anos, mas menos de 4, mostre uma mensagem dizendo que ela é uma criança.
#• Se a pessoa tiver pelo menos 4 anos, mas menos de 13, mostre uma mensagem dizendo que ela é um(a) garoto(a).
#• Se a pessoa tiver pelo menos 13 anos, mas menos de 20, mostre uma mensagem dizendo que ela é um(a) adolescente.
#• Se a pessoa tiver pelo menos 20 anos, mas menos de 65, mostre uma mensagem dizendo que ela é adulto.
#• Se a pessoa tiver 65 anos ou mais, mostre uma mensagem dizendo que essa pessoa é idoso.

#5.7 – Fruta favorita: Faça uma lista de suas frutas favoritas e, então, escreva uma série de instruções if independentes que verifiquem se determinadas frutas estão em sua lista.
#• Crie uma lista com suas três frutas favoritas e chame-a de favorite_fruits.
#• Escreva cinco instruções if. Cada instrução deve verificar se uma determinada fruta está em sua lista. Se estiver, o bloco if deverá exibir uma frase, por exemplo, Você realmente gosta de bananas!


#RESPOSTA DOS EXERCICIOS
#5.3

#• Escreva uma instrução if para testar se a cor do alienígena é verde. 
# Se for, mostre uma mensagem informando que o jogador acabou de ganhar cinco pontos.

print("\nAdivinhe a cor do alien e ganhe pontos!")
alien_color = 'green'                                                       #Passou
if alien_color == 'green':
    print("A cor do alien é verde, você acabou de ganhar 5 pontos!")

# • Escreva uma versão desse programa em que o teste if passe e outro em que ele falhe. 

print("\nAdivinhe a cor do alien e ganhe pontos!")
alien_color = 'green'
if alien_color == 'red':                                                    #Falhou
    print('\nVocê acertou, a cor do alien é'+' '+alien_color)
else:
    print("falhou")
    
#5.4


#• Se a cor do alienígena for verde, mostre uma frase informando que o jogador acabou de ganhar cinco pontos por atingir o alienígena.
alien_color = 'green'
if alien_color == 'green':
    print("\nVocê acabou de ganhar 5 pontos por atingir o alienigena!")     #Executando bloco IF
else:
    print("Você acabou de ganhar 10 pontos!")

#• Escreva uma versão desse programa que execute o bloco if e outro que execute o bloco else.
                                                  
#• Se a cor do alienígena não for verde, mostre uma frase informando que o jogador acabou de ganhar dez pontos.    
alien_color = 'blue'
if alien_color == 'green':
    print("Você acabou de ganhar 5 pontos por atingir o alienigena!")       #Executando bloco Else
else:
    print("\nVocê acabou de ganhar 10 pontos!")
    
#5.5
print("\nAcerte um dos aliens para ganhar pontos!")
alien_color = 'green'
if alien_color == 'green':                                                      #Executando bloco IF
    print("Você acabou de ganhar 5 pontos por atingir o alienigena verde!")     
elif alien_color == 'yellow':
    print("Você acabou de ganhar 10 pontos, pois você acertou o  alien amarelo!")
else:
    print("Você acabou de receber 15 pontos, pois você acertou o alien vermelho")
    
print("\nAcerte um dos aliens para ganhar pontos!")
alien_color = 'yellow'
if alien_color == 'green':
    print("\nVocê acabou de ganhar 5 pontos por atingir o alienigena verde!")     
elif alien_color == 'yellow':                                                       #Executando bloco Elif
    print("Você acabou de ganhar 10 pontos, pois você acertou o  alien amarelo!")   
else:
    print("Você acabou de receber 15 pontos, pois você acertou o alien vermelho")
    
print("\nAcerte um dos aliens para ganhar pontos!")
alien_color = 'red'
if alien_color == 'green':
    print("\nVocê acabou de ganhar 5 pontos por atingir o alienigena verde!")    
elif alien_color == 'yellow':
    print("Você acabou de ganhar 10 pontos, pois você acertou o  alien amarelo!")
else:                                                                               #Executando bloco Else
    print("Você acabou de receber 15 pontos, pois você acertou o alien vermelho")

#5.6

print("\n")
age = 26
if age == 2:                    #• Se a pessoa tiver menos de 2 anos de idade, mostre uma mensagem dizendo que ela é um bebê.
    ages = 'bebe'               
elif age == 2 or age < 4:       #• Se a pessoa tiver pelo menos 2 anos, mas menos de 4, mostre uma mensagem dizendo que ela é uma criança.
    ages = 'criança'
elif age == 4 or age < 13:      #• Se a pessoa tiver pelo menos 4 anos, mas menos de 13, mostre uma mensagem dizendo que ela é um(a) garoto(a).
    ages = "garoto(a)"
elif age == 13 or age < 20:     #• Se a pessoa tiver pelo menos 13 anos, mas menos de 20, mostre uma mensagem dizendo que ela é um(a) adolescente.
    ages = 'adolescente'
elif age == 20 or age < 65:     #• Se a pessoa tiver pelo menos 20 anos, mas menos de 65, mostre uma mensagem dizendo que ela é adulto.
    ages = 'adulto(a)'
else:                           #• Se a pessoa tiver 65 anos ou mais, mostre uma mensagem dizendo que essa pessoa é idoso.
    ages = 'idoso(a)'
print("Você é um(a)"+" "+ages)

#5.7

frutas = ['banana', 'abacaxi', 'melancia', 'manga', 'morango']
print("\nMinhas 5 frutas favoritas são:")
if 'banana' in frutas:
    print(frutas[0])
    
if 'abacaxi' in frutas:
    print(frutas[1])
    
if 'melancia' in frutas:
    print(frutas[-2])
      
if 'manga' in frutas:
    print(frutas[-1])
    
favorite_fruits = ['abacaxi', 'banana', 'manga']               #• Crie uma lista com suas três frutas favoritas e chame-a de favorite_fruits.
#• Escreva cinco instruções if. Cada instrução deve verificar se uma determinada fruta está em sua lista. Se estiver, o bloco if deverá exibir uma frase, por exemplo, Você realmente gosta de bananas!
print('Minha lista top 3 de frutas favoritas')                  
if 'banana' in favorite_fruits:
    print('\nVocê gosta de banana e é uma de suas frutas favorita!')

if 'manga' in favorite_fruits:
    print("Você gsota de manga e tambem é uma de suas frutas preferidas")

if 'abacaxi' in favorite_fruits:
    print('Você gosta de abacaxi e é uma das suas top 3 frutas preferidas!!')

if 'melancia' in favorite_fruits:
    print("Fruta favorita?")
    
if 'morango' in favorite_fruits:
    print("delicia?")