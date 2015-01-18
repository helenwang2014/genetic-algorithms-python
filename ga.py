import random
import math

def score(chromosome, target):
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


def sort_by_fitness(population):
	# Sorts a population of chromosomes by their fitness score
	pass

print

# Unit tests for score
print "Unit tests for score"
print score([1,2,3,4,5,6,7,8], [1,2,3,4,5,6,7,8]) # should be zero
print score([1,2,4,4,5,6,7,8], [1,2,3,4,5,6,7,8]) # should be non-zero
print

# Unit tests for crossover
print "Unit tests for crossover"
print crossover([0,1,2,3,4,5,6,7,8,9], [9,8,7,6,5,4,3,2,1,0])
print 

# Unit tests for mutate
print "Unit tests for mutate"
print mutate([0,1,2,3,4,5,6,7,8,9], 0.1)
print
