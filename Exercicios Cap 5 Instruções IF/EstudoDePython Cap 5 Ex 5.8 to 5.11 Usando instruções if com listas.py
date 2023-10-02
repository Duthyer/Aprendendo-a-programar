#FAÇA VOCÊ MESMO
#5.8 – Olá admin: Crie uma lista com cinco ou mais nomes de usuários, incluindo o nome 'admin'. 
#Suponha que você esteja escrevendo um código que exibirá uma saudação a cada usuário depois que eles fizerem login em um site.
#Percorra a lista com um laço e mostre uma saudação para cada usuário: 
# • Se o nome do usuário for 'admin', mostre uma saudação especial, por exemplo, Olá admin, gostaria de ver um relatório de status?
# • Caso contrário, mostre uma saudação genérica, como Olá Eric, obrigado por fazer login novamente.

#5.9 – Sem usuários: Acrescente um teste if em hello_admin.py para garantir que a lista de usuários não esteja vazia.
#• Se a lista estiver vazia, mostre a mensagem Precisamos encontrar alguns usuários!
#• Remova todos os nomes de usuário de sua lista e certifique-se de que a mensagem correta seja exibida.

#5.10 – Verificando nomes de usuários: Faça o seguinte para criar um programa que simule o modo como os sites garantem que todos tenham um nome de usuário único.
#• Crie uma lista chamada current_users com cinco ou mais nomes de usuários.
#• Crie outra lista chamada new_users com cinco nomes de usuários. Garanta que um ou dois dos novos usuários também estejam na lista current_users.
#• Percorra a lista new_users com um laço para ver se cada novo nome de usuário já foi usado. 
#Em caso afirmativo, mostre uma mensagem informando que a pessoa deverá fornecer um novo nome. 
#Se um nome de usuário não foi usado, apresente uma mensagem dizendo que o nome do usuário está disponível.
#• Certifique-se de que sua comparação não levará em conta as diferenças entre letras maiúsculas e minúsculas. Se 'John' foi usado, 'JOHN' não deverá ser aceito.

#5.11 – Números ordinais: Números ordinais indicam sua posição em uma lista, por exemplo, 1st ou 2nd, em inglês.
#A maioria dos números ordinais nessa língua termina com th, exceto 1, 2 e 3.
#• Armazene os números de 1 a 9 em uma lista.
#• Percorra a lista com um laço.
#• Use uma cadeia if-elif-else no laço para exibir a terminação apropriada para cada número ordinal. 
#Sua saída deverá conter "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", e cada resultado deve estar em uma linha separada.


#RESPOSTAS DOS EXERCICIOS

#5.8

users = ['admin', 'luthier', 'millerm',
         'lostedz', 'lost'] #Aqui criamos uma lista de usuarios.

for user in users:                                         #para cada usuario em usuarios
    if user == 'admin':                                    #Se o usuario for igual a admin, faça o que esta abaixo.
        print("Olá admin, gostaria de ver o relatorio?")
    else:                                                   #se não for igual a admin, faça o que esta abaixo.
        print("Olá"+" "+user+" "+"obrigado por fazer login")

#5.9

users = []      #Aqui temos uma lista vazia

if users:       #verificamos se a lista esta vazia quando uma instrução if utiliza uma lista. (se "lista" vazia = false, se com algum item = true)
    if user == 'admin':
        print("Olá admin, gostaria de ver o relatorio?")
    else:
        print("Olá"+" "+user+" "+"obrigado por fazer login")

else:           #este comando será executado após a verificação da lista, no caso pela lista estar vazia.
    print("\nA lista esta vazia, precisamos de usuarios!")
    
#5.10

current_users = ["joao", 'maria', 'jose',
                 'GUTEBA', 'lostedz']

new_users = ['guteba', 'lostedz', 'kaik',
             'tobias', 'zangão']  

for user in new_users:
    
    if user in current_users or user.lower() in current_users or user.upper() in current_users:
        print(user+" "+"usuario existente por favor forneça um novo nome")
    else:
        print("olá"+" "+user+" "+"o seu nome esta disponivel para utilização!")
        
#5.11

numeros_ordinais = [1, 2, 3,
                    4, 5, 6,
                    7, 8, 9]                            
for numero in numeros_ordinais:
    
    if numero == 1:
        print(str(numero)+"st")
    elif numero == 2:
        print(str(numero)+"nd")
    elif numero == 3:
        print(str(numero)+"rd")
    else:
        print(str(numero)+"th")


    
   
 