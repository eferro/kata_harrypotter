# -*- coding: utf-8 -*-

from expects import *
from hamcrest import *
from doublex import *

PRECIO_UNITARIO = 8
LIBRO1 = 'libro1'
LIBRO2 = 'libro2'

def precioLibros(libros):
    if len(libros) == 2:
        if libros[0] != libros[1]:
            return PRECIO_UNITARIO*2*0.95
    return PRECIO_UNITARIO * len(libros)


with context('Harry Potter Kata'):
    
    with describe('comprando de uno en uno'):
        with it('el primero cuesta PRECIO_UNITARIO'):
            expect(precioLibros([LIBRO1])).to(equal(PRECIO_UNITARIO))
        with it('el segundo cuesta PRECIO_UNITARIO'):
            expect(precioLibros([LIBRO2])).to(equal(PRECIO_UNITARIO))

    with describe('comprando dos'):
        with it('dos copias del mismo cuestan 16'):
            expect(precioLibros([LIBRO1, LIBRO1])).to(equal(2 * PRECIO_UNITARIO))
            expect(precioLibros([LIBRO2, LIBRO2])).to(equal(2 * PRECIO_UNITARIO))

        with it('dos copias distintas tienen un descuento de 5'):
            expect(precioLibros([LIBRO1, LIBRO2])).to(equal(16*0.95))