# Projeto par ou impar
while True:
    try:    
        valor = int(input('Digite o valor:'))
        if valor % 2 == 0:
            print('Numero par')
        else:
            print('Numero impar')
    except:
        print('Digite apenas numeros')