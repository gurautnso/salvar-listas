from functions.text import *
from functions.number import *
from time import sleep

while True:
    arquivo = str(input('Digite o nome do arquivo a ser utilizado: '))
    if not arqexists(arquivo):
        print(f'\033[1:31:40mOuve um erro\033[m')
        sleep(3)
        print(f'Verifique se escreveu o nome do arquivo corretamente,\n'
              f'ou de criar um arquivo com este nome?\n'
              f'[1] escrever o nome do arquivo novamente\n'
              f'[2] criar novo arquivo')
        sleep(.75)
        resp = leiaint('Digite um dos números acima: ', [1, 2])
        if resp == 2:
            arqcreate(arquivo)
        elif resp == 1:
            continue
