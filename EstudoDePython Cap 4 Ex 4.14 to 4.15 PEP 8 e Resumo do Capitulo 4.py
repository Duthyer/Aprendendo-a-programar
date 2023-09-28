#FAÇA VOCÊ MESMO
#4.14 – PEP 8: Observe o guia de estilo da PEP 8 original em https://python.org/dev/peps/pep-0008/. Você não usará boa parte dele agora, mas pode ser interessante dar uma olhada.
#4.15 – Revisão de código: Escolha três programas que você escreveu neste capítulo e modifique-os para que estejam de acordo com a PEP 8:
#• Use quatro espaços para cada nível de indentação. Configure seu editor de texto para inserir quatro espaços sempre que a tecla TAB for usada, 
#caso ainda não tenha feito isso (consulte o Apêndice B para ver instruções sobre como fazê-lo).
#• Use menos de 80 caracteres em cada linha e configure seu editor para que mostre uma linha vertical na posição do caractere de número 80.
#• Não use linhas em branco em demasia em seus arquivos de programa.

#Resumo
#Neste capítulo aprendemos a trabalhar de modo eficiente com os elementos de uma lista. 
#Vimos como percorrer uma lista usando um laço for, como Python usa indentação para estruturar um programa e como evitar alguns erros comuns de indentação.
#Aprendemos a criar listas numéricas simples, além de conhecermos algumas operações que podem ser realizadas em listas numéricas. 
#Aprendemos a fatiar uma lista para trabalhar com um subconjunto de itens e a copiar listas de modo adequado usando uma fatia.
#Também conhecemos as tuplas, que oferecem um nível de proteção a um conjunto de valores que não deve ser alterado,
#e aprendemos a estilizar seu código cada vez mais complexo para facilitar sua leitura.

#RESPOSTAS DOS EXERCICIOS

# 4.15

#REVISÃO 4.1
pizzas = ["frango catupiry", "calabresa", "peperoni"]
for pizza in pizzas:
    print("Eu gosto muito de "+" "+str(pizza.title())+"\n"+"muito saborosa!!\n") 
     
print("A classica pizza de"+" "+str(pizzas[0].title())+" "+"é a minha favorita!"+"\n"+"A pizza de"+" "
      +str(pizzas[1].title())+" "+"é muito gostosa tambem!"+"\n"+"A de"+" "+str(pizzas[2].title())+" "
      +"não poderia me esquecer, é maravilhosa!!\n") #Fora do Laço For.

#REVISÃO 4.11
minha_pizzas = ["Calabresa", "Frango e catupiry", 
                "queijo ao molho tonho", "chocolate", "coxinha"
]

friend_pizzas = minha_pizzas[:] #criei uma outra variavel chamada friend_pizza, para armazenar ali as pizzas fav do meu amigo, e então atribui a ela a minha lista.
minha_pizzas.append("mostarda") #utilizando o append() acrescentei mostarda a minha lista de pizza.
friend_pizzas.append("caramelo") #utilizando o append() acescentei caramelo na lista do meu amigo.
print("Estas são as minhas pizzas favoritas: "
      +str(minha_pizzas).title()) # Aqui é mostrado a minha lista com a atribuição de mais um item.

for pizzasm in minha_pizzas:
    print(pizzasm)
print("\n")

#REVISÃO 4.13
print("Cardapio original\n") #Aqui é utilizado a tupla, na qual não é possivel adicionar um item a ela, nem modificar, apenas reescrevendo como exemplo abaixo.
buffet = ("frango acebolado", "picanha", "costelão de boi", 
          "tilapia", "bife de boi"
)          
#buffet [0] = "calamelo"  TypeError: 'tuple' object does not support item assignment
for carnes in buffet:
    print(carnes)

print("\nCardapio alterado\n")
buffet = ("frango acebolado", "picanha", "costelão de boi",
          "careca", "xifornix"
)          
for carnes in buffet:
    print(carnes)
    
    