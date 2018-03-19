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

from random import gauss
import time
import multiprocessing 


class Plane:
	def __init__(self):
		self.orientation = 0
		self.max_angle = 270

	def __str__(self):
		return "Current orientation: {:+f}\r".format(self.orientation)

	def fly(self):
		while True:
			self.check_crash()
			yield self.orientation

	def check_crash(self):
		if abs(self.orientation) > self.max_angle:
			print("Ops! Plane has crashed")
			exit()


class Simulator:
	def __init__(self, plane):
		self.plane = plane

	def start_simulation(self):
		print("Starting Flight Simulation (press 'q' to exit)")
		while self.plane.fly():
			print(self.plane,end='')
			self.turbulations()
			self.apply_tilt_correction()
			time.sleep(1)

	def apply_tilt_correction(self):
		if self.plane.orientation < 0:
			self.plane.orientation += 20
		elif self.plane.orientation > 0:
			self.plane.orientation -= 20

	def turbulations(self):
		new_orientation = gauss(0,20)
		self.plane.orientation = new_orientation

	def check_user_input(self, another_thread):
	   	while True:
	   		if input() == 'q':
	   			another_thread.terminate()
	   			print("Ending simulation")
	   			exit()

if __name__ == '__main__':
	simulation = Simulator(Plane())
	another_thread = multiprocessing.Process(target=simulation.start_simulation)
	another_thread.start()
	simulation.check_user_input(another_thread)
		