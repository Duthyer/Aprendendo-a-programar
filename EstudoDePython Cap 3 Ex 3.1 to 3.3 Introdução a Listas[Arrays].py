# FAÇA VOCÊ MESMO
# Experimente criar estes programas pequenos para ter um pouco de experiência própria com listas em Python. 
# Você pode criar uma nova pasta para os exercícios de cada capítulo a fim de mantê-los organizados.
# 3.1 – Nomes: Armazene os nomes de alguns de seus amigos em uma lista chamada names. Exiba o nome de cada pessoa acessando cada elemento da lista, um de cada vez.

# 3.2 – Saudações: Comece com a lista usada no Exercício 3.1, mas em vez de simplesmente exibir o nome de cada pessoa, apresente uma mensagem a elas.
#O texto de cada mensagem deve ser o mesmo, porém cada mensagem deve estar personalizada com o nome da pessoa.

# 3.3 – Sua própria lista: Pense em seu meio de transporte preferido, como motocicleta ou carro, e crie uma lista que armazene vários exemplos.
# Utilize sua lista para exibir uma série de frases sobre esses itens, como “Gostaria de ter uma moto Honda”.


# RESPOSTAS DOS EXERCICIOS
# 3.1
names = ["teclado", "monitor", "mouse", "cpu", "headphone", "som", "extensão"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
print(names[5])
print(names[6])

# 3.2
names = ["teclado", "monitor", "mouse", "cpu", "headphone", "som", "extensão"]
print("Fundamental em um computador é o:"+" "+names[0])
print("Importate e necessario para a visualização é o:"+" "+names[1])
print("Importante e fundamental para mexer no computador é o:"+" "+names[2])
print("Processamento que fica na placa mãe que é:"+" "+names[3])
print("Utilizado para escutar músicas e afins de forma conectada ao ouvido é:"+" "+names[4])
print("Utilizado de forma aberta para escutar músicas e afins é o:"+" "+names[5])
print("Necessario e importante para distribuição de energia para o sistema é a :"+" "+names[6])

# 3.3
carros_favoritos = ["Mclaren GTR", "Ferrari 250 gto", "Mclaren P1 Gtr", "Paganni Zonda R", "Buggatti 'La Noire'"]
print("\nUm dos meus carros preferidos!"+" "+carros_favoritos[0])
print("Da mesma marca anterior o segundo mais preferido"+" "+carros_favoritos[2])
print("Carro antigo e muito bonito!"+" "+carros_favoritos[1])
print("Carro extremamente luxuoso e lindo!"+" "+carros_favoritos[-1])
print("Um esportivo incrivel e potente!"+" "+carros_favoritos[-2])


