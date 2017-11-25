# Test des axiomes
import random

from Progressif.MultiSet import MultiSet


def test_init():
    params = [
        [0, 7, 4, 'lokkzeeazdq', {'2165': 132, '_': int, -0.214: 46}, MultiSet(), ('tout', 12), (1, 7, 5, set())],
        {7: 5, 'lokkzeeazdq': 98, 15: 'quatre-vingt-quinze', 32: 7},
        {1, 7, 8, 'test', 12, 4, 18},
        "Ceci est un lorem ipsum sit dolor amet nec plus ultra hacked sans os. Avec windows 10. Donc avec os. Paradoxe.",
        None
    ]
    for (par, i) in enumerate(params):
        print(">> m" + str(i) + ") = Multiset(" + repr(par) + ")")
        print(">> m" + str(i))
        print(MultiSet(par))


def test_repr():
    a = MultiSet([(1, 2), (3, 4, 5, 6), 7])
    assert repr(a) == 'MultiSet({1: 2, 3: 4, 7: 1})'
    b = MultiSet({'une chaine': 12})
    assert repr(b) == "MultiSet({'une chaine': 12})"
    assert repr(MultiSet()) == "MultiSet({})"


def test_str():
    a = MultiSet([(3, 4, 5, 6)])
    assert str(a) == """{{\n  3: 4}}"""
    b = MultiSet({'a': 2})
    assert str(b) == """{{\n  'a': 2}}"""
    assert str(MultiSet()) == """{{}}"""


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
    vide = MultiSet()
    A = MultiSet((1, 3, 2, 3, 5, 4, 5))
    B = MultiSet((1, 3, 7))
    C = A * B
    assert C <= A
    assert C <= B
    for x in (1, 2, 3, 4, 5, 7):
        if x == 1 or x == 3:
            assert C.mt(x) == 1
        else:
            assert x not in C
    for M in (A, B, C, vide):
        assert M * M == M
        assert M * vide == vide


def test_add():
    A = MultiSet((1, 3, 2, 3, 5, 4, 5))
    B = MultiSet((1, 1, 3, 7))
    C = A + B
    assert A <= C
    assert B <= C
    vide = MultiSet()
    for M in (A, B, C, vide):
        assert M + M == M
        assert M + vide == M

def test_sub():
    A = MultiSet((1, 3, 6, 2, 5, 4, 5))
    B = MultiSet((1, 3, 7, 45))
    C = A - B
    assert C <= A
    vide = MultiSet()
    for M in (A, B, C, vide):
        assert M - M == vide
        assert M - vide == M


def test_mod():
    A = MultiSet((1, 3, 6, 2, 5, 4, 5))
    B = MultiSet((1, 3, 7, 45))
    C = A % B
    D = (A - B) + (B - A)
    E = (A + B) - (A * B)
    assert C == D
    assert D == E
    vide = MultiSet()
    for M in (A, B, C, vide):
        assert M % M == vide
        assert M % vide == M


def test_lt():
    parametre = [1, 2, 4, 4, 5, 7, 1, 4, 1, 2, 3, 5, 4, 7, 7, 8,
                 8, 9, 6, 5, 4, 1, 2, 3, "ok", "j", {"test": 7}]

    M1 = MultiSet(parametre)
    M2 = MultiSet(parametre)
    M3 = MultiSet(parametre[3:12])
    M4 = MultiSet(parametre[7:12])

    assert not M1 < M2
    assert M4 < M3
    assert M3 < M1

    for x in (M1, M2, M3, M4):
        for y in (M1, M2, M3, M4):
            if x < y:
                assert len(x) < len(y)
            for z in (M1, M2, M3, M4):
                if (x < y) and (y < z):
                    assert x < z


def test_eq():
    parametre = [1, 2, 4, 4, 5, 7, 1, 4, 1, 2, 3, 5, 4, 7, 7, 8,
                 8, 9, 6, 5, 4, 1, 2, 3, "ok", "j", {"test": 7}]

    M1 = MultiSet(parametre)
    M2 = MultiSet(parametre)
    M3 = MultiSet(parametre[3:12])
    M4 = MultiSet(parametre[7:12])
    M5 = MultiSet(parametre)

    assert M1 is not M2  # Pas le même objet Python
    assert M1 == M2
    assert M3 != M4
    assert M1 != M3

    for x in (M1, M2, M3, M4, M5):
        for y in (M1, M2, M3, M4, M5):
            if x == y:
                assert len(x) == len(y)
            for z in (M1, M2, M3, M4, M5):
                if (x == y) and (y == z):
                    assert x == z


