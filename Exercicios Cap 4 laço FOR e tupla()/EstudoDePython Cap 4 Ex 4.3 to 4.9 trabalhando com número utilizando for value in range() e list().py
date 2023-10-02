#FAÇA VOCÊ MESMO
# 4.3 – Contando até vinte: Use um laço for para exibir os números de 1 a 20, incluindo-os.

# 4.4 – Um milhão: Crie uma lista de números de um a um milhão e, então, use um laço for para exibir os números. 
#(Se a saída estiver demorando demais, interrompa pressionando CTRL-C ou feche a janela de saída.) 

# 4.5 – Somando um milhão: Crie uma lista de números de um a um milhão e, em seguida, use min() e max() para garantir que sua lista realmente começa em um e termina em um milhão.
#Além disso, utilize a função sum() para ver a rapidez com que Python é capaz de somar um milhão de números.

# 4.6 – Números ímpares: Use o terceiro argumento da função range() para criar uma lista de números ímpares de 1 a 20. Utilize um laço for para exibir todos os números.
# 4.7 – Três: Crie uma lista de múltiplos de 3, de 3 a 30. Use um laço for para exibir os números de sua lista.

# 4.8 – Cubos: Um número elevado à terceira potência é chamado de cubo. Por exemplo, o cubo de 2 é escrito como 2**3 em Python. 
#Crie uma lista dos dez primeiros cubos (isto é, o cubo de cada inteiro de 1 a 10), e utilize um laço for para exibir o valor de cada cubo.

# 4.9 – Comprehension de cubos: Use uma list comprehension para gerar uma lista dos dez primeiros cubos.

# RESPOSTAS DOS EXERCICIOS
# 4.3
for value in range(1,21): #value é o nome dado a variavel na qual esta guardando os valores de range "para cada valor no alcance de ... :".
    print(value)  
    
# 4.4
numbers = list(range(1,1001)) #Aqui foi criado uma Lista/Array especifica para números, utilizando o list e o range.
for number in numbers: #"Para cada número em números ..."
    print(number)

# 4.5
numbers = list(range(1,1001)) #foi criado uma lista especifica para números, utilizando o list e range.
for number in numbers: #aqui é utilizado o laço for com a variavel number contida dentro da lista numbers que no caso é cada objeto contido na lista numbers(number)
   print(number)

print(min(numbers)) #Minimo de números obtidos.
print(max(numbers)) #Maximo de números obtidos.
print(sum(numbers)) #A soma de todos os números obtidos.

# 4.6

numbers_imp = list(range(2,21,2)) #aqui a lista de números começa com número 2, e ao longo da lista é somado o número 2 (terceiro parametro de range) a cada número até chegar no 20.
for number in numbers_imp:
    print(number)

# 4.7
multiply_3 = list(range(3,31))
for number in multiply_3:
    number *= 3        #Aqui foi utilizado a variavel para a multiplicação de cada número por 3.
    print(number)

# 4.8
cubos = []
for cubo in range(1,11):
    value = cubo ** 3
    cubos.append(value) #utilizado o append() para acrescentação de cubo para a lista cubos.
    print(value)
print(str(cubos)+"\n") #checando se minha lista esta vazia.

# 4.9
cubes = [cube ** 3 for cube in range(1,11)] #Aqui é utilizado o List Comprehension.
for cube in cubos: 
    print(cube) #Aqui é imprimido o valor de cada item contido na lista de forma vertical.
print(cubos) #Aqui é imprimido a lista da forma que ela é.
   
   
    
    
    



