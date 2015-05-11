import csv
import random
from pprint import pprint

random.seed('doge')

#Chromosomes are just lists of dictionaries. Dictionary has the {"name": data} format
class Member:
    
    def __init__(self, motherchromosome, fatherchromosome, gender):
        
        self.mchrome = motherchromosome
        self.fchrome = fatherchromosome
        self.gender = gender
    
    def makeGamete(self):
        cutoff = random.randint(0, len(self.mchrome))
        #newchrome = []
        #for i in range(len(self.mchrome)):
        #    newchrome.append(self.fchrome[i] if i < cutoff else self.fchrome[i])
        return self.fchrome[0:cutoff] + self.mchrome[cutoff:len(self.mchrome)]

    #0 = male, 1 = female
    def getGender(self):
        return self.gender
    
    #Other is obviously another member...
    def makeBabby(self, other):#random gendered babby
        if self.getGender() == 1:#make mother first
            return Member(self.makeGamete(), other.makeGamete(), random.randint(0, 1))
        else:
            return Member(other.makeGamete(), self.makeGamete(), random.randint(0, 1))
    
    def getEyeSize(self):
        return (self.mchrome[3]["eyesize"] + self.fchrome[3]["eyesize"]) / 2
    
    def getColor(self):
        s = self.mchrome[2]['color'] + self.fchrome[2]['color']
        if s == 2:
            return 'red'
        if s == 4:
            return 'redgreen'
        if s == 6:
            return 'green'
        if s == 10:
            return 'redblue'
        if s == 12:
            return 'greenblue'
        return 'blue'#18
    
    #0 = small
    #2 = medium
    #4 = large
    def getSize(self):
        return self.mchrome[0]['size'] + self.fchrome[0]['size']
    
    def getHairLength(self):
        return min(self.mchrome[1]['hair'] + self.fchrome[1]['hair'], 2)
    
    def getChromosomes(self):
        return (self.mchrome, self.fchrome)
    
    def __str__(self):
        return "Member: mchr: " + str(self.mchrome) + ", fchr: " + str(self.fchrome)

def makeRandomChromosome():
    #The format:
        #0. 'gender': 0, 1; male, female (mendalian) NOT ON THE MAIN CHROMOSOME. I AM STUPID.
        #1. 'size': 0, 2; incomplete dominance (average the two values)
        #2. 'hair': 0, 2; mendalian, longer is better than shorter
        #3. 'shape': 1, 2, 3; higher is more dominant (31 = 3, 11 = 1)
        #4. 'eyesize': 0, 2; incomplete dominance (average the two values)
    #gendervalues = [0, 1]
    sizevalues = [0, 2]
    hairvalues = [0, 2]
    colorvalues = [1, 3, 9]#red, blue, green: 2: red, 4: redgreen, 10: redblue, 6: green, 18: blue, 12: greenblue
    eyesizevalues = [0, 2]
    
    r = random.randint(0, 7)
    v = None
    if r < 3:
        v = eyesizevalues[0]
    else:
        v = eyesizevalues[1]
    return [{'size': random.choice(sizevalues)}, {'hair': random.choice(hairvalues)}, {'color': random.choice(colorvalues)}, {'eyesize': v}]

