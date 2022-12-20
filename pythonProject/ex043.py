peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2) #calcular altura quadrado
print('O IMC dessa pessoa é de {:.1f}'. format(imc))
if imc < 18.50:
    print('\033[31mVoce esta abaixo do peso\033[0m')
elif imc <= 25:
    print('\033[36mVoce esta no peso ideal\033[0m')
elif imc <= 30:
    print('\033[31mVoce esta com sobrepeso\033[0m')
elif imc <= 40:
    print('\033[31mVoce esta com obesidade\033[0m')
else:
    print('\033[31mVoce esta com obesidade mórbida\033[0m')
