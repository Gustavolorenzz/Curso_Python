#Aprenderemos: 
#1-operacoes basicas
#2-ordem de operação
#3-variaveis
#4-comparação
#5-string
#6-input e output

#1-----------------------------------
#soma e subtração
10-4
#Multiplicaçao e divisao
8/2
#Exponencial
4**(1/2)
#Divisao inteira(no C é o %)
20//6
#Resto
20%6
#2-----------------------------------
#ordem: (), **, *, /, +, -.
#parenteses tem e a mais prioritaria e a subtração a menos
#3-----------------------------------
#maior: >  >=
#menor: <  <=
#igual: ==
#diferente: !=
#4-----------------------------------
#Nao e necessario indicar o tipo da variavel -> tipagem forte e dinâmica
num=2
texto="Olá"
#5-----------------------------------
string = "blablabla blabla bla"
string2 = """oioioioi
oioioioi
super oi
oioioioi
"""
#concatenar "+" : juntar duas strings
string+string2
#indexacao: string[n] para n sendo um numero maior ou igual a 0 caso seja sequencial
#           ou um numero menor que 0, caso caminhe de tras para frente
string[0]#b
#bloco de caracteres: "n:m"
string[0:-1]
string[0:]
#Metodos:
#.upper() toda string com letras maiusculas
#.lower() minuscula
#.strip() tira espaços no início e final
#.startswith('xyz') teste se começa
#.endswith('xyz') testa se termina
#.find('xyz') encontra
#.replace('old','new') mudar
string.upper()
string.replace('bla','oie')
#6-----------------------------------
#input
string = input('bla?')
#output
print('bla eh', string,', um super bla')
print(f'mas {2*8} sera bla?{string.upper() + num*"bla"}')
