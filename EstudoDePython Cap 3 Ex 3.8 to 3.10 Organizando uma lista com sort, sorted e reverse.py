#FAÇA VOCÊ MESMO
# 3.8 – Conhecendo o mundo: Pense em pelo menos cinco lugares do mundo que você gostaria de visitar.
#• Armazene as localidades em uma lista. Certifique-se de que a lista não esteja em ordem alfabética.
#• Exiba sua lista na ordem original. Não se preocupe em exibir a lista de forma elegante; basta exibi-la como uma lista Python pura.
#• Utilize sorted() para exibir sua lista em ordem alfabética, sem modificar a lista propriamente dita.
#• Mostre que sua lista manteve sua ordem original exibindo-a.
#• Utilize sorted() para exibir sua lista em ordem alfabética inversa sem alterar a ordem da lista original.
#• Mostre que sua lista manteve sua ordem original exibindo-a novamente.
#• Utilize reverse() para mudar a ordem de sua lista. Exiba a lista para mostrar que sua ordem mudou.
#• Utilize reverse() para mudar a ordem de sua lista novamente. Exiba a lista para mostrar que ela voltou à sua ordem original.
#• Utilize sort() para mudar sua lista de modo que ela seja armazenada em ordem alfabética. Exiba a lista para mostrar que sua ordem mudou.
#• Utilize sort() para mudar sua lista de modo que ela seja armazenada em ordem alfabética inversa. Exiba a lista para mostrar que sua ordem mudou.

# 3.9 – Convidados para o jantar: Trabalhando com um dos programas dos Exercícios de 3.4 a 3.7 
#(páginas 80 e 81), use len() para exibir uma mensagem informando o número de pessoas que você está convidando para o jantar.

# 3.10 – Todas as funções: Pensa em algo que você poderia armazenar em uma lista.
#Por exemplo, você poderia criar uma lista de montanhas, rios, países, cidades, idiomas ou qualquer outro item que quiser. 
#Escreva um programa que crie uma lista contendo esses itens e então utilize cada função apresentada neste capítulo pelo menos uma vez.


# RESPOSTAS DOS EXERCICIOS
# 3.8
visitar_paises = ['estados unidos', 'suécia', 'indonesia', 'canada', 'israel']
#• Armazene as localidades em uma lista. Certifique-se de que a lista não esteja em ordem alfabética.
print("\n"+str(visitar_paises)) 

#• Utilize sorted() para exibir sua lista em ordem alfabética de forma temporaria , sem modificar a lista propriamente dita.
print("\n"+str(sorted(visitar_paises))) 

 #• mostre que sua lista manteve sua ordem original exibindo-a.
print("\n"+str(visitar_paises)) 

#• Utilize sorted() para exibir sua lista em ordem alfabética temporaria inversa sem alterar a ordem da lista original.
print("\n"+str(sorted(visitar_paises, reverse=True))) 

#• Mostre que sua lista manteve sua ordem original exibindo-a novamente.
print("\n"+str(visitar_paises))

#• Utilize reverse() para mudar a ordem de sua lista. Exiba a lista para mostrar que sua ordem mudou.
visitar_paises.reverse() 
print("\n"+str(visitar_paises))

#• Utilize reverse() para mudar a ordem de sua lista novamente. Exiba a lista para mostrar que ela voltou à sua ordem original.
visitar_paises.reverse() 
print("\n"+str(visitar_paises))

#• Utilize sort() para mudar sua lista de modo que ela seja permanente armazenada em ordem alfabética. Exiba a lista para mostrar que sua ordem mudou.
visitar_paises.sort() 
print("\n"+str(visitar_paises))

#• Utilize sort() para mudar sua lista de modo que ela seja permanente armazenada em ordem alfabética inversa. Exiba a lista para mostrar que sua ordem mudou.
visitar_paises.sort(reverse=True)
print("\n"+str(visitar_paises))


#3.9

convite_jantar = ["Joaquim", "Maria", "Joao"]
print("\nTe convido para um jantar em familia esta noite!"+" "+convite_jantar[0])
print("Te convido para um jantar em familia esta noite!"+" "+convite_jantar[1])
print("Te convido para um jantar em familia esta noite!"+" "+convite_jantar[2])
tamanho = len(convite_jantar) #• use len() para exibir uma mensagem informando o número de pessoas que você está convidando para o jantar.
print("estou convidando "+" "+str(tamanho)+"pessoas para jantar!") 

#3.10

aliens = ["alien", "mini alien", "mini alien", "mini alien", "boss alien", "alien"]
print("\nEstes são os inimigos "+" "+str(aliens))
aliens_count = len(aliens) # len é utilizado para saber o tamanho da lista.
print("\nNo total existem "+str(aliens_count)+" "+"inimigos")
print("Estes são os inimigos em ordem alfabetica temporaria:"+str(sorted(aliens))) # Ordenando uma lista temporariamente com a função sorted() Para preservar a ordem original de uma lista
print("Estes são os inimigos em ordem alfabetica reversa temporaria:"+str(sorted(aliens, reverse=True)))
aliens.reverse()
print("Estes são os inimigos em ordem reversa padrão (permanente):"+str(aliens))
aliens.reverse()
print("Estes são os inimigos em ordem padrão (utilizei o .reverse() novamente):"+str(aliens))
print("\nVamos adicionar mais 4 inimigos para o jogo")
aliens.insert(0, "giant alien") # Você pode adicionar um novo elemento em qualquer posição de sua lista usando o método insert().
aliens.insert(3, "sword alien")
aliens.append("dragon alien") # append() facilita criar listas dinamicamente, e é utilizado para adicionar o objeto a ultima posição da lista.
aliens.insert(5, "scorpion alien")
print("Esta é a lista incluindo os novos 4 alienigenas no jogo!!")
print(aliens)
print("\nEstes são os novos aliens:")
print(aliens[0])
print(aliens[3])
print(aliens[-1])
print(aliens[5])
print("totalizando mais 4 inimigos para o game!")

morto = aliens.pop(-1)# você pode usar pop() para remover um item de qualquer posição em uma lista se incluir o índice do item que você deseja remover entre parênteses.
morto2 = aliens.pop(3) 
print("\nDois inimigos foram mortos, são eles:")
print(morto)
print(morto2)

aliens_count = len(aliens) #contagem da lista

print("\nEstes são os inimigos restantes"+" "+str(aliens)+" "+"totalizando"+" "+str(aliens_count)+" "+"inimigos")
aliens.sort() # O método sort() altera a ordem da lista de forma permanente.
print("Inimigos em ordem alfabetica permanente"+" "+str(aliens))

print("Todos os inimigos foram derrotados!")

del aliens [0] # Se a posição do item que você quer remover de uma lista for conhecida, a instrução del poderá ser usada.
del aliens [1]
del aliens [2]
del aliens [3]
del aliens [-3]
del aliens [-2]
del aliens [-1]
aliens.remove("alien")# O método remove() apaga apenas a primeira ocorrência do valor que você especificar.
# Se houver a possibilidade de o valor aparecer mais de uma vez na lista, será necessário usar um laço para determinar se todas as ocorrências desse valor foram removidas.
print("A lista de inimigos ficou assim: "+str(aliens))


