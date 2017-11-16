# Test des axiomes
from Progressif.MultiSet2 import MultiSet


def test_add():
    m = MultiSet()
    # Signature
    for pas_un_nombre_valide in (-1, 0, 'a', [1, 2, 3]):
        m.add('cobaye', pas_un_nombre_valide)
        assert 'cobaye' not in m

    # Axiomes
    m.add(4)
    assert m.multiplicite(4) == 1
    m.add('un mot', 145)
    assert m.multiplicite('un mot') >= 145


def test_repr():
    a = MultiSet([(1, 2), (3, 4, 5, 6), 7])
    assert repr(a) == 'MultiSet({1: 2, 3: 4, 7: 1})'
    b = MultiSet({'une chaine': 12})
    assert repr(b) == "MultiSet({'une chaine': 12})"


def test_str():
    a = MultiSet([(3, 4, 5, 6)])
    assert str(a) == """{{\n  3: 4}}"""
    b = MultiSet({'a': 2})
    assert str(b) == """{{\n  'a': 2}}"""


def test_contains():
    m = MultiSet()
    assert 0 not in m
    m.add('dix-sept')
    assert 17 not in m
    assert 'dix-sept' in m


def test_multiplicite():
    m = MultiSet()
    for i, lettre in enumerate(('a', 'b', 'c', 'd')):
        m.add(lettre, i)
        assert m.multiplicite(lettre) == i

    m.add('o', 18)
    assert m.multiplicite('o') == 18
    m.add('o', 12)
    assert m.multiplicite('o') == 30

def test_len():
    liste = [1, 2, 2, 4, 3, 5, 5, 7, 7, 8, 1, 2, 4, 5, 6, 7, 9]
    m = MultiSet(liste)
    assert len(m) == len(liste)
    m.add(4, 2)
    m.add('brique', 3)
    assert len(m) == len(liste) + 5

def test_iter():
    liste = [1, 2, 2, 4, 3, 5, 5, 7, 7, 8, 1, 2, 4, 5, 6, 7, 9]
    elements = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    m = MultiSet(liste)
    for nombre in m:
        assert nombre in liste

    m = MultiSet()
    for rien in m:
        assert False
    m.add('cobaye', 123)
    m.add('sujet', 92)
    cpt = 0
    for x in m:
        cpt += 1
    assert cpt == 2

def test_to_List():
    m = MultiSet('ceci est un test')
    liste = m.to_List()
    cpt = 0
    for x in m:
        cpt += 1
    assert len(liste) == cpt
    liste.pop(0)
    assert liste != m.to_List()

def test_mul():
    A = MultiSet((1, 3, 2, 3, 5, 4, 5))
    B = MultiSet((1, 3, 7))
    C = A * B
    for x in (1, 2, 3, 4, 5, 7):
        if x == 1 or x == 3:
            assert C.multiplicite(x) == 1
        else:
            assert x not in C



def test_to_Dict():
    m = MultiSet([('a', 3), 7])
    assert m.multiplicite('a') == 3
    stockage = m.to_Dict()
    assert type(stockage) is dict
    assert stockage['a'] == 3
    assert stockage[7] == 1
    stockage['a'] = 9
    assert m.multiplicite('a') == 3


if __name__ == '__main__':
    test_add()
    test_str()
    test_repr()
    test_contains()
    test_multiplicite()
    test_iter()
    test_len()
    test_to_List()
    test_to_Dict()
    test_mul()
