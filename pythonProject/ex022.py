nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em letras maiusculas é {}'.format(nome.upper()))
print('Seu nome em letra minusculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letra'.format(len(nome)-nome.count(' ')))
print('Seu prmeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print(separa)
print('Seu primeiro nome é {} e ele tem {} letra'.format(separa[0], len(separa[0])))