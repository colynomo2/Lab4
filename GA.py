from random import randint

from Chromosome import Chromosome


class GA:

    def __init__(self, populationSize, problParam):
        self.__populationSize = populationSize
        self.__problParam = problParam
        self.__population = []

    def initialization(self):
        for _ in range(0, self.__populationSize):
            c = Chromosome(self.__problParam)
            self.__population.append(c)
        self.evaluation(self.__population)
        for i in range(self.__populationSize - 1):
            for j in range(i + 1, self.__populationSize):
                if self.__population[i].fitness > self.__population[j].fitness:
                    aux = self.__population[i]
                    self.__population[i] = self.__population[j]
                    self.__population[j] = aux

    def evaluation(self, list):
        for c in list:
            dist = 0
            matrix = self.__problParam['mat']
            for i in range(len(c.repres) - 1):
                dist += matrix[c.repres[i]][c.repres[i + 1]]
            dist += matrix[c.repres[len(c.repres) - 1]][c.repres[0]]
            c.fitness = dist

    def worstChromosome(self):
        best = self.__population[0]
        for c in self.__population:
            if (c.fitness > best.fitness):
                best = c
        return best

    def bestChromosome(self):
        return self.__population[0]


    def selection(self):
        pos1 = randint(0, self.__populationSize - 1)
        pos2 = randint(0, self.__populationSize - 1)
        if (self.__population[pos1].fitness < self.__population[pos2].fitness):
            return pos1
        else:
            return pos2

    def newPopulation(self):
        newPopulation = []
        for _ in range(self.__populationSize):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            off.mutation()
            newPopulation.append(off)
        self.evaluation(newPopulation)
        for i in range(len(newPopulation) - 1):
            for j in range(i + 1, len(newPopulation)):
                if newPopulation[i].fitness > newPopulation[j].fitness:
                    aux = newPopulation[i]
                    newPopulation[i] = newPopulation[j]
                    newPopulation[j] = aux
        return newPopulation

    def oneGeneration(self):
        newGen = self.newPopulation()
        newPop = []
        i = 0
        for i in range(int(self.__populationSize / 2)):
            newPop.append(self.__population[i])
        p = 0
        for j in range(i + 1, self.__populationSize):
            newPop.append(newGen[p])
            p += 1
        self.__population = newPop
        self.evaluation(self.__population)
        for i in range(self.__populationSize-1):
            for j in range(i+1,self.__populationSize):
                if self.__population[i]>self.__population[j]:
                    aux = self.__population[i]
                    self.__population[i] = self.__population[j]
                    self.__population[j] = aux

