velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('\033[31mMULTADO!, você excedeu o limita permidito que é de 80Km/h')
    print('\033[31mVocê deve pagar uma multa de R${:.2f}!'.format((velocidade-80) * 7))
print('\033[36mTenha um bom dia! Dirija com segurança!')
