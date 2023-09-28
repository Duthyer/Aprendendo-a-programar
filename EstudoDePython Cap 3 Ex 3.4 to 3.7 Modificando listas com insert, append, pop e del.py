# FAÇA VOCÊ MESMO

# Os exercícios a seguir são um pouco mais complexos que aqueles do Capítulo 2, porém darão a você a oportunidade de usar listas de todas as formas descritas.
# 3.4 – Lista de convidados: Se pudesse convidar alguém, vivo ou morto, para o jantar, quem você convidaria? 
#Crie uma lista que inclua pelo menos três pessoas que você gostaria de convidar para jantar. Em seguida, utilize sua lista para exibir uma mensagem para cada pessoa, 
#convidando-a para jantar.

# 3.5 – Alterando a lista de convidados: Você acabou de saber que um de seus convidados não poderá comparecer ao jantar, portanto será necessário enviar um novo conjunto de convites. 
#Você deverá pensar em outra pessoa para convidar.
#• Comece com seu programa do Exercício 3.4. Acrescente uma instrução print no final de seu programa, especificando o nome do convidado que não poderá comparecer.
#• Modifique sua lista, substituindo o nome do convidado que não poderá comparecer pelo nome da nova pessoa que você está convidando.
#• Exiba um segundo conjunto de mensagens com o convite, uma para cada pessoa que continua presente em sua lista.


# 3.6 – Mais convidados: Você acabou de encontrar uma mesa de jantar maior, portanto agora tem mais espaço disponível. Pense em mais três convidados para o jantar.
#• Comece com seu programa do Exercício 3.4 ou do Exercício 3.5. Acrescente uma instrução print no final de seu programa informando às pessoas que você encontrou uma mesa de jantar 
#maior.
#• Utilize insert() para adicionar um novo convidado no início de sua lista.
#• Utilize insert() para adicionar um novo convidado no meio de sua lista.
#• Utilize append() para adicionar um novo convidado no final de sua lista.
#• Exiba um novo conjunto de mensagens de convite, uma para cada pessoa que está em sua lista.

# 3.7 – Reduzindo a lista de convidados: Você acabou de descobrir que sua nova mesa de jantar não chegará a tempo para o jantar e tem espaço para somente dois convidados.

#• Comece com seu programa do Exercício 3.6. Acrescente uma nova linha que mostre uma mensagem informando que você pode convidar apenas duas pessoas para o jantar.
#• Utilize pop() para remover os convidados de sua lista, um de cada vez, até que apenas dois nomes permaneçam em sua lista. 
#Sempre que remover um nome de sua lista, mostre uma mensagem a essa pessoa, permitindo que ela saiba que você sente muito por não poder convidá-la para o jantar.
#• Apresente uma mensagem para cada uma das duas pessoas que continuam na lista, permitindo que elas saibam que ainda estão convidadas.
#• Utilize del para remover os dois últimos nomes de sua lista, de modo que você tenha uma lista vazia. 
#Mostre sua lista para garantir que você realmente tem uma lista vazia no final de seu programa.


# RESPOSTAS DOS EXERCICIOS
# 3.4
convite_jantar = ["Joaquim", "Maria", "Joao"]
print("Te convido para um jantar em familia esta noite!"+" "+convite_jantar[0])
print("Te convido para um jantar em familia esta noite!"+" "+convite_jantar[1])
print("Te convido para um jantar em familia esta noite!"+" "+convite_jantar[2])

# 3.5
convite_jantar = ["Joaquim", "Maria", "Joao"]
print("\nTe convido para um jantar em familia esta noite!"+" "+convite_jantar[0])
print("Te convido para um jantar em familia esta noite!"+" "+convite_jantar[1])
#• Acrescente uma instrução print no final de seu programa, especificando o nome do convidado que não poderá comparecer.
print("O "+" "+convite_jantar[2]+" "+"Não pode comparecer ao jantar") 


#• Modifique sua lista, substituindo o nome do convidado que não poderá comparecer pelo nome da nova pessoa que você está convidando.
convite_jantar = ["Joaquim", "Maria", "Maria Luiza"] 

