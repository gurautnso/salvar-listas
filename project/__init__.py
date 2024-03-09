from functions.text import *
from functions.number import *
from time import sleep

arquivo = resp = resp2 = 0
while True:
    if arquivo == 0 or resp == 0:
        arquivo = str(input('Digite o nome do arquivo a ser utilizado: '))
    if not arqexists(arquivo):
        print(f'\033[1:31:40mOuve um erro\033[m')
        sleep(3)
        print(f'Verifique se escreveu o nome do arquivo corretamente,\n'
              f'ou de criar um arquivo com este nome?\n'
              f'[0] escrever o nome do arquivo novamente\n'
              f'[1] criar novo arquivo')
        sleep(.75)
        resp = leiaint('Digite um dos números acima: ', [0, 1])
        if resp == 1:
            arqcreate(arquivo)
            continue
        elif resp == 0:
            continue
    else:
        print(f'\033[1:34mArquivo encontrado com sucesso!\033[m')
        sleep(.7)
        print(f'O\'que deseja fazer agora?\n'
              f'[0] adicionar novo valor ao arquivo escolhido;\n'
              f'[1] modificar valor já existente no arquivo escolhido;\n'
              f'[2] escolher outro arquivo;')
        resp2 = leiaint('Digite um dos números acima: ', [0, 1, 2])
