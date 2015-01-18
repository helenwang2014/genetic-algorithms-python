import random
import math
import operator

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


def create_table_by_fitness(population, target_value):

	ranking = []

	for i in range(0, len(population)):
		ranking.append([])
		ranking[i].append(objective(population[i], target_value))
		ranking[i].append(population[i])
	
	return ranking


def sort_table(table, col):
	# Sorts a population of chromosomes by their fitness score column
	
	return sorted(table, key=operator.itemgetter(col))


print

# Unit tests for score
print "Unit tests for score"
print objective([1,2,3,4,5,6], [1,2,3,4,5,6]) # should be zero
print objective([1,2,4,4,5,6], [1,2,3,4,5,6]) # should be non-zero
print

# Unit tests for crossover
print "Unit tests for crossover"
print crossover([0,1,2,3,4,5], [9,8,7,6,5,4])
print 

# Unit tests for mutate
print "Unit tests for mutate"
print mutate([0,1,2,3,4,5], 0.5)
print


population1 = create_population(10, 6)
print population1
print 
print "Population table with score"
ranking1 = create_table_by_fitness(population1, [1,2,3,4,5,6])
print ranking1
print 
#Unit tests for sort_by_fitness
print "Unit tests for sort_by_fitness"
print sort_table(ranking1, 0)


