class MultiSet(object):
    def __init__(self, entrant: (set, list, tuple, dict, str) = None):
        self.stockage = {}
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
    def add(self, objet: object, n: int =1) -> None:
        "Rajoute n fois l'élément object dans le multiset"
        pass