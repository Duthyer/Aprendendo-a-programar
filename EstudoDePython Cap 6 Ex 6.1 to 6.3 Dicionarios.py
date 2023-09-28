#FAÇA VOCÊ MESMO
#6.1 – Pessoa: Use um dicionário para armazenar informações sobre uma pessoa que você conheça. Armazene seu primeiro nome, o sobrenome, a idade e a cidade em que ela vive. 
#Você deverá ter chaves como first_name, last_name, age e city. Mostre cada informação armazenada em seu dicionário.

#6.2 – Números favoritos: Use um dicionário para armazenar os números favoritos de algumas pessoas. Pense em cinco nomes e use-os como chaves em seu dicionário. 
#Pense em um número favorito para cada pessoa e armazene cada um como um valor em seu dicionário. 
#Exiba o nome de cada pessoa e seu número favorito. Para que seja mais divertido ainda, faça uma enquete com alguns amigos e obtenha alguns dados reais para o seu programa.

#6.3 – Glossário: Um dicionário Python pode ser usado para modelar um dicionário de verdade. No entanto, para evitar confusão, vamos chamá-lo de glossário.
#• Pense em cinco palavras relacionadas à programação que você conheceu nos capítulos anteriores. 
#Use essas palavras como chaves em seu glossário e armazene seus significados como valores.
#• Mostre cada palavra e seu significado em uma saída formatada de modo elegante. Você pode exibir a palavra seguida de dois-pontos e depois o seu significado, 
#ou apresentar a palavra em uma linha e então exibir seu significado indentado em uma segunda linha. 
#Utilize o caractere de quebra de linha (\n) para inserir uma linha em branco entre cada par palavra-significado em sua saída.

#RESPOSTAS DOS EXERCICIOS

#6.1

eu = {'Muller':'Miguel', 'idade':25, 'cidade':'Minas Gerais'} #Aqui é criado um dicionario {}.

print("Meu sobrenome é"+" "+eu['Muller'])                     #Aqui e na linha abaixo eu imprimo as informaçoes de cada objeto dentro do dicionario.
print("Minha idade é"+" "+str(eu['idade']))
print("Minha cidade é"+" "+eu['cidade'])

#6.2

numeros_fav = {'andrea':5, 'muller':10, 'maria':18,
               'nelio':20, 'jao':22,}

print("O número favorito da andrea é"+
    ' '+str(numeros_fav['andrea']))

print("O número favorito do muller é"+
    ' '+str(numeros_fav['muller']))

print("O número favorito da maria é"+
    ' '+str(numeros_fav['maria']))

print("O número favorito da nelio é"+
    ' '+str(numeros_fav['nelio']))

print("O número favorito do jao é"+
    ' '+str(numeros_fav['jao']))

#6.3
#• Pense em cinco palavras relacionadas à programação que você conheceu nos capítulos anteriores.
glossario = {
    'listas':'conjunto de códigos []', 'if':'estrutura de condição', 'for':'laço de repetição', 
    'tupla':'"lista" sem modificação ()', 'print':"comando de imprimir algo na tela"
    }

#• Mostre cada palavra e seu significado em uma saída formatada de modo elegante. Você pode exibir a palavra seguida de dois-pontos e depois o seu significado, 
#ou apresentar a palavra em uma linha e então exibir seu significado indentado em uma segunda linha.
print("\nListas é basicamente um:\n"+glossario['listas']+"."
      +"\nO if é uma:\n"+glossario['if']+"."
      +"\nO for é utilizado como:\n"+glossario['for']+"."      #Utilize o caractere de quebra de linha (\n) para inserir uma linha em branco entre cada par palavra-significado em sua saída.
      +"\nA tupla é basicamente uma:\n"+glossario['tupla']+"."
      +"\nO print é um:\n"+glossario['print']+"."
    )