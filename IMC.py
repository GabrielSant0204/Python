print('================================')
print('         CALCULE SEU IMC   ')
print('================================')

nome = input('Qual é seu nome?').capitalize()
altura = float(input('qual é sua altura?'))
peso = int(input('qual é seu peso?'))

imc = peso / (altura * altura)

print('o IMC de {} é {}'.format(nome, imc))


if imc <= 18.5:
    print('você está abaixo do peso. Alimente-se melhor!')

elif imc >= 18.6 and  imc <= 24.9:
    print('Peso Ideal, PARABÉNS!!!')

elif imc >= 25.0 and imc <=29.9:
    print('levemente acima do peso')

elif imc >= 30.0 and imc <=34.9:
    print('obesidade grau I, CUIDADO!!!')

elif imc >= 35.0 and imc <=39.9:
    print('obesidade grau II,ISSO É SEVERO!!!')

elif imc >= 40:
    print('obesidade grau III, ISSO JÁ É MÓRBIDO!!!')

