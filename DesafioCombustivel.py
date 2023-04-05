#Até 20 litros 4% de desconto por litro, acima de 20 litros 6% de desconto para gasolina
#Até 20 litros 3% de desconto por litro, acima de 20 litros 5% de desconto para alcool

combustivel = input("Qual combustível será abastecido? 'G' para Gasolina e 'A' para Àlcool").upper()

litros = float(input("Qauntos litros de Combustivel serão abastecidos?"))

gasolina = 5
alcool = 3

if combustivel == "G" and litros < 20:
  gasolina = gasolina-(gasolina*0.04)
  valor = gasolina * litros
  print("O valor do seu abastecimento é: ",valor)
elif combustivel == "G" and litros > 20:
  gasolina = gasolina-(gasolina*0.06)
  valor = gasolina * litros
  print("O valor do seu abastecimento é: ",valor)
elif combustivel == "A" and litros > 20:
  alcool = alcool-(alcool*0.05)
  valor = alcool * litros
  print("O valor do seu abastecimento é: ",valor)
elif combustivel == "A" and litros < 20:
  alcool = alcool-(alcool*0.03)
  valor = alcool * litros
  print("O valor do seu abastecimento é: ",valor)