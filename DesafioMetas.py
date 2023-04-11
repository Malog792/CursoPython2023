#Se a meta não for atingida, o programa deverá informar que a meta não foi atingida e ninguém recebe bonus.
#Se a meta for atingida com menos de 500 unidades de diferença, o programa informa que a meta foi atingida e que os vendedores ganharão 5% de bonus.
#Se a meta for ultrapassada em mais de 500 unidades, os vendedores receberão bonus de 15%.

print("Desafio de Metas:\n Informe o número de vendas realizadas pelos vendedores e será calculada se a meta foi atingida e o bônus que os funcionários recebem\n")

meta1 = 50_000
meta2 = 50_500
print("Meta de Vendas: ",meta1)
vendas = float(input("Número de Vendas: "))
if vendas < meta1:
    resto = meta1 - vendas
    print("Infelizmente faltou {:.0f} para atingir a meta de vendas. O bônus não será repassado. ".format(resto))
elif vendas <= meta2:
  resto = meta2 - vendas
  print("Muito bom, meta atingida, bônus de 5 %, faça mais {:.0f} venda(s) na próxima para conseguir mais bônus".format(resto))
elif vendas > meta2:
  resto = vendas - meta2
  print("Meus parabéns, vocês superaram em {:.0f} venda(s) a meta de vendas, bônus de 15% para os ótimos funcionários ".format(resto))

   
  
  