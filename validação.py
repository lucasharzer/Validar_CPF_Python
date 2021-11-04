from time import sleep
import funções as f


f.Linha()
f.Titulo('Validação de CPF')
f.Linha()
sleep(1)
print('\nAguarde ...')
sleep(2)


# Inicio do programa

while True:

    # Inserir o CPF:

    try:

        cpf_numerado = []
        cpf = str(input("\nInsira o CPF corretamente (com ou sem pontuação): ")).replace('.', '').replace('-', '')

    except (KeyboardInterrupt):
        print("\nO programa foi interrompido pelo usuário.")
        break

    # Passar pelas Regras:

    f.NumerarCaracteres(cpf, cpf_numerado)

    f.ChecarQuantidade(cpf)

    f.PrimeiroVerificador(cpf, cpf_numerado)

    f.SegundoVerificador(cpf, cpf_numerado)

    # Validação:

    print("\nAnalisando ...\n")
    sleep(2)

    if f.ChecarQuantidade(cpf) == True and f.PrimeiroVerificador(cpf, cpf_numerado) == True and f.SegundoVerificador(cpf, cpf_numerado) == True:
        print("O CPF é válido!")
    else:
        print("O CPF é inválido!")

    # Perguntar se quer continuar:

    while True:

        try:

            f.Linha()
            escolha = str(input("\nDeseja validar outro CPF ? [S/N] ")).strip().upper()

            if escolha == 'N' or escolha == "S":
                break
            else:
                print("Opção Inválida! Tente novamente.")

        except(KeyboardInterrupt):
            print("\nO programa não pode ser interrompido, até responder a pergunta.")
        
    f.Linha()

    if escolha[0] == 'N':
        break
    

sleep(1)
print("\nFinalizando ...\n")
sleep(2)
print("Finalizado\nObrigado por participar!")