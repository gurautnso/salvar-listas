from functions.text import *
from functions.number import *
from time import sleep

arquivo = resp = resp2 = tam = 0
while True:
    if arquivo == 0 or resp == 0:
        arquivo = str(input('Digite o nome do arquivo a ser utilizado: '))
    if not arqexists(arquivo):
        print(f'\033[1:31:40mOuve um erro\033[m')
        sleep(3)
        print(f'Verifique se escreveu o nome do arquivo corretamente,\n'
              f'ou gostaria de criar um arquivo com este nome?\n'
              f'[0] Escrever o nome do arquivo novamente\n'
              f'[1] Criar novo arquivo\n')
        sleep(.75)
        resp = leiaint('Digite um dos números acima: ', [0, 1])
        if resp == 1:
            print(f'\033[1:33mCriando arquivo...\033[m')           # esta parte é puramente estetica
            sleep(.5)                                              # esta parte é puramente estetica
            arqcreate(arquivo)
            print(f'\033[1:32mArquivo criado com sucesso!\033[m')  # esta parte é puramente estetica
            sleep(.5)                                              # esta parte é puramente estetica
            continue
        elif resp == 0:
            continue
    else:
        print(f'\033[1:34mArquivo encontrado com sucesso!\033[m')
        sleep(.7)
        print(f'O\'que deseja fazer agora?\n'
              f'[0] Adicionar novo valor ao arquivo escolhido;\n'
              f'[1] Escolher outro arquivo;\n')
        resp2 = leiaint('Digite um dos números acima: ', [0, 1])
        if resp2 == 1:
            arquivo = resp = resp2 = tam = 0
            continue
        elif resp2 == 0:
            while True:
                final = str(input(f'Escreva o valor desejado[-1 para parar]: '))
                if final == '-1':
                    break
                tam = arqread(arquivo)+1
                arqwrite(arquivo, f'{tam};{final};\n')
