#FAÇA VOCÊ MESMO
# 4.1 – Pizzas: Pense em pelo menos três tipos de pizzas favoritas. Armazene os nomes dessas pizzas e, então, utilize um laço for para exibir o nome de cada pizza.
#• Modifique seu laço for para mostrar uma frase usando o nome da pizza em vez de exibir apenas o nome dela. Para cada pizza, você deve ter uma linha na saída contendo uma frase simples como Gosto de pizza de pepperoni.
#• Acrescente uma linha no final de seu programa, fora do laço for, que informe quanto você gosta de pizza. A saída deve ser constituída de três ou mais linhas sobre os tipos de pizza que você gosta e de uma frase adicional, por exemplo, Eu realmente adoro pizza!

# 4.2 – Animais: Pense em pelo menos três animais diferentes que tenham uma característica em comum. Armazene os nomes desses animais em uma lista e, então, utilize um laço for para exibir o nome de cada animal.
#• Modifique seu programa para exibir uma frase sobre cada animal, por exemplo, Um cachorro seria um ótimo animal de estimação.
#• Acrescente uma linha no final de seu programa informando o que esses animais têm em comum. Você poderia exibir uma frase como Qualquer um desses animais seria um ótimo animal de estimação!


# RESPOSTAS DOS EXERCICIOS
# 4.1
pizzas = ["frango catupiry", "calabresa", "peperoni"]
for pizza in pizzas:
    print("Eu gosto muito de "+" "+str(pizza.title())+"\n"+"muito saborosa!!\n") 
     
print("A classica pizza de"+" "+str(pizzas[0].title())+" "+"é a minha favorita!"+"\n"+"A pizza de"+" "+str(pizzas[1].title())+" "+"é muito gostosa tambem!"+"\n"+"A de"+" "+str(pizzas[2].title())+" "+"não poderia me esquecer, é maravilhosa!!\n") #Fora do Laço For.

# 4.2 
animals = ["cachorro", "leão", "lobo"]   
qtd = len(animals)
for animal in animals:
    print("Um"+" "+animal.title()+" "+"é muito inteligente, e até mesmo adestravel!!\n")
print("O"+" "+str(animals[0].title())+" "+"é semelhante ao"+" "+str(animals[1].title())+" "+"no sentido de ser um quadrúpede, semelhante tambem ao"+" "+str(animals[-1].title())+" "+"porem todos eles tem a força diferencial sendo o leão o mais forte dos"+" "+str(qtd)+"\n"+"O cachorro é um ótimo animal de estimação! uma curiosidade é que algumas pessoas tem e adestram leões e lobos.")
    