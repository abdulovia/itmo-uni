class Country:
    def __init__(self, capital='', population=''):
        self.capital = capital
        self.population = population

    def setPopulation(self, population):
        self.population = population

    def getPopulation(self):
        print(self.population)


class Russia(Country):
    capital = 'Moscow'


class Canada(Country):
    capital = 'Ottawa'


class Germany(Country):
    capital = 'Berlin'
    population = 1000000


rus = Russia('Saint Petersburgh', '120M')
can = Canada('Wont', '10m')
ger = Germany
rus.setPopulation('143m')
rus.getPopulation()
can.getPopulation()
print(rus.capital, rus.population)
print(can.capital, can.population)
print(ger.capital, ger.population)