#rolling game
from random import randint

min , max = 1, 6

def roll():
	print randint(min ,max)


choice = raw_input("Do you want to roll? Y/N:")

while (choice in ('Y' , 'y')):
	roll()
	choice = raw_input("DO you want to roll again ? Y?N:")

print ("Thanks for rolling!!!!")
