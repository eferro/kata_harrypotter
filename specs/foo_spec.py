# -*- coding: utf-8 -*-

from expects import *
from hamcrest import *
from doublex import *

def precioLibros(libros):
    if len(libros) == 2:
        if libros[0] != libros[1]:
            return 8*2*0.95
    return 8 * len(libros)


with context('Harry Potter Kata'):
    
    with describe('comprando de uno en uno'):
        with it('el primero cuesta 8'):
            expect(precioLibros([1])).to(equal(8))
        with it('el segundo cuesta 8'):
            expect(precioLibros([2])).to(equal(8))

    with describe('comprando dos'):
        with it('dos copias del mismo cuestan 16'):
            expect(precioLibros([1, 1])).to(equal(16))
            expect(precioLibros([2, 2])).to(equal(16))

        with it('dos copias distintas tienen un descuento de 5'):
            expect(precioLibros([1, 2])).to(equal(16*0.95))