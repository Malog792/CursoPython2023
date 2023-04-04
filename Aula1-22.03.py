print('bom dia')
#Aula sobre Print
print("Minha idade é: ", 20)
# Texto com booleano
print("cerveja: ", True)
# comentarios com varias linhas 
'''ola meano'''
# Textos Longos com mais de uma linha
print('''Cardápio:
1 - Hamburger
2 - Pizza''')
#Repetição de mensagem 25 vezes
print("Prof, eu sou",25*"muito ","Mais legal que tu")
#declarar a variavel inteira
print("")
a=2
print(a)
a= 3.14
print(a)
#tomar cuidado pois podemos perder informações com o uso das variaveis
# como rodar numeros grandes sem se perder
numero = 1_000_000_000
print("O numero digitado é: ", numero)
# Perceba que após executar não tem o under line
# Print usando format
numero2 = 3
numero1 = 1
print("O numero {} é menor que o numero {}".format(numero1, numero2))
#Mais exemplos
ham = 25
pizza = 50
dogao = 39
refri = 20
print("""Cardápio:
1 - Hamburger {}
2 - Pizza {}
3 - dogao {}
4 - refri {} """.format(ham,pizza,dogao,refri))
# concatenar texto
texto1 = "O mauricio é top."
texto2 = "Top demais"
print(texto1+texto2)
print("")
#Declarar lista
lista = ["Batatinha",'Frita',1,2,3]
# Imprimir as variaveis na tela
print(lista)
#