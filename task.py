###Flight simulator. 
#Write a code in python that simulates the tilt correction of the plane (angle between plane wings and earth). 
##The program should:
# - print out current orientation
# - applied tilt correction
# - run in infinite loop
# - until user breaks the loop
#Assume that plane orientation in every new simulation step is random angle with gaussian distribution (the planes is experiencing "turbulations"). 
#With every simulation step the orentation should be corrected, applied and printed out.
#The level of realism in simulation is of your choice, but more sophisticated solutions are better.
#If you can thing of any other features, you can add them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#The whole repository MUST be a fork from https://github.com/mwmajew/kol1_gr2
#Good Luck

import random
import time

class Flight(object):
	"""docstring for Plane"""
	def __init__(self, name):
		self.name = name
		self.mu = 0
		self.sigma = 0.1 # mean and standard deviation
		self.orient = 0


	def simulate(self):
		while True:
			self.new_orientation()
			self.print_orient("Current")
			self.correct()
			self.print_orient("Corrected one")
			time.sleep(1)


	def correct(self):
		if self.orient < 0:
			self.orient += 20
		elif self.orient > 0:
			self.orient -= 20

	def new_orientation(self):
		self.orient = random.gauss(self.mu, self.sigma) * 180

	def print_orient(self, s):
		print(str(s)+" orientation: {}".format(self.orient))




plane = Flight("Airplane")
plane.simulate()