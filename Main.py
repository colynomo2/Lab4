from GA import GA
from fileReader import readNet3, readNet2


def run():
    while True:
        print("1. RUN: \n")
        print("0. Exit\n")

        cmd = input()
        if cmd == "1":
            print("fisierul: \n")
            filename = input()
            if (filename != ""):
                print("marimea populatiei = \n")
                populationSize = int(input())
                print("numarul de generatii = \n")
                numGenerations = int(input())
                graph = readNet3(filename)
                ga = GA(populationSize, graph)
                ga.initialization()
                counterr = 0
                gen = counterr + 1
                best = ga.bestChromosome()
                counterr +=1
                print("generation " + str(gen) + " " + str(best.repres) + " fitness " + str(best.fitness))
                while (counterr < numGenerations):
                    ga.oneGeneration()
                    best = ga.bestChromosome()
                    gen = counterr + 1
                    print("generation " + str(gen) + " " + str(best.repres) + " fitness "+str(best.fitness))
                    counterr += 1

        else:
            break


run()
