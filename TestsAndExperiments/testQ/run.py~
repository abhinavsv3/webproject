###################################################
#mock code to test modular graph generator 

###################################################

#####importing functions

#the generator requires networkx package to be installed
import networkx as nx
#importing modular graph generator by Sah2014
import random_modular_generator_variable_modules as rmg
#importing sequence generator by Sah2014
import sequence_generator as sg
import louvaininpy as lv
################################################################################################
import time as tm
import matplotlib.pyplot as plt
# generate the graph! 
N = 2000
l = []
for i in range(1,8):
	s = str(i)+".txt"
	a = tm.time()
	g = lv.louvaininpy()
	g.createGraph(s)
	b = tm.time()
	l.append(b-a)

print len(l)
plt.plot(range(1,8),l,"ro")
plt.ylabel("Time")
plt.xlabel("N")
plt.show()




