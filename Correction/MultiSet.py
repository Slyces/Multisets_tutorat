from typing import Any, Union


class MultiSet(object):
    def __init__(self, iterable=None):
        self.__values = {}
        variable = 0
        if isinstance(iterable, str):
            for char in iterable:
                if char.isalpha():
                    self.add(char)
        if isinstance(iterable, dict):
            for element, number in iterable.items():
                self.add(element, number)
        if isinstance(iterable, (set, list, tuple)):
            for element in iterable:
                if isinstance(element, (tuple, list)) and len(element) > 1:
                    self.add(element[0], element[1])
                else:
                    self.add(element)

    # =========================================================================
    def add(self, element: object, n: int = 1) -> None:
        if isinstance(n, int) and n > 0:
            if element in self:
                self.__values[element] += n
            else:
                self.__values[element] = n

    def remove(self, element, n=1):
        self.__values[element] += n
        if self.__values[element] <= 0:
            self.__values.pop(element)

    def multiplicity(self, element):
        if element in self.__values:
            return self.__values[element]
        return 0

    # =========================================================================
    def __pairs(self):
        # Cette fonction est très utilisée en interne. La redéfinir permet
        # d'obtenir un résultat moins dépendant de l'implémentation
        for item, number in self.__values.items():
            yield item, number

    # =========================================================================
    def copy(self):
        return MultiSet(self.to_List())

    # =========================================================================
    def __len__(self):
        return sum(self.__values.values())

    def __iter__(self):
        for element in self.__values.keys():
            yield element

    def __contains__(self, item):
        return item in self.__values and self.__values[item] > 0

    # =========================================================================
    def __repr__(self):
        return 'Multiset(' + repr(self.__values) + ')'

    def __str__(self):
        return '{{\n   ' + ',\n   '.join(repr(self.__values)[1:-1].split(', ')) + '}}'

    # =========================================================================
    def to_Set(self):
        return set(self.__values.keys())

    def to_List(self):
        return list(self.__pairs())

    def to_Dict(self):
        return self.__values.copy()

    # =========================================================================
    def __mul__(self, mset):
        new = MultiSet()
        for element in self:
            if element in mset:
                new.add(element, min(self.multiplicity(element),
                                     mset.multiplicity(element)))
        return new

    def __add__(self, mset):
        new = MultiSet()
        for element in self:
            new.add(element, max(self.multiplicity(element),
                                 mset.multiplicity(element)))
        for element in mset:
            if element not in new:
                new.add(element, max(self.multiplicity(element),
                                     mset.multiplicity(element)))
        return new

    def __sub__(self, mset):
        new = MultiSet()
        for element in self:
            new.add(element, self.multiplicity(element) - mset.multiplicity(element))
        return new

    def __mod__(self, mset):
        new = MultiSet()
        for element in self:
            if element not in mset:
                new.add(element, abs(self.multiplicity(element) -
                                     mset.multiplicity(element)))
        for element in mset:
            if element not in self:
                if element not in mset:
                    new.add(element, abs(self.multiplicity(element) -
                                         mset.multiplicity(element)))
        return new

    def __lt__(self, mset):
        for element in self:
            if element not in mset or \
                            self.multiplicity(element) >= mset.multiplicity(element):
                return False
        return True

    def __le__(self, mset):
        for element in self:
            if element not in mset or \
                            self.multiplicity(element) > mset.multiplicity(element):
                return False
        return True

    def __eq__(self, mset):
        for element in self:
            if self.multiplicity(element) != mset.multiplicity(element):
                return False
        for element in mset:
            if mset.multiplicity(element) != self.multiplicity(element):
                return False

    # =========================================================================
    def union(self, *mset_list):
        somme = self.copy()
        for mset in mset_list:
            if isinstance(mset, MultiSet):
                somme += mset
        return somme

    def intersection(self, *mset_list):
        inter = self.copy()
        for mset in mset_list:
            if isinstance(mset, MultiSet):
                inter -= mset
        return inter

    def sup(self, n=0):
        support = set()
        for element in self:
            if self.multiplicity(element) > n:
                support.add(element)
        return support

    def inf(self, n=0):
        support = set()
        for element in self:
            if self.multiplicity(element) < n:
                support.add(element)
        return support

    def cut(self, n=0):
        support = set()
        for element in self:
            if self.multiplicity(element) == n:
                support.add(element)
        return support

    def elements(self):
        for element, number in self.__pairs():
            for i in range(number):
                yield element


if __name__ == '__main__':
    m = MultiSet({1: 2, 3: 4, 7: 1, 'op': 8})
    print('repr m :', repr(m))
    print('m :\n', m)
    print(m.to_Set())
    print(m.to_List())
    print(m.to_Dict())
    print(' '.join([str(e) for e in m]))
