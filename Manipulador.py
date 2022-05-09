from os import system

class manipulador():
    file = ''
    dictionary = {}

    def __init__(self):
        self.file = ''
        self.dictionary = {}

    def set_file(self, directory):
        self.file = directory

    def set_reference(self, referencias=None):
        c = 1

        if referencias != None:
            self.dictionary = referencias
        else:
            while (True):
                system('cls')
                digito = input("Informe a {}a referência:".format(c))

                if digito == None or digito == '':
                    break

                self.dictionary.update({digito: None})
                c += 1

    def set_dados(self):
        c = 0

        for i in self.dictionary:
            system('cls')

            dados = input("REFERENCIA {}\nInforme os dados:".format(i))

            self.dictionary.update({i: dados})