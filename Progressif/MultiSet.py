class MultiSet(object):
    def __init__(self, entrant: (set, list, tuple, dict, str) = None):
        """Constructeur du MultiSet"""
        self.__stockage = {}
        if isinstance(entrant, str):
            ignored = 0
            for caractere in entrant:
                if caractere.isalpha():
                    self.add(caractere)
                else:
                    ignored += 1
            print("Ignoring {} values out of {}".format(ignored, len(entrant)))
        if isinstance(entrant, (list, tuple)):
            for element in entrant:
                if isinstance(element, (list, tuple)):
                    if len(element) == 1:
                        self.add(element[0])
                    elif len(element) >= 2:
                        self.add(element[0], element[1])
                else:
                    self.add(element)
        if isinstance(entrant, set):
            for element in entrant:
                self.add(element)
        if isinstance(entrant, dict):
            for key, number in entrant.items():
                self.add(key, number)

    # =========================================================================
    def add(self, objet: object, n: int = 1) -> None:
        """Rajoute n fois l'élément object dans le MultiSet"""
        if isinstance(n, int) and n > 0:
            if objet in self:
                self.__stockage[objet] += n
            else:
                self.__stockage[objet] = n

    # =========================================================================
    def __len__(self) -> int:
        """Renvoie le nombre total d'éléments du MultiSet"""
        somme = 0
        for element in self:
            somme = self.mt(element)
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
        for valeur, nombre in self.__stockage.items():
            final += "  {}: {},\n".format(repr(valeur), repr(nombre))
        return final[:-2] + "}}"  # On supprime le dernier retour à la ligne et la virgule

    # =========================================================================
    def __contains__(self, item: object) -> bool:
        """Renvoie vrai si la multiplicité de l'élément est supérieure à 0"""
        # Vrai car on ne peut pas avoir stockage[qqch] == 0
        return item in self.__stockage.keys()

    # =========================================================================
    def mt(self, item: object) -> int:
        """Renvoie le nombre d'occurences de l'élément dans le MultiSet"""
        if item in self:
            return self.__stockage[item]
        return 0

    # =========================================================================
    def copy(self) -> 'MultiSet':
        """Renvoie un MultiSet avec les mêmes éléments"""
        return MultiSet(self.to_Dict())

    # =========================================================================
    def to_Set(self) -> set:
        """Renvoie un set contenant l'ensemble support de ce MultiSet"""
        return_set = set()
        for element in self:  # Parcours le support
            return_set.add(element)
        return return_set

    # =========================================================================
    def to_List(self) -> list:
        """Renvoie une liste de couples (element, multiplicité)"""
        return_list = []
        for element, multiplicite in self.__stockage.items():
            return_list.append((element, multiplicite))
        return return_list

    # =========================================================================
    def to_Dict(self) -> dict:
        """Renvoie un dictionnaire sous la forme """
        return self.__stockage.copy()

    # =========================================================================
    def __mul__(self, m_set: 'MultiSet') -> 'MultiSet':
        """Renvoie l'intersection entre deux MultiSet"""
        assert type(m_set) is MultiSet
        new_mset = MultiSet()
        for a in self:
            if a in m_set:
                new_mset.add(a, min(self.mt(a),
                                    m_set.mt(a)))
        return new_mset

    # =========================================================================
    def __add__(self, m_set: 'MultiSet') -> 'MultiSet':
        """Renvoie l'union entre deux MultiSet"""
        assert type(m_set) is MultiSet
        new_mset = MultiSet()
        for a in self:
            new_mset.add(max(self.mt(a),
                             m_set.mt(a)))
        for b in m_set:
            if b not in self:
                new_mset.add(m_set.mt(b))
        return new_mset

    # =========================================================================
    def __sub__(self, m_set: 'MultiSet') -> 'MultiSet':
        """Renvoie la différence entre deux MultiSet"""
        assert type(m_set) is MultiSet
        new = MultiSet()
        for element in self:
            new.add(element, self.mt(element) - m_set.mt(element))
        return new

    # =========================================================================
    def __mod__(self, m_set: 'MultiSet') -> 'MultiSet':
        """Renvoie la différence symétrique entre deux MultiSet"""
        assert type(m_set) is MultiSet
        new = MultiSet()
        for element in self:
            if element not in m_set:
                new.add(element, abs(self.mt(element) -
                                     m_set.mt(element)))
        for element in m_set:
            if element not in self:
                if element not in m_set:
                    new.add(element, abs(self.mt(element) -
                                         m_set.mt(element)))
        return new

    # =========================================================================
    def __lt__(self, m_set: 'MultiSet') -> bool:
        """Vérifie si le premier MultiSet est inclus dans le second"""
        assert type(m_set) is MultiSet
        for element in self:
            if element not in m_set or \
                            self.mt(element) >= m_set.mt(element):
                return False
        return True

    # =========================================================================
    def __le__(self, m_set):
        """Vérifie si le second MultiSet est inclus dans le premier"""
        assert type(m_set) is MultiSet
        for element in self:
            if element not in m_set or \
                            self.mt(element) > m_set.multiplicity(element):
                return False
        return True

    # =========================================================================
    def __eq__(self, m_set):
        """Vérifie si les deux multisets ont les mêmes éléments"""
        assert type(m_set) is MultiSet
        for element in self:
            if self.mt(element) != m_set.multiplicity(element):
                return False
        for element in m_set:
            if m_set.multiplicity(element) != self.mt(element):
                return False

    # =========================================================================
    def union(self, *m_sets: tuple('MultiSet')) -> 'MultiSet':
        """Renvoie l'union entre n >= 1 MultiSets"""
        new_mset = self
        for mSet in m_sets:
            assert isinstance(mSet, MultiSet)
            new_mset += mSet
        return new_mset

    # =========================================================================
    def intersection(self, *m_sets: tuple('MultiSet')) -> 'MultiSet':
        """Renvoie l'intersection entre n >= 1 MultiSets"""
        new_mset = self
        for mSet in m_sets:
            assert isinstance(mSet, MultiSet)
            new_mset *= mSet
        return new_mset

    # =========================================================================
    def sup(self, n: int = 0) -> set:
        """Renvoie l'ensemble des éléments présents n fois ou plus"""
        if type(n) is not int or n <= 0:
            return set()
        support = set()
        for element in self:
            if self.mt(element) > n:
                support.add(element)
        return support

    # =========================================================================
    def inf(self, n: int = 0) -> set:
        """Renvoie l'ensemble des éléments présents n fois ou moins"""
        if type(n) is not int or n <= 0:
            return set()
        support = set()
        for element in self:
            if self.mt(element) < n:
                support.add(element)
        return support

    # =========================================================================
    def cut(self, n: int = 0) -> set:
        """Renvoie l'ensemble des éléments présents exactement n fois"""
        if type(n) is not int or n <= 0:
            return set()
        support = set()
        for element in self:
            if self.mt(element) == n:
                support.add(element)
        return support

    # =========================================================================
    def delete(self, objet: object, number: int) -> None:
        """Supprime n occurences d'un élément"""
        if objet in self and type(number) is int and number > 0:
            self.__stockage[objet] -= number
            if self.__stockage[objet] <= 0:
                self.__stockage.pop(objet)

    # =========================================================================
    def elements(self):
        """Renvoie un itérateur sur les éléments du MultiSet"""
        for element in self:
            for x in range(self.mt(element)):
                yield x


if __name__ == '__main__':
    d = {1: 5, 'a': 2}
    m = MultiSet(d)
    print(repr(m))
