import random
def flipCoin():
	prob = float(input("Probability of landing an H"))
	while(input("Next")=="n"):
		if (random.random() <= prob):
			print("H")
		else:
			print("T")
flipCoin()