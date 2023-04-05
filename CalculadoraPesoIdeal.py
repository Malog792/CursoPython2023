print("Olá, essa é a calculadora de Peso Ideal.")

print("Siga as instruções para definirmos seu peso ideal:\n")
while 0 == 0:
  input("Pressione Enter para continuar")
  print("1. Primeiro passo:")

  altura = float(input("Digite a sua altura em metros\n"))

  print(altura)

  print("2. Segundo passo:")
  
  peso = float(input("Digite o seu Peso em Kilogramas\n"))

  print(peso)

  print("3. Terceiro passo:")

  sexo = input("Digite o seu Sexo Biológico\n'M' para masculino e 'F' para feminino\n").upper()

  if sexo == 'M':
    PesoMasculinoIdeal = ((72.7 * altura) - 50)
    print("Seu peso ideal é: {}".format(PesoMasculinoIdeal))
  elif sexo == 'F':
    PesoFemininoIdeal = ((62.1 * altura) - 44.7)
    print("Seu peso ideal é: {}".format(PesoFemininoIdeal))