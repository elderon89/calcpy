def calculate():
    operation = input('''
Favor inserir qual operação deseja realizar:
+ para soma
- para subtração
* para multiplicação
/ para divisão
** para potência
''')

    n1 = int(input('Escolha o primeiro número: '))
    n2 = int(input('Escolha o segundo número: '))

    # Addition
    if operation == '+':
        print('{} + {} = '.format(n1, n2))
        print(n1 + n2)

    # Subtraction
    elif operation == '-':
        print('{} - {} = '.format(n1, n2))
        print(n1 - n2)

    # Multiplication
    elif operation == '*':
        print('{} * {} = '.format(n1, n2))
        print(n1 * n2)

    # Division
    elif operation == '/':
        print('{} / {} = '.format(n1, n2))
        print(n1 / n2)


    elif operation == '**':
        print('{} ** {} = '.format(n1, n2))
        print(n1 ** n2)

    else:
        print('Você não escolheu com um operador válido, por favor rode o programa novamente.')

    # Add again() function to calculate() function
    again()

# Define again() function to ask user if they want to use the calculator again
def again():

    # Take input from user
    calc_dnv = input('''
Você deseja calcular novamente?
Favor digitar S para SIM ou N para NÃO.
''')

    # If user types Y, run the calculate() function
    if calc_dnv == 'S':
        calculate()

    # If user types N, say good-bye to the user and end the program
    elif calc_dnv == 'N':
        print('Até mais!')

    # If user types another key, run the function again
    else:
        again()

# Call calculate() outside of the function
calculate()
