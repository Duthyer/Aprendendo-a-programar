#FAÇA VOCÊ MESMO

#6.7 – Pessoas: Comece com o programa que você escreveu no Exercício 6.1
#(página 147). Crie dois novos dicionários que representem pessoas diferentes e armazene os três dicionários em uma lista chamada people. Percorra sua lista de pessoas com um laço. À medida que percorrer a lista, apresente tudo que você sabe sobre cada pessoa.

#6.8 – Animais de estimação: Crie vários dicionários, em que o nome de cada dicionário seja o nome de um animal de estimação.
# Em cada dicionário, inclua o tipo do animal e o nome do dono. Armazene esses dicionários em uma lista chamada pets.
# Em seguida, percorra sua lista com um laço e, à medida que fizer isso, apresente tudo que você sabe sobre cada animal de estimação.

#6.9 – Lugares favoritos: Crie um dicionário chamado favorite_places. Pense em três nomes para usar como chaves do dicionário e armazene de um a três 149
#lugares favoritos para cada pessoa. Para deixar este exercício um pouco mais interessante, peça a alguns amigos que nomeiem alguns de seus lugares favoritos.
#Percorra o dicionário com um laço e apresente o nome de cada pessoa e seus lugares favoritos.

#6.10 – Números favoritos: Modifique o seu programa do Exercício 6.2 (página 147) para que cada pessoa possa ter mais de um número favorito.
# Em seguida, apresente o nome de cada pessoa, juntamente com seus números favoritos.

#6.11 – Cidades: Crie um dicionário chamado cities. Use os nomes de três cidades como chaves em seu dicionário.
# Crie um dicionário com informações sobre cada cidade e inclua o país em que a cidade está localizada, a população aproximada e um fato sobre essa cidade. As chaves do dicionário de cada cidade devem ser algo como country, population e fact. Apresente o nome de cada cidade e todas as informações que você armazenou sobre ela.

#6.12 – Extensões: Estamos trabalhando agora com exemplos complexos o bastante para poderem ser estendidos de várias maneiras.
# Use um dos programas de exemplo deste capítulo e estenda-o acrescentando novas chaves e valores, alterando o contexto do programa ou melhorando a formatação da saída.


#RESPOSTAS DOS EXERCICIOS
#6.7
#Pessoas: Comece com o programa que você escreveu no Exercício 6.1
pessoa_eu = {'nome':'müller', 'idade':25, 'cidade':'Minas Gerais'} #Aqui é criado um dicionario {}.
#abaixo é imprimido a informação contido no dicionario, sendo eles chaves-valore.
print("Meu sobrenome é"+" "+pessoa_eu['nome'])                     
print("Minha idade é"+" "+str(pessoa_eu['idade']))
print("Minha cidade é"+" "+pessoa_eu['cidade']+"\n") 

#abaixo é criado mais 2 novos dicionarios e uma lista guardando os três dicionarios.
pessoa_1 = {'nome':'julia', 'idade':22,
            'cidade':'santa catarina'
            }
pessoa_2 = {'nome':'celmo', 'idade':29,
            'cidade':'amazonas'
            }
people = [pessoa_eu, pessoa_1, pessoa_2]

#aqui é utilizado um laço for para cada pessoa em people:
for pessoa in people:
#Abaixo temos a variavel pessoa representando cada dicionario da lista,e em seguide cada chave contida neste dicionario, nos retornando o valor dela.  
    print("O nome da pessoa é"+" "+pessoa['nome'].title()+
          " "+"a idade é"+" "+str(pessoa['idade'])+
          " "+"e a cidade é"+" "+pessoa['cidade'].title()
          )

#6.8 
#Crie vários dicionários, em que o nome de cada dicionário seja o nome de um animal de estimação.
# Em cada dicionário, inclua o tipo do animal e o nome do dono.
luthier = {'tipo do animal':"cachorro",
           'nome do dono(a)':"müller"
           }

medy = {'tipo do animal':"coelho",
        'nome do dono(a)':"maria"
        }

arara = {'tipo do animal':"passaro",
         'nome do dono(a)':"odair"
         }
#Armazene esses dicionários em uma lista chamada pets.
pets = [luthier, arara, medy]
print('\n')
# Em seguida, percorra sua lista com um laço e, à medida que fizer isso, apresente tudo que você sabe sobre cada animal de estimação
for pet in pets:
    print("este é um animal do tipo"+" "+
          pet['tipo do animal']+
          " "+"e o nome do dono(a) é"+
          " "+pet['nome do dono(a)'].title()
          )

#6.9
#Crie um dicionário chamado favorite_places
#Pense em três nomes para usar como chaves do dicionário e armazene de um a três 149
#lugares favoritos para cada pessoa.
favorite_places = {'müller':["eua", "suiça"],
                   'maria':["interior de minas", "australia"],
                   'nelio':["italia", "canada"]
                   }
#Percorra o dicionário com um laço e apresente o nome de cada pessoa e seus lugares favoritos.
for name, info in favorite_places.items():  #O info representa cada lista de uma chave.
    print("\nO lugar favorito do(a)"+
          " "+name.title()+" "+"é:\n"
          )
    for infos in info:  #infos é a variavel criada para cada valor dentro de cada lista, no caso representando os valores de cada dicionario.
        print(infos)
 
#6.10 
#Números favoritos: Modifique o seu programa do Exercício 6.2 para que cada pessoa possa ter mais de um número favorito.      
numeros_fav = {'andrea':[5,18], 'muller':[10,26],
               'maria':[18,34], 'nelio':[20,49],
               'jao':[22,52], 'adilson':[10,7]
               }
#Em seguida, apresente o nome de cada pessoa, juntamente com seus números favoritos. 
for name, fav_number in numeros_fav.items(): #Aqui utilizamos name para representar cada chave contida no dicionario.
    print("O nome dele(a) é"+" "+name.title()+
          " "+"e seu número favorito é"
          ) 
    for fav_numbers in fav_number:  #fav_number representa a lista de cada chave, e fav_numbers cada valor contido na lista fav_number.
        print(fav_numbers)


#6.11 
#Cidades: Crie um dicionário chamado cities.
#Crie um dicionário chamado cities.     
#Crie um dicionário com informações sobre cada cidade e inclua o país em que a cidade está localizada, a população aproximada e um fato sobre essa cidade. 
#Use os nomes de três cidades como chaves em seu dicionário. 
#Abaixo criamos dicionarios dentro de um dicionario.
cities = {'minas gerais':{'pais':"brasil", 'população':"11 milhoes", 'fato':"melhor gastronomia"},      
          'los angels':{'pais':"estados unidos", 'população':"3 milhoes", 'fato':"cidade rica e empoderada!"},
          'jerusalém':{'pais':"israel", 'população':"700 mil", 'fato':"é uma cidade santa!", }
          } 

# Apresente o nome de cada cidade e todas as informações que você armazenou sobre ela.
for citie, citie_info in cities.items():
    print(
        "O nome da cidade é"+" "+citie.title()+", "+"o pais é"+ #citie é a Chave de cada dicionario.
        " "+citie_info['pais'].title()+", "+"população aproximada de"+ #citie_info é um valor de cada chave.
        " "+citie_info['população']+", "+"um fato sobre a cidade"+" "+citie_info['fato']
        )


        
    
