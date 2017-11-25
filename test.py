class Universite(object):
    def __init__(self, name: str, capacity: int = 5000):
        self.name = name
        self.capacity = capacity

    def presenter(self, fancy: bool = False) -> str:
        if fancy:
            return "Bonjour mesdemoiselles et messieurs, je suis l'université de {}" \
                   " et je peux accueillir {} étudiants".format(self.name, self.capacity)
        else:
            return "Université de {} -- capacité d'accueil : {} étudiants".format(self.name, self.capacity)


if __name__ == '__main__':
    univ1 = Universite('Bordeaux', capacity=15000)
    univ2 = Universite('Toulouse')
    print(univ1.presenter())
    print(univ2.presenter(True))
    dictionnaire = {
        "clé": 7,
        "b": 4,
        45: 1,
        [1, 2, 7, 9]: 1
    }