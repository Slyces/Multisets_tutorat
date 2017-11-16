class MultiSet(object):
    def __init__(self, entrant: (set, list, tuple, dict, str) = None):
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
        "Rajoute n fois l'élément object dans le multiset"
        if isinstance(n, int) and n > 0:
            if objet in self:
                self.__stockage[objet] += n
            else:
                self.__stockage[objet] = n

    # =========================================================================
    def __repr__(self) -> str:
        "Rajoute n fois l'élément object dans le multiset"
        return "MultiSet({})".format(str(self.__stockage))

    # =========================================================================
    def __str__(self) -> str:
        "Rajoute n fois l'élément object dans le multiset"
        final = "{{\n"
        for valeur, nombre in self.__stockage.items():
            final += "  {}: {},\n".format(repr(valeur), repr(nombre))
        return final[:-2] + "}}"  # On supprime le dernier retour à la ligne et la virgule

    # =========================================================================
    def __contains__(self, item: object) -> bool:
        # Vrai car on ne peut pas avoir stockage[qqch] == 0
        return item in self.__stockage.keys()

    # =========================================================================
    def multiplicite(self, item: object) -> int:
        if item in self:
            return self.__stockage[item]
        return 0

    # =========================================================================
    def __len__(self) -> int:
        return sum(self.__stockage.values())

    # =========================================================================
    def __iter__(self):
        return iter(self.__stockage.keys())

    # =========================================================================
    def to_Set(self) -> set:
        return_set = set()
        for element in self: # Parcours le support
            return_set.add(element)
        return return_set

    # =========================================================================
    def to_List(self) -> list:
        return_list = []
        for element, multiplicite in self.__stockage.items():
            return_list.append((element, multiplicite))
        return return_list

    # =========================================================================
    def to_Dict(self) -> dict:
        return self.__stockage.copy()

    # =========================================================================
    def __mul__(self, mSet: 'MultiSet') -> 'MultiSet':
        new_mset = MultiSet()
        for a in self:
            if a in mSet:
                new_mset.add(a, min(self.multiplicite(a),
                                    mSet.multiplicite(a)))
        return new_mset

    # =========================================================================
    def __add__(self, mSet: 'MultiSet') -> 'MultiSet':
        new_mset = MultiSet()
        for a in self:
            new_mset.add(max(self.multiplicite(a),
                             mSet.multiplicite(a)))
        for b in mSet:
            if b not in self:
                new_mset.add(mSet.multiplicite(b))
        return new_mset

    # =========================================================================
    def copy(self):
        return MultiSet(self.to_Dict())

    # =========================================================================
    def union(self, *mSets: tuple('MultiSet')) -> 'MultiSet':
        new_mset = self
        for mSet in mSets:
            assert isinstance(mSet, MultiSet)
            new_mset += mSet
        return new_mset

    # =========================================================================
    def intersection(self, *mSets: tuple('MultiSet')) -> 'MultiSet':
        new_mset = self
        for mSet in mSets:
            assert isinstance(mSet, MultiSet)
            new_mset *= mSet
        return new_mset

    # =========================================================================
    def delete(self, objet: object, number: int) -> None:
        if objet in self:
            self.__stockage[objet] -= number
            if self.__stockage[objet] <= 0:
                self.__stockage.pop(objet)

    # =========================================================================
    def elements(self):
        for element in self:
            for x in range(self.multiplicite(element)):
                yield x

if __name__ == '__main__':
    d = {1: 5, 'a': 2}
    m = MultiSet(d)
    print(repr(m))