def analyzePopulation(population):
    
    sumgendermale = 0
    sumgenderfemale = 0
    
    summale = 0
    sumfemale = 0
    
    sumsizesmall = 0
    sumsizelarge = 0
    
    sumhairshort = 0
    sumhairlong = 0
    
    sumshapeone = 0
    sumshapetwo = 0
    sumshapethree = 0
    
    sumeyesizelarge = 0
    sumeyesizesmall = 0
    
    sumsmall = 0
    summedium = 0
    sumlarge = 0
    
    sumsmalleyes = 0
    summediumeyes = 0
    sumlargeeyes = 0
    
    sumlonghair = 0
    summediumhair = 0
    sumshorthair = 0
    
    sumred = 0
    sumblue = 0
    sumgreen = 0
    sumredblue = 0
    sumredgreen = 0
    sumgreenblue = 0
    
    
    for m in population:
        if m.getGender() == 0:
            summale += 1
            sumgendermale += 1
            sumgenderfemale += 1
        else:
            sumfemale += 1
            sumgenderfemale += 2
    
        if m.getChromosomes()[0][0]['size'] == 0:
            sumsizesmall += 1
        else:
            sumsizelarge += 1
        if m.getChromosomes()[1][0]['size'] == 0:
            sumsizesmall += 1
        else:
            sumsizelarge += 1
    
        if m.getChromosomes()[0][1]['hair'] == 0:
            sumhairshort += 1
        else:
            sumhairlong += 1
        if m.getChromosomes()[1][1]['hair'] == 0:
            sumhairshort += 1
        else:
            sumhairlong += 1
    
        if m.getChromosomes()[0][2]['color'] == 1:
            sumshapeone += 1
        elif m.getChromosomes()[0][2]['color'] == 3:
            sumshapetwo += 1
        else:
            sumshapethree += 1
        if m.getChromosomes()[1][2]['color'] == 1:
            sumshapeone += 1
        elif m.getChromosomes()[1][2]['color'] == 2:
            sumshapetwo += 1
        else:
            sumshapethree += 1
    
        if m.getChromosomes()[0][3]['eyesize'] == 0:
            sumeyesizesmall += 1
        else:
            sumeyesizelarge += 1
        if m.getChromosomes()[1][3]['eyesize'] == 0:
            sumeyesizesmall += 1
        else:
            sumeyesizelarge += 1
    
        if int((m.getChromosomes()[0][0]['size'] + m.getChromosomes()[1][0]['size']) / 2) == 0:
            sumsmall += 1
        elif int((m.getChromosomes()[0][0]['size'] + m.getChromosomes()[1][0]['size']) / 2) == 1:
            summedium += 1
        else:
            sumlarge += 1
    
        if int((m.getChromosomes()[0][3]['eyesize'] + m.getChromosomes()[1][3]['eyesize']) / 2) == 0:
            sumsmalleyes += 1
        elif int((m.getChromosomes()[0][3]['eyesize'] + m.getChromosomes()[1][3]['eyesize']) / 2) == 1:
            summediumeyes += 1
        else:
            sumlargeeyes += 1
        
        if m.getChromosomes()[0][1]['hair'] == 2 or m.getChromosomes()[1][1]['hair'] == 2:
            sumlonghair += 1
        else:
            sumshorthair += 1
        
        if m.getColor() == 'red':
            sumred += 1
        elif m.getColor() == 'green':
            sumgreen += 1
        elif m.getColor() == 'blue':
            sumblue += 1
        elif m.getColor() == 'redgreen':
            sumredgreen += 1
        elif m.getColor() == 'greenblue':
            sumgreenblue += 1
        elif m.getColor() == 'redblue':
            sumredblue += 1
    
    return {
        'Size of Population': len(population),
        'Sum Y Allele': sumgendermale,
        'Sum X Allele': sumgenderfemale,
        'Size Small Allele': sumsizesmall,
        'Size Large Allele': sumsizelarge,
        'Short Hair Allele': sumhairshort,
        'Long Hair Allele': sumhairlong,
        'Red Color Allele': sumshapeone,
        'Green Color Allele': sumshapetwo,
        'Blue Color Allele': sumshapethree,
        'Small Eye Allele': sumeyesizesmall,
        'Large Eye Allele': sumeyesizelarge,
        'Males': summale,
        'Females': sumfemale,
        'Small Puffles': sumsmall,
        'Medium Puffles': summedium,
        'Large Puffles': sumlarge,
        'Small Eyes': sumsmalleyes,
        'Medium Eyes': summediumeyes,
        'Large Eyes': sumlargeeyes,
        'Long Hair': sumlonghair,
        'Short Hair': sumshorthair,
        'Red Puffles': sumred,
        'Green Puffles': sumgreen,
        'Blue Puffles': sumblue,
        'RedGreen Puffles': sumredgreen,
        'GreenBlue Puffles': sumgreenblue,
        'RedBlue Puffles': sumredblue
    }
    
    #print("SIZE OF POPULATION:        " + str(len(population)))
    #print("Sum male allele:           " + str(sumgendermale))
    #print("Sum female allele:         " + str(sumgenderfemale))
    #print("Sum size small allele:     " + str(sumsizesmall))
    #print("Sum size large allele:     " + str(sumsizelarge))
    #print("Sum hair short allele:     " + str(sumhairshort))
    #print("Sum hair long allele:      " + str(sumhairlong))
    #print("Sum shape one allele:      " + str(sumshapeone))
    #print("Sum shape two allele:      " + str(sumshapetwo))
    #print("Sum shape three allele:    " + str(sumshapethree))
    #print("Sum eyesize small allele:  " + str(sumeyesizesmall))
    #print("Sum eyesize large allele:  " + str(sumeyesizelarge))
    #print("Sum male:                  " + str(summale))
    #print("Sum female:                " + str(sumfemale))
    #print("Sum small:                 " + str(sumsmall))
    #print("Sum medium:                " + str(summedium))
    #print("Sum large:                 " + str(sumlarge))
    #print("Sum small eyes:            " + str(sumsmalleyes))
    #print("Sum medium eyes:           " + str(summediumeyes))
    #print("Sum large eyes:            " + str(sumlargeeyes))

