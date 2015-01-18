import random
import math


def objective(chromosome, target):
	# Returns the fitness score for the given chromosome
	score = 0

	for i in range(0, len(chromosome)):
		score += math.pow(chromosome[i] - target[i], 2)
	
	return score	


def crossover(chromosome1, chromosome2):
	# Performs crossover on the pair of chromosomes across middle
	x = len(chromosome1) / 2

	for i in range(x, len(chromosome1)):
		chromosome1[i], chromosome2[i] = chromosome2[i], chromosome1[i]

	return chromosome1, chromosome2


def mutate(chromosome, probability):
	# Performs mutation on a given chromosome with certain probability
	dice = random.uniform(0,1)
	idx = random.choice(chromosome)
	new_value = random.randint(0,10)

	if dice < probability:
		chromosome[idx] = new_value

	return chromosome



def create_population(size, length):
	population = []
	for i in range(0, size):
		population.append([])
		for j in range(0, length):
			population[i].append(random.randint(0, 10))
	
	return population



def sort_by_fitness(population, target_value):
	# Sorts a population of chromosomes by their fitness score
	fitness = 0

	for i in range(0, size):
		for j in range(0, length):
			objective(population, target_value)




print

# Unit tests for score
print "Unit tests for score"
print objective([1,2,3,4,5,6,7,8], [1,2,3,4,5,6,7,8]) # should be zero
print objective([1,2,4,4,5,6,7,8], [1,2,3,4,5,6,7,8]) # should be non-zero
print

# Unit tests for crossover
print "Unit tests for crossover"
print crossover([0,1,2,3,4,5,6,7,8,9], [9,8,7,6,5,4,3,2,1,0])
print 

# Unit tests for mutate
print "Unit tests for mutate"
print mutate([0,1,2,3,4,5,6,7,8,9], 0.1)
print






print create_population(10, 3)

#Unit tests for sort_by_fitness
print "Unit tests for sort_by_fitness"
print sort_by_fitness(create_population(10, 3), )


