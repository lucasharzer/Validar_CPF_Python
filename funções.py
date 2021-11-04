def Linha():
    '''
    -> Linha para separação visando a organização.
    '''

    print("~---------------------------------~")

def Titulo(msg):
    '''
    -> Centralizar o título.
    '''

    print(msg.center(35))

# Checar a quantidade de valores do CPF

def ChecarQuantidade(c):
    '''
    -> Checar se o CPF tem, obrigatoriamente, 11 números e
    caso tiver retorna verdadeira senão retorna falso;
    -> c é o CPF.
    '''

    if len(c) < 11 or len(c) > 11:
        return False
    else:
        return True

# Separar os números para o cálculo

def NumerarCaracteres(c, cn):
    '''
    -> Transformar o CPF que foi recebido como caractere em um 
    número para poder realizar os cálculos para validação e 
    adicionar os números separadamente em uma lista.
    -> c é o CPF
    -> cn é uma lista
    '''

    for n in c:
        n = int(n)
        cn.append(n)

# Analisar o primeiro verificador

def PrimeiroVerificador(c, cn):
    '''
    -> Verificar se o resultado do primeiro cálculo é igual ao
    primeiro verificador.
    -> c é o CPF
    -> cn é uma lista
    '''

    if len(c) < 11 or len(c) > 11:
        return False
    else:
        acumulador1 = 0
        resultado1 = 0
        controlador1 = 10

        for numeros1 in cn[0:9]:
            resultado1 = numeros1 * controlador1
            acumulador1 += resultado1
            controlador1 -= 1

        acumulador1 = acumulador1 * 10 % 11

        if acumulador1 == 10:
            acumulador1 = 0

        if acumulador1 == cn[9]:
            return True
        else:
            return False

# Analisar o segundo verificador

def SegundoVerificador(c, cn):
    '''
    -> Verificar se o resultado do segundo cálculo é igual ao
    segundo verificador.
    -> c é o CPF
    -> cn é uma lista
    '''

    if len(c) < 11 or len(c) > 11:
        return False
    else:
        acumulador2 = 0
        resultado2 = 0
        controlador2 = 11

        for numeros2 in cn[0:10]:
            resultado2 = numeros2 * controlador2
            acumulador2 += resultado2
            controlador2 -= 1

        acumulador2 = acumulador2 * 10 % 11

        if acumulador2 == 10:
            acumulador2 = 0

        if acumulador2 == cn[10]:
            return True
        else:
            return False