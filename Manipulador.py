from os import system
import docx
import os

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
                digito = input("Informe a {}a referĂȘncia:".format(c))

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

    def save_dados(self, referencias: dict):
        if '.txt' in self.file:
            arq = open(self.file, 'r')
            txt = arq.read()

            for i in referencias:
                txt = txt.replace(i, referencias[i])

            arq.close()

            arq_write = open(self.file, 'w')
            arq_write.write(txt)
            arq_write.close()
        else:
            pass

