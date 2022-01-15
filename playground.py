"""Con esto se ejemplifica la utulización de *args, lo que hace
que la función acepte un numero ilimitado de entradas que
en este caso solo van a sumarse para dar un total"""

def add(*args):
    total = 0
    for n in args:
        total += n
    return total

print(add(1, 5, 6, 8, 9, 10))
"""**kwargs arguments:
esta sintaxis me permite usar las entradas como un diccionario"""

def calculate(**kwargs):
    print(kwargs)

calculate(add=3, multiply = 5)

"""También es útil para crear clases con propiedades opcionales"""
class Car:


    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')
        self.colour = kw.get('colour')
        self.seats = kw.get('seats')


my_car = Car(make= 'Nissan', seats= 4)

"""Esto normalmente ocurre cuando los programas son pasados de otro lenguaje 
a Python"""
