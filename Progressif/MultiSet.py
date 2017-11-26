import collections


class MultiSet(object):
    def __init__(self, entrant: (set, list, tuple, dict, str) = None):
        """Constructeur du MultiSet"""
        self.__stockage = {}
        if isinstance(entrant, str):  # 1
            caracteres_ignores = 0
            for caractere in entrant:  # n
                if caractere.isalpha():  # 1
                    self.ajoute(caractere)  # 1
                else:
                    caracteres_ignores += 1  # 1
            print("Ignoring {} values out of {}".format(caracteres_ignores, len(entrant)))  # 1
        if isinstance(entrant, (list, tuple)):
            for element in entrant:
                if isinstance(element, (list, tuple)):
                    if len(element) == 1:
                        self.ajoute(element[0])
                    elif len(element) >= 2:
                        self.ajoute(element[0], element[1])
                else:
                    self.ajoute(element)
        if isinstance(entrant, set):
            for element in entrant:
                self.ajoute(element)
        if isinstance(entrant, dict):
            for key, nombre in entrant.items():
                self.ajoute(key, nombre)

    # =========================================================================
    def ajoute(self, element: object, n: int = 1) -> None:
        """Rajoute n fois l'élément object dans le MultiSet"""
        if isinstance(element, collections.Hashable) and isinstance(n, int) and n > 0:  # 1
            if element in self:  # 1
                self.__stockage[element] += n  # 1
            else:  # 1
                self.__stockage[element] = n  # 1

    # =========================================================================
    def __len__(self) -> int:
        """Renvoie le nombre total d'éléments du MultiSet"""
        somme = 0
        for element in self:
            somme += self.multiplicity(element)
        return somme

    # =========================================================================
    def __iter__(self):
        """Parcourt l'ensemble support du MultiSet"""
        liste = []
        for key in self.__stockage.keys():
            liste.append(key)
        return iter(liste)

    # =========================================================================
    def __repr__(self) -> str:
        """Rajoute n fois l'élément object dans le MultiSet"""
        return "MultiSet({})".format(str(self.__stockage))

    # =========================================================================
    def __str__(self) -> str:
        """Rajoute n fois l'élément object dans le MultiSet"""
        final = "{{\n"
        if len(self) == 0:
            return "{{}}"
        for support, mult in self.couples():
            final += "  {}: {},\n".format(repr(support), repr(mult))
        return final[:-2] + "}}"  # On supprime le dernier retour à la ligne et la virgule

    # =========================================================================
    def __contains__(self, element: object) -> bool:
        """Renvoie vrai si la multiplicité de l'élément est supérieure à 0"""
        # Vrai car on ne peut pas avoir stockage[qqch] == 0
        # mais on vérifie, on sait jamais
        if not isinstance(element, collections.Hashable):
            return False
        if element in self.__stockage.keys():
            if self.__stockage[element] <= 0:
                self.__stockage.pop(element)
        return element in self.__stockage.keys()

    # =========================================================================
    def multiplicity(self, element: object) -> int:
        """Renvoie le nombre d'occurences de l'élément dans le MultiSet"""
        if element in self:
            return self.__stockage[element]
        return 0

    # =========================================================================
    def copy(self) -> 'MultiSet':
        """Renvoie un MultiSet avec les mêmes éléments"""
        return MultiSet(self.to_Dict())

    # =========================================================================
    def couples(self):
        """Renvoie un itérateur sur les couples (élément, multiplicité)"""
        return self.__stockage.items()

    # =========================================================================
    def to_Set(self) -> set:
        """Renvoie un set contenant l'ensemble support de ce MultiSet"""
        nouveau_set = set()
        for element in self:  # Parcours le support
            nouveau_set.add(element)
        return nouveau_set

    # =========================================================================
    def to_List(self) -> list:
        """Renvoie une liste de couples (element, multiplicité)"""
        nouvelle_liste = []
        for element, multiplicite in self.couples():
            nouvelle_liste.append((element, multiplicite))
        return nouvelle_liste

    # =========================================================================
    def to_Dict(self) -> dict:
        """Renvoie un dictionnaire sous la forme """
        return self.__stockage.copy()

    # =========================================================================
    def __mul__(self, m_set: 'MultiSet') -> 'MultiSet':
        """Renvoie l'intersection entre deux MultiSet"""
        assert type(m_set) is MultiSet
        nouveau_mset = MultiSet()
        for a in self:
            if a in m_set:
                nouveau_mset.ajoute(a, min(self.multiplicity(a),
                                           m_set.multiplicity(a)))
        return nouveau_mset

    # =========================================================================
    def __add__(self, m_set: 'MultiSet') -> 'MultiSet':
        """Renvoie l'union entre deux MultiSet"""
        assert type(m_set) is MultiSet
        nouveau_mset = MultiSet()
        for a in self:
            nouveau_mset.ajoute(a, max(self.multiplicity(a),
                                       m_set.multiplicity(a)))
        for b in m_set:
            if b not in self:
                nouveau_mset.ajoute(b, m_set.multiplicity(b))
        return nouveau_mset

    # =========================================================================
    def __sub__(self, m_set: 'MultiSet') -> 'MultiSet':
        """Renvoie la différence entre deux MultiSet"""
        assert type(m_set) is MultiSet
        nouveau_mset = MultiSet()
        for element in self:
            nouveau_mset.ajoute(element, self.multiplicity(element) - m_set.multiplicity(element))
        return nouveau_mset

    # =========================================================================
    def __mod__(self, m_set: 'MultiSet') -> 'MultiSet':
        """Renvoie la différence symétrique entre deux MultiSet"""
        assert type(m_set) is MultiSet
        nouveau_mset = MultiSet()
        for a in self:
            if a not in m_set:
                nouveau_mset.ajoute(a, self.multiplicity(a))
        for b in m_set:
            if b not in self:
                nouveau_mset.ajoute(b, m_set.multiplicity(b))
        return nouveau_mset

    # =========================================================================
    def __lt__(self, m_set: 'MultiSet') -> bool:
        """Vérifie si le premier MultiSet est inclus dans le second"""
        assert type(m_set) is MultiSet
        for element in m_set:
            if element not in self or \
                            self.multiplicity(element) < m_set.multiplicity(element):
                return True
        return False

    # =========================================================================
    def __le__(self, m_set):
        """Vérifie si le second MultiSet est inclus dans le premier"""
        assert type(m_set) is MultiSet
        for element in self:
            if element not in self or \
                            self.multiplicity(element) > m_set.multiplicity(element):
                return False
        return True

    # =========================================================================
    def __eq__(self, m_set):
        """Vérifie si les deux multisets ont les mêmes éléments"""
        assert type(m_set) is MultiSet
        for element in self:
            if self.multiplicity(element) != m_set.multiplicity(element):
                return False
        for element in m_set:
            if m_set.multiplicity(element) != self.multiplicity(element):
                return False
        return True

    # =========================================================================
    def union(self, *m_sets: tuple('MultiSet')) -> 'MultiSet':
        """Renvoie l'union entre n >= 1 MultiSets"""
        nouveau_mset = self.copy()
        for mset in m_sets:
            assert isinstance(mset, MultiSet)
            nouveau_mset += mset
        return nouveau_mset

    # =========================================================================
    def intersection(self, *m_sets: tuple('MultiSet')) -> 'MultiSet':
        """Renvoie l'intersection entre n >= 1 MultiSets"""
        nouveau_mset = self.copy()
        for mset in m_sets:
            assert isinstance(mset, MultiSet)
            nouveau_mset *= mset
        return nouveau_mset

    # =========================================================================
    def sup(self, n: int = 0) -> set:

        """Renvoie l'ensemble des éléments présents n fois ou plus"""
        if type(n) is not int or n <= 0:
            return set()
        support = set()
        for element in self:
            if self.multiplicity(element) > n:
                support.add(element)
        return support

    # =========================================================================
    def inf(self, n: int = 0) -> set:
        """Renvoie l'ensemble des éléments présents n fois ou moins"""
        if type(n) is not int or n <= 0:
            return set()
        support = set()
        for element in self:
            if self.multiplicity(element) < n:
                support.add(element)
        return support

    # =========================================================================
    def cut(self, n: int = 0) -> set:
        """Renvoie l'ensemble des éléments présents exactement n fois"""
        if type(n) is not int or n <= 0:
            return set()
        support = set()
        for element in self:
            if self.multiplicity(element) == n:
                support.add(element)
        return support

    # =========================================================================
    def supprime(self, element: object, nombre: int) -> None:
        """Supprime n occurences d'un élément"""
        if element in self and type(nombre) is int and nombre > 0:
            self.__stockage[element] -= nombre
            if self.__stockage[element] <= 0:
                self.__stockage.pop(element)

    # =========================================================================
    def elements(self):
        """Renvoie un itérateur sur les éléments du MultiSet"""
        liste = []
        for element in self:
            for x in range(self.multiplicity(element)):
                liste.append(element)
        return iter(liste)


if __name__ == '__main__':
    d = {1: 5, 'a': 2}
    m = MultiSet(d)
    print(repr(m))