#• Exiba um segundo conjunto de mensagens com o convite, uma para cada pessoa que continua presente em sua lista.
print("\nTe convido para um jantar em familia esta noite!"+" "+convite_jantar[0])
print("Te convido para um jantar em familia esta noite!"+" "+convite_jantar[1])   
print("Te convido para um jantar em familia esta noite!"+" "+convite_jantar[2])

# 3.6
#• Acrescente uma instrução print no final de seu programa informando às pessoas que você encontrou uma mesa de jantar 
#maior.
print("\nConsegui encontrar uma mesa de jantar maior!!") 
convite_jantar = ["Joaquim", "Maria", "Maria Luiza"]
convite_jantar.insert(0, 'Enzo') #• Utilize insert() para adicionar um novo convidado no início de sua lista.
convite_jantar.insert(2, "Rayca") #• Utilize insert() para adicionar um novo convidado no meio de sua lista.
convite_jantar.append("Helisson") #• Utilize append() para adicionar um novo convidado no final de sua lista.

#• Exiba um novo conjunto de mensagens de convite, uma para cada pessoa que está em sua lista.
print("\nTe convido para um jantar em familia esta noite!"+" "+convite_jantar[0])
print("Te convido para um jantar em familia esta noite!"+" "+convite_jantar[1])
print("Te convido para um jantar em familia esta noite!"+" "+convite_jantar[2])
print("Te convido para um jantar em familia esta noite!"+" "+convite_jantar[3])
print("Te convido para um jantar em familia esta noite!"+" "+convite_jantar[4])
print("Te convido para um jantar em familia esta noite!"+" "+convite_jantar[5])

# 3.7
#• Comece com seu programa do Exercício 3.6. 
convite_jantar = ["Joaquim", "Maria", "Maria Luiza"]
convite_jantar.insert(0, 'Enzo')
convite_jantar.insert(2, "Rayca")
convite_jantar.append('Helisson')
print("\nTe convido para um jantar em familia esta noite!"+" "+convite_jantar[0])
print("Te convido para um jantar em familia esta noite!"+" "+convite_jantar[1])
print("Te convido para um jantar em familia esta noite!"+" "+convite_jantar[2])
print("Te convido para um jantar em familia esta noite!"+" "+convite_jantar[3])
print("Te convido para um jantar em familia esta noite!"+" "+convite_jantar[4])
print("Te convido para um jantar em familia esta noite!"+" "+convite_jantar[5])

#• Acrescente uma nova linha que mostre uma mensagem informando que você pode convidar apenas duas pessoas para o jantar.
print("Só foi possivel convidar duas pessoas") 

#• Utilize pop() para remover os convidados de sua lista, um de cada vez, até que apenas dois nomes permaneçam em sua lista. 
#Sempre que remover um nome de sua lista, mostre uma mensagem a essa pessoa, permitindo que ela saiba que você sente muito por não poder convidá-la para o jantar.
convite_1 = convite_jantar.pop(0)
print("Infelizmente não pude te receber no jantar"+" "+convite_1)
convite_2 = convite_jantar.pop(1)
print("Me desculpe, na proxima vez eu te chamo"+" "+convite_2)
convite_3 = convite_jantar.pop(-2)
print("Não foi dessa vez, mas na proxima eu te convido em, me desculpe"+" "+convite_3)
convite_4 = convite_jantar.pop(-1)
print("Ai foi mal man, na proxima eu te convido beleza"+" "+convite_4+"?")

#• Apresente uma mensagem para cada uma das duas pessoas que continuam na lista, permitindo que elas saibam que ainda estão convidadas.
print("Voce ainda esta convidado em!"+" "+convite_jantar[0])
print("Voce ainda esta convidada em!"+" "+convite_jantar[1])

#• Utilize del para remover os dois últimos nomes de sua lista, de modo que você tenha uma lista vazia. 
del convite_jantar[0]
del convite_jantar[-1]

#• Mostre sua lista para garantir que você realmente tem uma lista vazia no final de seu programa.
print("\n"+str(convite_jantar))














