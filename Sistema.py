from os import system
import Manipulador

novo_documento = True
option = None
documento = Manipulador.manipulador()

def open_file(directory):
    system('start {}'.format(directory))

def get_list(directory):
    try:
        arq = open(directory, 'r')

        lista = []
        arq.seek(0)

        while True:
            linha = arq.readline()

            if linha == '' or linha == None:
                break

            lista.append(linha[0:linha.index('[')])

        arq.close()

        return lista

    except Exception:
        pass

def verify(directory):
    try:
        arq = open(directory, 'r')
        arq.close()

        return True
    except Exception:
        print('Arquivo não encontrado !')

        return False

while True:
    system('cls')

    print('Bem vindo ao sistema de automação de documentos !\n')

    if novo_documento:
        diretorio = input('Informe o local do arquivo:')

        if verify(diretorio):
            documento = Manipulador.manipulador()
            documento.set_file(diretorio)
            novo_documento = False
    else:
        print('MENU\n\n(1) - NOVO DOCUMENTO\n(2) - ABRIR O DOCUMENTO\n(3) - ADICIONAR REFERÊNCIAS')
        print('(4) - ADICIONAR DADOS\n(5) - CONFERIR DADOS\n(6) - SELECIONAR PREDEFINIÇÃO')
        print('(7) - ADICIONAR PREDEFINIÇÃO\n(8) - EXCLUIR PREDEFINIÇÃO\n(9) - LISTA DE PREDEFINIÇÕES')
        print('(10) - GRAVAR NO DOCUMENTO\n')

        option = input('OPÇÃO:')

    try:
        if option == '1': #FUNCIONANDO
            novo_documento = True
        elif option == '2': #FUNCIONANDO
            if documento.file != '':
                open_file(documento.file)
            else:
                while True:
                    try:
                        system('cls')
                        documento.set_file(input('INFORME O DIRETORIO: '))

                        arq = open(documento.file, 'r')
                        arq.close()

                        open_file(documento.file)
                    except Exception:
                        if documento.file != '':
                            print("\nARQUIVO NÃO ENCONTRADO !")
                            system('pause')
                            break

        elif option == '3': #FUNCIONANDO
            documento.set_reference()

        elif option == '4': #FUNCIONANDO
            documento.set_dados()

        elif option == '5': #FUNCIONANDO
            system('cls')

            for i in documento.dictionary.items():
                print('---\nREFERÊNCIA -> {}\nDADO -> {}\n---'.format(i[0], i[1]))

            system('pause')

        elif option == '6': #FUNCIONANDO
            system('cls')
            predefinicao = {}

            lista = get_list('predefinicoes.txt')

            for i in range(0, len(lista)):
                print(i+1, '- ', lista[i], '\n')

            opcao = int(input('PREDEFINIÇÃO: '))
            selecao = lista[opcao-1]

            arq = open('predefinicoes.txt', 'r')

            for i in arq:
                valores = str(i).split('\'')
                c = 1
                for j in valores:
                    if c%2 == 0:
                        predefinicao.update({valores[c-1]:None})
                    c += 1

            arq.close()

            documento.set_reference(predefinicao)

            system('pause')

        elif option == '7': #FUNCIONANDO
            system('cls')

            nome = input('Informe o nome da predefinição:')
            arq = open('predefinicoes.txt', 'a')

            predefinicao = str(documento.dictionary.keys())
            predefinicao = predefinicao.replace('dict_keys(', '')
            predefinicao = predefinicao.replace(')', '')
            arq.write(nome + predefinicao + '\n')
            print(str(documento.dictionary.keys()))
            arq.close()

        elif option == '8': #FUNCIONANDO
            system('cls')

            lista = get_list('predefinicoes.txt')

            for i in lista:
                print(i)

            escolha = input('INFORME A PREDEFINIÇÃO A SER ESCOLHIDA: ')

            for ii in lista:
                if escolha in ii:
                    arq_read = open('predefinicoes.txt', 'r')

                    txt = arq_read.read()
                    prox_index = lista.index(ii)+1
                    prox_predefinicao = lista[prox_index]
                    predefinicao_escolhida = txt[txt.index(ii):txt.index(prox_predefinicao)]

                    txt = txt.replace(predefinicao_escolhida, '')

                    arq = open('predefinicoes.txt', 'w')
                    arq.write(txt)

                    arq.close()
                    arq_read.close()

        elif option == '9': #FUNCIONANDO
            system('cls')

            lista = get_list('predefinicoes.txt')

            for i in lista:
                print(i)
                pass

            system('pause')

        elif option == '10':
            documento.save_dados(documento.dictionary)

    except Exception:
        print('\nAlgo deu errado !')
        system('pause')