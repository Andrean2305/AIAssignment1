# Python3 implementation of the above approach
from random import randint

INT_MAX = 69696969696969
# Number of cities in TSP
V = 7

# Names of the cities
GENES = "ABCDEFG"

# Starting Node Value
START = 0

# Initial population size for the algorithm
POP_SIZE = 1000

# Structure of a GNOME
# defines the path traversed
# by the salesman while the fitness value
# of the path is stored in an integer

FITNESS_NOW = INT_MAX
RUTE = "ANJAY"

class individual:
	def __init__(self) -> None:
		self.gnome = ""
		self.fitness = 0

	def __lt__(self, other):
		return self.fitness < other.fitness

	def __gt__(self, other):
		return self.fitness > other.fitness


# Function to return a random number
# from start and end
def rand_num(start, end):
	return randint(start, end-1)


# Function to check if the character
# has already occurred in the string
def repeat(s, ch):
	for i in range(len(s)):
		if s[i] == ch:
			return True

	return False


# Function to return a mutated GNOME
# Mutated GNOME is a string
# with a random interchange
# of two genes to create variation in species
def mutatedGene(gnome):
	gnome = list(gnome)
	while True:
		r = rand_num(1, V)
		r1 = rand_num(1, V)
		if r1 != r:
			temp = gnome[r]
			gnome[r] = gnome[r1]
			gnome[r1] = temp
			break
	return ''.join(gnome)


# Function to return a valid GNOME string
# required to create the population
def create_gnome():
	gnome = "0"
	while True:
		if len(gnome) == V:
			gnome += gnome[0]
			break

		temp = rand_num(1, V)
		if not repeat(gnome, chr(temp + 48)):
			gnome += chr(temp + 48)

	return gnome


# Function to return the fitness value of a gnome.
# The fitness value is the path length
# of the path represented by the GNOME.
def cal_fitness(gnome):
	mp = [
    [0, 12, 10, INT_MAX, INT_MAX, INT_MAX, 12],
    [12, 0, 8, 12, INT_MAX, INT_MAX, INT_MAX],
    [10, 8, 0, 11, 3, INT_MAX, 9],
    [INT_MAX, 12, 11, 0, 11, 10, INT_MAX],
    [INT_MAX, INT_MAX, 3, 11, 0, 6, 7],
    [INT_MAX, INT_MAX, INT_MAX, 10, 6, 0, 9],
    [12, INT_MAX, 9, INT_MAX, 7, 9, 0]
    ]

	f = 0
	for i in range(len(gnome) - 1):
		if mp[ord(gnome[i]) - 48][ord(gnome[i + 1]) - 48] == INT_MAX:
			return INT_MAX
		f += mp[ord(gnome[i]) - 48][ord(gnome[i + 1]) - 48]

	return f


# Function to return the updated value
# of the cooling element.
def cooldown(temp):
	return (90 * temp) / 100


# Comparator for GNOME struct.
# def lessthan(individual t1,
#			 individual t2)
# :
#	 return t1.fitness < t2.fitness


# Utility function for TSP problem.
def TSPUtil(mp):
    global FITNESS_NOW,RUTE
    # Generation Number
    gen = 1
    # Number of Gene Iterations
    gen_thres = 5

    population = []
    temp = individual()

    # Populating the GNOME pool.
    for i in range(POP_SIZE):
        temp.gnome = create_gnome()
        temp.fitness = cal_fitness(temp.gnome)
        population.append(temp)

    print("\nInitial population: \nGNOME\tFITNESS VALUE\n")
    for i in range(POP_SIZE):
        print(population[i].gnome, population[i].fitness)
        if(population[i].fitness < FITNESS_NOW):
            FITNESS_NOW = population[i].fitness
            RUTE = population[i].gnome
            print("UHUY DAPET YANG CEPET NIH GES")

    print()

    found = False
    temperature = 10000

    # Iteration to perform
    # population crossing and gene mutation.
    while temperature > 1000 and gen <= gen_thres:
        population.sort()
        print("\nCurrent temp: ", temperature)
        new_population = []

        for i in range(POP_SIZE):
            p1 = population[i]

            while True:
                new_g = mutatedGene(p1.gnome)
                new_gnome = individual()
                new_gnome.gnome = new_g
                new_gnome.fitness = cal_fitness(new_gnome.gnome)

                if new_gnome.fitness <= population[i].fitness:
                    new_population.append(new_gnome)
                    break

                else:

                    # Accepting the rejected children at
                    # a possible probability above threshold.
                    prob = pow(
                        2.7,
                        -1
                        * (
                            (float)(new_gnome.fitness - population[i].fitness)
                            / temperature
                        ),
                    )
                    if prob > 0.5:
                        new_population.append(new_gnome)
                        break

        temperature = cooldown(temperature)
        population = new_population
        print("Generation", gen)
        print("GNOME\tFITNESS VALUE")

        for i in range(POP_SIZE):
            print(population[i].gnome, population[i].fitness)
            if(population[i].fitness < FITNESS_NOW):
                FITNESS_NOW = population[i].fitness
                RUTE = population[i].gnome
                print("UHUY DAPET YANG CEPET NIH GES")
        gen += 1



if __name__ == "__main__":

	mp = [
    [0, 12, 10, INT_MAX, INT_MAX, INT_MAX, 12],
    [12, 0, 8, 12, INT_MAX, INT_MAX, INT_MAX],
    [10, 8, 0, 11, 3, INT_MAX, 9],
    [INT_MAX, 12, 11, 0, 11, 10, INT_MAX],
    [INT_MAX, INT_MAX, 3, 11, 0, 6, 7],
    [INT_MAX, INT_MAX, INT_MAX, 10, 6, 0, 9],
    [12, INT_MAX, 9, INT_MAX, 7, 9, 0]
    ]

	TSPUtil(mp)
# Input string
input_str = RUTE

# Mapping of digits to letters
digit_to_letter = {
    '0': 'A',
    '1': 'B',
    '2': 'C',
    '3': 'D',
    '4': 'E',
    '5': 'F',
    '6': 'G',
    '7': 'H',  # Adding '7' as an example, but you can adjust the mapping as needed
}

# Transform the input string into the desired string
RUTE = ''.join([digit_to_letter[digit] for digit in input_str])

print("--------------------------")
print("FOR NOW THE PROGRAM FIND: " + RUTE + " AS THE FASTEST ROUTES, WITH THE VALUE/DISTANCE OF: " + str(FITNESS_NOW))

print("BY THE WAY GUYS, THE POP_SIZE IS 1000, BECAUSE KNOWING THE FACTS THAT WE GOT 7 CITIES (JUST TO BE SURE GOT THE FASTEST)")
print("IF SOMEHOW THE PROGRAM FITNESS SCORE GET 69696969696969 AT LAST PLS RUN AGAIN (BUT I DOUBT WITH POP_SIZE 1000 IT STILL GOT INT_MAX)")
print("--------------------------")
#SOURCE CODE GEEKSFORGEEKS. MOD BY A.H.
