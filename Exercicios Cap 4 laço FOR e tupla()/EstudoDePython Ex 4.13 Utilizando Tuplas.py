#FAÇA VOCÊ MESMO
#4.13 – Buffet: Um restaurante do tipo buffet oferece apenas cinco tipos básicos de comida. Pense em cinco pratos simples e armazene-os em uma tupla.
#• Use um laço for para exibir cada prato oferecido pelo restaurante.
#• Tente modificar um dos itens e cerifique-se de que Python rejeita a mudança.
#• O restaurante muda seu cardápio, substituindo dois dos itens com pratos diferentes. Acrescente um bloco de código que reescreva a tupla e, em seguida, 
#use um laço for para exibir cada um dos itens do cardápio revisado.

#RESPOSTAS DOS EXERCICIOS
#4.13
print("Cardapio original\n") 
buffet = ("frango acebolado", "picanha", "costelão de boi", "tilapia", "bife de boi")#Aqui é utilizado a tupla, na qual não é possivel adicionar um item a ela, nem modificar, apenas reescrevendo como exemplo abaixo.
#buffet [0] = "calamelo"  TypeError: 'tuple' object does not support item assignment
for carnes in buffet:
    print(carnes)

print("\nCardapio alterado\n")
buffet = ("frango acebolado", "picanha", "costelão de boi", "careca", "xifornix")
for carnes in buffet:
    print(carnes)

