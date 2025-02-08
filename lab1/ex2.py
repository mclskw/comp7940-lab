# Write a function that prints all factors of the given parameter x
def print_factor(x):
	for i in range(x+1):
		if x%(i+1)==0:
			print (i+1)
