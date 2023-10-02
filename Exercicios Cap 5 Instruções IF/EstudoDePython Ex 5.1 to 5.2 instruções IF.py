#FAÇA VOCÊ MESMO
#5.1 – Testes condicionais: Escreva uma série de testes condicionais. Exiba uma frase que descreva o teste e o resultado previsto para cada um. Seu código deverá ser semelhante a: car = 'subaru'
#print("Is car == 'subaru'? I predict True.") print(car == 'subaru') print("\nIs car == 'audi'? I predict False.") print(car == 'audi') 
#•Observe atentamente seus resultados e certifique-se de que compreende por que cada linha é avaliada como True ou False.
#• Crie pelo menos dez testes. Tenha no mínimo cinco testes avaliados como True e outros cinco avaliados como False.

#5.2 – Mais testes condicionais: Você não precisa limitar o número de testes que criar em dez. Se quiser testar mais comparações, escreva outros testes e acrescente-os em conditional_tests.py. 
#Tenha pelo menos um resultado True e um False para cada um dos casos a seguir: • testes de igualdade e de não igualdade com strings; • testes usando a função lower(); 
# • testes numéricos que envolvam igualdade e não igualdade, maior e menor que, maior ou igual a e menor ou igual a; • testes usando as palavras reservadas and e or; 
# • testes para verificar se um item está em uma lista; • testes para verificar se um item não está em uma lista.

#RESPOSTAS DOS EXERCICIOS
#5.1
#• Crie pelo menos dez testes. Tenha no mínimo cinco testes avaliados como True e outros cinco avaliados como False.

car = 'ferrari 250 gto'
print('is car == ferrari italia?')
print(car == 'ferrari italia')

print('\nis car == ferrari 250 gtO?')
print(car == 'ferrari 250 gtO')

print('\nis car != ferrari 250 gto?')
print(car != 'ferrari 250 gto')

print('\nis car == audi')
print(car == 'audi')

print('\nis car == porsche?')
print(car == 'porsche')                       #até aqui da tudo False.

print('\nis car =! ferrari gto 250')
print(car != 'ferrari gto 250')

print('\nis car == ferrari 250 gto?')
print(car == 'ferrari 250 gto')

print('\nis car != audi?')
print(car != 'audi')

print('\nis car == ferrari 250 gto.upper()?')
print(car == "ferrari 250 gto".upper())

print('\nis car != porsche?')
print(car != 'porsche')                       #até aqui da tudo True


#5.2

#• testes de igualdade e de não igualdade com strings (==, !=)

gun = "Ak47"

print('\nis gun == ak45?')
print(gun =='ak45')

print('\nis gun != Ak45?')
print(gun !='Ak45')

#• testes usando a função lower()

print('\nis gun == ak45?')
print(gun =='ak45'.upper)

print('\nis gun != Ak45?')
print(gun !='Ak45'.title())

#• testes numéricos que envolvam igualdade (==) e não igualdade(!=), maior e menor que(>, <), maior ou igual a e menor ou igual a (>=, <=);

dinheiro = 100

print("\nMeu dinheiro é igual a 150?")
print(dinheiro == 150)

print("\nMeu dinheiro é diferente de 50?")
print(dinheiro != 50)

print("\nMeu dinheiro é maior que 250??")
print(dinheiro > 250)

print("\nMeu dinheiro é menor que 110")
print(dinheiro < 110)

print("\nMeu dinheiro é maior ou igual a 100?")
print(dinheiro >= 100)

print("\nMeu dinheiro é menor ou igual a 90?")
print(dinheiro <= 90)

#• testes usando as palavras reservadas and e or;

number = 126

print("\nMeu número é maior que 125 e igual a 126?")
print(number > 125 and number == 126)

print("\nMeu número é menor que 130 e igual a 90?")
print(number < 130 and number == 90 )

print("\nMeu número é maior que 100 ou menor que 90?")
print(number > 100 or number < 90)

print("\nMeu número é menor que 50 ou maior que 300?")
print(number < 50 or number > 300)

#• testes para verificar se um item está em uma lista

print('\n')
requested_guns = ["Ak47", "Aug", "Famas", "M41A1", "M416 SOP MOD"]
print("Se a arma famas estiver no requested_guns print verdadeiro, se não estiver print falso.")
if 'famas' in requested_guns:
    print("Verdadeiro.")
else:
    print("Falso")
    
#• testes para verificar se um item não está em uma lista.

banned_guns = ['Minigun', 'RPG', 'SAW']
guns = 'Ak47'

if guns not in banned_guns:
    print("\n"+guns.title()+" "+"its allowed.")
    
