from functions import *

arquivo = str(input('Digite o nome do arquivo a ser utilizado: '))
if not arqexists(arquivo):
    print(f'Ouve um erro, verifique se escreveu o nome do arquivo corretamente,\n ou de criar um arquivo com este nome?\n')