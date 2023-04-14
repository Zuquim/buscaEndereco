from lista_menu import lista
from consulta import buscar_por_cep, buscar_por_end
import sys


def menu():
    # Formata o menu
    string = '#'
    barra = string * 42
    titulo = ' MENU PRINCIPAL '
    titulo_principal = titulo.center(42, '#')

    c = 1
    print(titulo_principal)
    for item in lista:
        print('\033[33m[{}]\033[m - \033[34m{}\033[m'.format(c, item))
        c += 1
    print(barra)


def apontar_funcoes(valor):
    if valor == '1':
        buscar_por_cep()
    elif valor == '2':
        buscar_por_end()
    elif valor == 4:
        sys.exit()


def escolher_opcao():
    valor = input('Escolha a sua opção: ')
    return valor
