#FAÇA VOCÊ MESMO
# 4.10 – Fatias: Usando um dos programas que você escreveu neste capítulo, acrescente várias linhas no final do programa que façam o seguinte: 
#• Exiba a mensagem Os três primeiros itens da lista são: Em seguida, use uma fatia para exibir os três primeiros itens da lista desse programa.
#• Exiba a mensagem Três itens do meio da lista são:. Use uma fatia para exibir os três itens do meio da lista.
#• Exiba a mensagem Os três últimos itens da lista são:. Use uma fatia para exibir os três últimos itens da lista.

# 4.11 – Minhas pizzas, suas pizzas: Comece com seu programa do Exercício 4.1
#(página 97). Faça uma cópia da lista de pizzas e chame-a de friend_pizzas.
#Então faça o seguinte: • Adicione uma nova pizza à lista original.
#• Adicione uma pizza diferente à lista friend_pizzas.
#• Prove que você tem duas listas diferentes. Exiba a mensagem Minhas pizzas favoritas são:; em seguida, utilize um laço for para exibir a primeira lista.
#Exiba a mensagem As pizzas favoritas de meu amigo são:; em seguida, utilize um laço for para exibir a segunda lista. 
#Certifique-se de que cada pizza nova esteja armazenada na lista apropriada.

# 4.12 – Mais laços: Todas as versões de foods.py nesta seção evitaram usar laços for para fazer exibições a fim de economizar espaço. 
#Escolha uma versão de foods.py e escreva dois laços for para exibir cada lista de comidas.

# RESPOSTAS DOS EXERCICIOS
# 4. 10
pizzas = ["Calabresa", "Frango e catupiry", "queijo ao molho tonho", "chocolate", "coxinha"]
print("Os três primeiros itens da lista são:"+str(pizzas[:3]).title()+"\n") #utilização da fatia : para definir quais são os itens, neste caso os 3 primeiros que eu quero que apareça.
print("Os três itens do meio da lista são:"+str(pizzas[1:4]).title()+"\n")
print("Os três ultimos da lista são:"+str(pizzas[-3:]).title()+"\n")

# 4.11
minha_pizzas = ["Calabresa", "Frango e catupiry", "queijo ao molho tonho", "chocolate", "coxinha"]
friend_pizzas = minha_pizzas[:] #criei uma outra variavel chamada friend_pizza, para armazenar ali as pizzas fav do meu amigo, e então atribui a ela a minha lista.
minha_pizzas.append("mostarda") #utilizando o append() acrescentei mostarda a minha lista de pizza.
friend_pizzas.append("caramelo") #utilizando o append() acescentei caramelo na lista do meu amigo.
print("Estas são as minhas pizzas favoritas: "+str(minha_pizzas).title()) # Aqui é mostrado a minha lista com a atribuição de mais um item.
for pizzasm in minha_pizzas:
    print(pizzasm)
print("\n")

print("Estas são as pizzas favoritas do meu amigo."+str(friend_pizzas).title()) #Aqui é mostrado a lista do meu amigo, com atribuição a mais um item diferente da minha lista.Mostrando que são duas listas com adições diferentes.
for pizzaa in friend_pizzas:
    print(pizzaa)
print("\n")

# 4.12
print("My foods are:")
my_foods = ['pizza', 'falafel', 'carrot cake']  #1° listas
for foods in my_foods:
    print(foods)

print("\n")                        #Aqui duas listas diferentes foram criadas, não entendi o exercicio muito bem, revisar mais tarde.
    
print("My friends food are:")
friends_food = ['pizza', 'falafel', 'carrot cake' , 'ice cream', 'cogumelous'] #2° lista
for foods in friends_food:
    print(foods)



