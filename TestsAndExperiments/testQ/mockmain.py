###################################################
#mock code to test modular graph generator 

###################################################

#####importing functions

#the generator requires networkx package to be installed
import networkx as nx
#importing modular graph generator by Sah2014
import random_modular_generator_variable_modules as rmg
#importing1seence generator by Sah2014
import sequence_generator as sg
from random import randint as ran
################################################################################################

# Enter the network size(N), average network degree (d), total modules in the network (m), and modularity (Q)
N=150
d=10
m=10
Q= 0.4

# specify the degree distribution of the graph. In it's current format the code can generate
# four well known degree distribution found in biological networks - scalefree, geometric, poisson and regular distribution
sfunction = sg.poisson_sequence

# specify the distribution of module size. The distribution can be scalefree, geometric, poisson and regular distribution (or any aribtrary sequence)
#in it's simplest form speicify module size tp be regular which implies that all modules are of equal size
modfunction = sg.regular_sequence

# generate the graph! 

print "Generating a simple poisson random modular graph with modularity(Q)= " + str(Q)
print "Graph has " + str(N) + " nodes, " +str(m)+ " modules, and a network mean degree of " + str(d)
print "Generating graph....." 
Q=0.1
for i in range(1,10):
	G = rmg.generate_modular_networks(N, sfunction, modfunction, Q, m, d)
	print i," is being loaded"
	k =  G.edges()
	f = open(str(i)+".txt","w")
	for j in k:
		s = str(j[0])+" "+str(j[1])+"\n"
		f.write(s)
	f.close()
	Q=Q+0.1


