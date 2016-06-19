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
import gc
# generate the graph! 
N = 2000
l = []
for i in range(150,N):
	s = str(i)+".txt"
	a = tm.time()
	g = lv.louvaininpy()
	g.createGraph(s)
	b = tm.time()
	l.append(b-a)
	gc.collect()


print len(l)

"""

f = plt.figure()

ax = f.add_subplot(111)

for i in range(150,N):
	 ax.annotate('(%s)' % i,xy=(i,l[i-150]),textcoords='data')
"""
plt.plot(range(150,N),l,"ro")
#plt.legend( loc='upper left', numpoints = 1 )
plt.ylabel("Time")
plt.xlabel("N")
plt.show()




