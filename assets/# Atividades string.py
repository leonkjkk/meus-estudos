# Atividades
# Exercicio 22
nome1 = str(input('Nome Completo: ')).strip()
print('Seu nome maiúsculo:', nome1.upper())
print('Seu nome minúsculo:', nome1.lower())
print('Seu nome tem', len(nome1) - nome1.count(' '), 'letras.')
separado = nome1.split()
print('Seu primeiro nome tem', len(separado[0]))
#print('Seu primeiro nome tem', nome1.find(' '), 'letras.') // Também funciona

# Exercicio 23
num = int(input('Digite um número: '))
U = num // 1 % 10
D = num // 10 % 10
C = num // 100 % 10
M = num // 1000 % 10
print('A Unidade é: ', U)
print('A Dezena é: ', D)
print('A Centena é: ', C)
print('O Milhar é: ', M)

# Exercicio 24
nom = str(input('Digite o nome da sua cidade: ')).strip()
nom = nom.title()
print('Santo' in nom)

# Exercicio 25
nome2 = str(input('Digite seu nome: ')).strip()
nome2 = nome2.title()
print('Silva' in nome2)

# Exercicio 26
nome = str(input('Digite uma frase:')).lower().strip()
print('A letra >a< aparece: ', nome.count('a'), 'vezes.')
print('A letra A aparece primeiro na posição: ', nome.find('a')+1)
print('A letra A aparece por último na posição: ', nome.rfind('a')+1)

# Exercicio 27
nome3 = str(input('Digite seu nome: ')).strip()
n = nome3.split()
print('Seu primeiro nome é:', n[0])
print('Seu último nome é:', n[len(n)-1])

