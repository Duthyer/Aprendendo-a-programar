#FAÇA VOCÊ MESMO
#6.4 – Glossário 2: Agora que você já sabe como percorrer um dicionário com um laço, limpe o código do Exercício 6.3 (página 148), 
#substituindo sua sequência de instruções print por um laço que percorra as chaves e os valores do dicionário.
#Quando tiver certeza de que seu laço funciona, acrescente mais cinco termos de Python ao seu glossário. Ao executar seu programa novamente,
#essas palavras e significados novos deverão ser automaticamente incluídos na saída.

#6.5 – Rios: Crie um dicionário que contenha três rios importantes e o país que cada rio corta. Um par chave-valor poderia ser 'nilo': 'egito'.
#• Use um laço para exibir uma frase sobre cada rio, por exemplo, O Nilo corre pelo Egito.
#• Use um laço para exibir o nome de cada rio incluído no dicionário.
#• Use um laço para exibir o nome de cada país incluído no dicionário.

#6.6 – Enquete: Utilize o código em favorite_languages.py (página 150).
#• Crie uma lista de pessoas que devam participar da enquete sobre linguagem favorita. Inclua alguns nomes que já estejam no dicionário e outros que não estão.
#• Percorra a lista de pessoas que devem participar da enquete. Se elas já tiverem respondido à enquete, mostre uma mensagem agradecendo-lhes por responder. Se ainda não participaram da enquete, apresente uma mensagem convidando-as a responder.


#RESPOSTAS DOS EXERCICIOS
#6.4
glossario = {
    'listas':'conjunto de códigos []', 'if':'estrutura de condição', 'for':'laço de repetição', 
    'tupla':'"lista" sem modificação ()', 'print':"comando de imprimir algo na tela"
    }
#Abaixo é feito a adição de 5 nova(s) chave-valor ao dicionario.
glossario['or'] = 'ou'       
glossario['and'] = 'e'
glossario['for in'] = 'para (item) dentro de/em'
glossario['sorted()'] = 'ordenação temporaria alfabetica.'
glossario['set()'] = 'conjunto sem objetos duplicados'
#Abaixo é imprimido valor-chave contido no dicionario incluindo os novos adicionados.
for key, value in glossario.items(): #aqui usamos item() para solicitação do conjunto chave-valor
    print(key+": "+value)     

#6.5

#Rios: Crie um dicionário que contenha três rios importantes e o país que cada rio corta. Um par chave-valor poderia ser 'nilo': 'egito'.
print('\n')
rios = {
    'nilo':'Egito', 'amazonas':'Brasil',     
    'yangtze River':'China'
    }
#• Use um laço para exibir uma frase sobre cada rio, por exemplo, O Nilo corre pelo Egito.
for rio, city in rios.items():  #aqui usamos item() para solicitação do conjunto chave-valor
    print("O"+" "+rio.title()+" "+"corre pelo(a)"+" "+city)
#• Use um laço para exibir o nome de cada rio incluído no dicionário.
print('\n')
for rio in rios.keys():         #aqui solocitamos apenas a chave!
    print("Este é o rio"+" "+rio+"!")
#• Use um laço para exibir o nome de cada país incluído no dicionário.
print('\n')
for city in rios.values():      #aqui solicitamos apenas o valor.
    print("Este pais se chama"+" "+city+"!")

#6.6
print('\n')
#Enquete: Utilize o código em favorite_languages.py (página 150).
favorite_languages = {'jen': 'python', 'sarah': 'c',
                      'edward': 'ruby', 'phil': 'python',
                    }  
#• Crie uma lista de pessoas que devam participar da enquete sobre linguagem favorita. Inclua alguns nomes que já estejam no dicionário e outros que não estão.
pessoas = ['jubinha', 'toinho', 'julius',
           'sarah', 'edward',
           ]
#• Percorra a lista de pessoas que devem participar da enquete. Se elas já tiverem respondido à enquete, mostre uma mensagem agradecendo-lhes por responder
for names in favorite_languages.keys():
    if names in pessoas:
        print("Olá"+" "+names.title()+" "+"obrigado por responder a enquete!")
#• Se ainda não participaram da enquete, apresente uma mensagem convidando-as a responder.
print("\n")
for names in pessoas:
    if names not in favorite_languages:
        print("Olá"+" "+names.title()+" "+"venha participar de nossa enquete!")
        
       
 