population = []
popsize = 10000
for i in range(popsize):
    #father chromosome is second, that's why it's not fixed to 1
    population.append(Member(makeRandomChromosome(), makeRandomChromosome(), random.randint(0, 1)))


#print("Makeup of generation 0: ")
#analyzePopulation(population);



generations = [population]
alldata = [analyzePopulation(population)]
#now, populations are initialized. Step through x generations
for x in range(50):
    newpop = []

    moms, dads = [], []
    for m in generations[x]:
        if m.getGender() == 0:
            dads.append(m)
        else:
            moms.append(m)
    #do da shuffle
    random.shuffle(moms)
    random.shuffle(dads)
    
    for i in range(min(len(moms), len(dads))):
        #Make a random number of babbies if mom accepts dad. 0.5 for large/small eyes, 0.8 for medium eyes
        #Causes stabilizing selection
        randval = random.randint(0, 9)/10
        mom = moms[i]
        dad = dads[i]
        #HERE IS WHERE YOU DO SEXUAL SELECTION
        if (dad.getEyeSize() == 1 and randval < 0.8):
            for i in range(random.randint(1, 6)):
                newpop.append(mom.makeBabby(dad))
        elif (randval < 0.5):
            for i in range(random.randint(1, 6)):
                newpop.append(mom.makeBabby(dad))
    if (len(newpop) == 0):
        print("Puffles have died out. Such is life. Diagnostics: generation is currently " + str(x+1))
        exit(1)
    
    #HERE IS WHERE YOU DO OTHER SELECTION
    #RED, REDGREEN, puffles are easily visible to penguins. They are eaten sometimes.
    #After 10 generations, penguins attack. goddammit penguins
    for i in reversed(range(len(newpop))):#PENGUINS ARE PREDATORS ONLY AFTER 10 GENERATIONS
        if x > 9 and ((newpop[i].getColor() == 'red' or newpop[i].getColor() == 'redgreen') and random.randint(0, 10) == 0):
            del newpop[i]
    
    #After 25 generations, the environment gets colder. Small or short-haired puffles have a higher chance of death
    #Note: how do penguins have nuclear weapons/wars???
    for i in reversed(range(len(newpop))):
        #small = 0 point, medium = 2 points, large = 4 points
        #short hair = 0 point, long hair = 2 points
        score = newpop[i].getSize() + newpop[i].getHairLength()
        if (score < random.randint(1, 5) and random.randint(0, 4) == 0):
            del newpop[i]
    
    
    generations.append(newpop)
    alldata.append(analyzePopulation(newpop))

    #print("Makeup of generation " + str((x+1)) + ": ")
    #analyzePopulation(generations[x+1])
    print("On generation" + str(x+1) + " of size " + str(len(newpop)))

#Write data to csv
with open('results.csv', 'w') as outfile:
    writer = csv.DictWriter(outfile, alldata[0].keys())
    writer.writeheader()
    writer.writerows(alldata)
