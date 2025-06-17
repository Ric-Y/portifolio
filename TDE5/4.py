N = input('digite 2 numeros')
Lista = list(map(int, N.split()))
print(f'A soma dos seus numeros é: {Lista[0]+Lista[1]}, a Multiplicação deles é {Lista[0]*Lista[1]}, e a divisão de {Lista[0]} por {Lista[1]} é {Lista[0]/Lista[1]}')