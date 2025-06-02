# -*- coding: utf-8 -*-

def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print('hola')
        funcion(palabra)
        print('adios')
    return otra_funcion


def mayusculas(texto):
    print(texto.upper())

def minusculas(texto):
    print(texto.lower())

#Lo que hago aca abajo es asiganr un contenido a mayuscula_decorada que sea el decorador y como parametro la función mayusulas
#es decir, pase como parametro una funcion
mayuscula_decorada = decorar_saludo(mayusculas)
mayuscula_decorada('python')