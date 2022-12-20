frase = 'Curso em video python'
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])
print(len(frase))
print(frase.count('o', 0, 13))
print(frase.find('deo'))
print(frase.find('android'))
print('Curso' in frase)
frase = frase.replace('python', 'android')
print(frase.replace('python', 'android'))
print(frase)
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.split())
dividido = frase.split()
print(dividido[2][3])
frase2 = '   Aprenda Python  '
print(frase2.strip())
print(frase2.rstrip())
print(frase2.lstrip())
print(len(frase.strip()))

print("""asdasdasdas
asdasdasdasdasdasd
asdasdasdasdasd
asdasdasdasdasd
asdasdasdasdasda""")