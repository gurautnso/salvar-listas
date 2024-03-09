def leiaint(prompt='', validnumbers=[-1], style='0', color='31', back='40'):
    """
    -> função para analisar uma variavel é numerica de forma que não de syntaxerror
    :param prompt: pede um numero
    :param validnumbers: se diferente de '-1' apenas os valores dentro deste parametro seram aceitos
    :param style: define o estilo da mensagem de erro no padrão ANSI
    :param color: define a cor da mensagem de erro no padrão ANSI
    :param back: define a cor da mensagem de erro no padrão ANSI
    :return: se for o prompt for numerico vai retormar o prompt em int senão vai ficar perguntando até ser um numero
    """
    while True:
        try:
            num = int(input(prompt).strip())
            if validnumbers[0] != -1:
                for i in validnumbers:
                    if num == i:
                        return num
            else:
                return num
        except (TypeError, ValueError):
            print(f'\033[{style};{color};{back}mERRO! Digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print(f'\n\033[{style};{color};{back}mUsuario preferiu não digitar esse número.\033[m')
            return 0
