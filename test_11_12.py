from unittest import TestCase

# class Testy(TestCase):
#     def test_always_pass(self):
#         assert 'ala'.upper()=='ALA'

# class Test:
#     def test_sortuj_alph(self):
#         name = ['ola','ania','kasia']
#         sort_name = name.sort()
#         return sort_name
#         # assert test_sortuj_alph(name) == ['ania','ola', 'kasia']
#         # assert sort_name == ['ania','ola', 'kasia']
#         assert sort_name == ['ola','ania','kasia']

# class Testy(TestCase):
#     def test_always_pass(self):
#         assert 'ala'.upper()=='ALa', 'blad blad blad'

import pytest

def suma(a,b):
    return a+b

@pytest.mark.parametrize("a,b,expected",[(1,2,3),(5,6,11)])
def test (a,b,expected):
    assert suma(a,b)==expected