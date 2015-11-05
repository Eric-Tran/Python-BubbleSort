import random
random_list = random.sample(xrange(1,10000),100)
print random_list

def bubblesort(a):
	count = 0
	while count < len(random_list):
		for x in range(0, len(random_list)-1):
			if random_list[x] > random_list[x+1]:
				random_list[x], random_list[x+1] = random_list[x+1], random_list[x]
		print random_list
		count += 1

bubblesort(random_list)


