# Test des axiomes
from Progressif.MultiSet import MultiSet


def test_init():
    assert False

def test_add():
    m = MultiSet()
    # Signature
    for pas_un_nombre_valide in (-1, 0, 'a', [1, 2, 3]):
        m.add('cobaye', pas_un_nombre_valide)
        assert 'cobaye' not in m

    # Axiomes
    m.add(4)
    assert m.mt(4) == 1
    m.add('un mot', 145)
    assert m.mt('un mot') >= 145


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


def test_contains():
    m = MultiSet()
    assert 0 not in m
    m.add('dix-sept')
    assert 17 not in m
    assert 'dix-sept' in m


def test_mul():
    A = MultiSet((1, 3, 2, 3, 5, 4, 5))
    B = MultiSet((1, 3, 7))
    C = A * B
    for x in (1, 2, 3, 4, 5, 7):
        if x == 1 or x == 3:
            assert C.mt(x) == 1
        else:
            assert x not in C


def test_sub():
    assert False


def test_mod():
    assert False


def test_lt():
    assert False


def test_eq():
    assert False


def test_le():
    assert False


def test_to_Set():
    assert False


def test_to_List():
    m = MultiSet('ceci est un test')
    liste = m.to_List()
    cpt = 0
    for x in m:
        cpt += 1
    assert len(liste) == cpt
    liste.pop(0)
    assert liste != m.to_List()


def test_to_Dict():
    m = MultiSet([('a', 3), 7])
    assert m.mt('a') == 3
    stockage = m.to_Dict()
    assert type(stockage) is dict
    assert stockage['a'] == 3
    assert stockage[7] == 1
    stockage['a'] = 9
    assert m.mt('a') == 3


def test_multiplicite():
    m = MultiSet()
    for i, lettre in enumerate(('a', 'b', 'c', 'd')):
        m.add(lettre, i)
        assert m.mt(lettre) == i

    m.add('o', 18)
    assert m.mt('o') == 18
    m.add('o', 12)
    assert m.mt('o') == 30


def test_union():
    assert False


def test_intersection():
    assert False


def test_ajoute():
    assert False


def test_supprime():
    assert False


def test_sup():
    assert False


def test_inf():
    assert False


def test_cut():
    assert False


def test_elements():
    assert False


if __name__ == '__main__':
    methodes_speciales = "init repr str len iter contains mul sub mod lt eq le"
    methodes_normales = "to_Set to_List to_Dict multiplicite union intersection " \
                        "ajoute supprime sup inf cut elements "

    for nom in (methodes_normales + methodes_speciales).split(" "):
        methode = eval("test_" + nom)
        if nom in methodes_speciales:
            nom = "_" + nom + "__"
        print("=" * 80)
        print("Test de {}".format(nom).center(80))
        print("=" * 80)
        try:
            methode()
            print("test assert passed")
        except:
            print("/!\\ /!\\ TEST FAILED /!\\ /!\\".center(80))
        print("-" * 80)
        print("\n")