def test_le():
    parametre = [1, 2, 4, 4, 5, 7, 1, 4, 1, 2, 3, 5, 4, 7, 7, 8,
                 8, 9, 6, 5, 4, 1, 2, 3, "ok", "j", {"test": 7}]

    M1 = MultiSet(parametre)
    M2 = MultiSet(parametre)
    M3 = MultiSet(parametre[3:12])
    M4 = MultiSet(parametre[7:12])

    assert M1 <= M2
    assert M4 <= M3
    assert not M3 <= M4
    assert M3 <= M1

    for x in (M1, M2, M3, M4):
        for y in (M1, M2, M3, M4):
            if x <= y:
                assert len(x) <= len(y)
            for z in (M1, M2, M3, M4):
                if (x <= y) and (y <= z):
                    assert x <= z


def test_to_Set():
    m = MultiSet([(1, 7), ('o', 2), (8, 23, 14, 7)])
    assert m.to_Set() == {1, 'o', 8}
    l = [1, 7, 4, 5, 6, 1, 1, 4, 7, 5, 4, 1, 2]
    assert set(l) == MultiSet(l).to_Set()


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

    assert m.mt('test') == 0
    assert m.mt({1: 2, 3: 4, 5: 6, 7: 8}) == 0

    m.add('p', -5478)
    assert m.mt('p') == 0

    m.delete('o', 165465)
    assert m.mt('o') == 0


def test_union():
    assert False


def test_intersection():
    assert False


def test_ajoute():
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

    m2 = MultiSet()

    for i in range(20):
        for n in (1, 4, 2, 7, 1, 3, 8, 9, 4):
            element = random.randrange(4)
            m1 = m2.copy()
            m2.add(element, n)
            assert m2.mt(element) - m1.mt(element) == n
            assert len(m1) < len(m2)
            assert m1 < m2


def test_supprime():
    param = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}
    M = MultiSet(param)
    for element in M:
        M.add(element, 2 + random.randrange(8))  # On ajoute de 2 à 9 éléments, donc
        # chaque élément est présent de 3 à 10 fois

    M.delete(1, 20)
    assert 1 not in M
    assert M.mt(1) == 0

    for element in param:
        avant = M.mt(element)
        M.delete(element, 3)
        apres = M.mt(element)
        assert avant == 0 or apres < avant


def test_sup():
    M = MultiSet([0, 7, 4, 'lokkzeeazdq', {'2165': 132, '_': int, "o": 46}, MultiSet(), ('tout', 12), (1, 7, 5, set())])
    N = MultiSet(
        "Ceci est un lorem ipsum sit dolor amet nec plus ultra hacked sans os. Avec windows 10. Donc il y a 1 os. Mé non. Paradoxe.")
    assert len(M.sup(3)) <= len(M)
    MSup = M.sup(5)
    for x in M.sup(5):
        assert M.mt(x) > 5
    for x in M:
        assert not(M.mt(x) > 5 and x not in MSup)

    NSup = N.sup(5)
    for x in N.sup(5):
        assert N.mt(x) > 5
    for x in N:
        assert not (N.mt(x) > 5 and x not in NSup)

def test_inf():
    M = MultiSet([0, 7, 4, 'lokkzeeazdq', {'2165': 132, '_': int, 14: 46}, MultiSet(), ('tout', 12), (1, 7, 5, set())])
    N = MultiSet(
        "Ceci est un lorem ipsum sit dolor amet nec plus ultra hacked sans os. Avec windows 10. Donc il y a 1 os. Mé non. Paradoxe.")
    assert len(M.inf(3)) <= len(M)
    Minf = M.inf(9)
    for x in M.inf(9):
        assert M.mt(x) < 9
    for x in M:
        assert not(M.mt(x) < 9 and x not in Minf)

    Ninf = N.inf(9)
    for x in N.inf(9):
        assert N.mt(x) < 9
    for x in N:
        assert not (N.mt(x) < 9 and x not in Ninf)


def test_cut():
    M = MultiSet([0, 7, 4, 'lokkzeeazdq', {'2165': 132, '_': int, 654: 46}, MultiSet(), ('tout', 12), (1, 7, 5, set())])
    N = MultiSet(
        "Ceci est un lorem ipsum sit dolor amet nec plus ultra hacked sans os. Avec windows 10. Donc il y a 1 os. Mé non. Paradoxe.")
    assert len(M.sup(6)) <= len(M)
    MSup = M.sup(7)
    for x in M.sup(7):
        assert M.mt(x) > 7
    for x in M:
        assert not(M.mt(x) > 7 and x not in MSup)

    NSup = N.sup(7)
    for x in N.sup(7):
        assert N.mt(x) > 7
    for x in N:
        assert not (N.mt(x) > 7 and x not in NSup)


def test_elements():
    M = MultiSet([0, 7, 4, 'lokkzeeazdq', {'2165': 132, '_': int, 4654: 46}, MultiSet(), ('tout', 12), (1, 7, 5, set())])
    N = MultiSet(
        "Ceci est un lorem ipsum sit dolor amet nec plus ultra hacked sans os. Avec windows 10. Donc il y a 1 os. Mé non. Paradoxe.")
    cpt = 0
    for x in M.elements():
        cpt += 1
    assert cpt == len(M)



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
