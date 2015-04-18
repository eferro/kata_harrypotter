# -*- coding: utf-8 -*-

from expects import *
from hamcrest import *
from doublex import *

def precioLibros(libros):
    return 8


with context('Harry Potter Kata'):
    with describe('comprando de uno en uno'):
        with it('el primero cuesta 8'):
            expect(precioLibros([1])).to(equal(8))
