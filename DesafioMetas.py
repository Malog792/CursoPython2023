#Se a meta não for atingida, o programa deverá informar que a meta não foi atingida e ninguém recebe bonus.
#Se a meta for atingida com menos de 500 unidades de diferença, o programa informa que a meta foi atingida e que os vendedores ganharão 5% de bonus.
#Se a meta for ultrapassada em mais de 500 unidades, os vendedores receberão bonus de 15%.

print("Desafio de Metas:\n Informe o número de vendas realizadas pelos vendedores e será calculada se a meta foi atingida e o bônus que os funcionários recebem\n")
meta1 = 50_000
meta2 = 50_500
vendas = float(input("Número de Vendas: "))
if vendas < meta1:
    resto = meta - vendas
    print("Infelizmente faltou {} para atingir a meta de vendas. O bônus não será repassado. ".format(resto))
elif vendas >= meta1 and <meta2:
   
  
  