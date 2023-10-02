#FAÇA VOCÊ MESMO
#Salve cada um dos exercícios a seguir em um arquivo separado com um nome como name_cases.py. Se não souber o que fazer, 
#descase um pouco ou consulte as sugestões que estão no Apêndice C.

#2.3 – Mensagem pessoal: Armazene o nome de uma pessoa em uma variável e apresente uma mensagem a essa pessoa. Sua mensagem deve ser simples, 
#como “Alô Eric, você gostaria de aprender um pouco de Python hoje?”.

#2.4 – Letras maiúsculas e minúsculas em nomes: Armazene o nome de uma pessoa em uma variável e então apresente o nome dessa pessoa em letras minúsculas, 
#em letras maiúsculas e somente com a primeira letra maiúscula.

#2.5 – Citação famosa: Encontre uma citação de uma pessoa famosa que você admire. 
#Exiba a citação e o nome do autor. Sua saída deverá ter a aparência a seguir, incluindo as aspas: Albert Einstein certa vez disse: 
#“Uma pessoa que nunca cometeu um erro jamais tentou nada novo.”

#2.6 – Citação famosa 2: Repita o Exercício 2.5, porém, desta vez, armazene o nome da pessoa famosa em uma variável chamada famous_person. 
# Em seguida, componha sua mensagem e armazene-a em uma nova variável chamada message. Exiba sua mensagem.

# 2.7 – Removendo caracteres em branco de nomes: Armazene o nome de uma pessoa e inclua alguns caracteres em branco no início e no final do nome.
#Lembre-se de usar cada combinação de caracteres, "\t" e "\n", pelo menos uma vez.
#Exiba o nome uma vez, de modo que os espaços em branco em torno do nome sejam mostrados. Em seguida, exiba o nome usando cada uma das três funções de remoção de espaços: 
#lstrip(), rstrip() e strip().

# RESPOSTAS DOS EXERCICIOS
# 2.3
nome = "Aleki"
message = "Olá" + " " + nome + " " + "Cê ta bão mano??"
print(message)

# 2.4
nome = "Muriel"
print(nome.lower())
print(nome.upper())
print(nome.title())

# 2.5
print("Um Ótario certa vez disse: 'Uma pessoa que tem uma canoa, pode ser vagarosamente grande em suas pequenas coisas!' ")

# 2.6
nome = "Ótario"
citacao = "certa vez disse: 'Uma pessoa que tem uma canoa, pode ser vagarosamente grande em suas pequenas coisas!' "
print("Um" + " "+ nome + " " + citacao)

# 2.7
nome = "\t Cú de burro "
print(nome)
print(nome.lstrip()) #tira somente lado esquerdo em branco.
print(nome.rstrip()) #tira somente lado direito em branco.
print(nome.strip()) #tira ambos espaços em branco.
