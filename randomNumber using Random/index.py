import random

num = 100*(random.randint(1,6))/2
print("The random number generated is:", num)

rand_uniform = int(1000*(random.uniform(1.5, 9.5)))
print("The random number generated using uniform is:", rand_uniform)