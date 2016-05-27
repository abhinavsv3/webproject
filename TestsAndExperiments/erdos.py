import igraph as ig

g= ig.Graph()
sol = g.Erdos_Renyi(1000, 1)
e = open("erdos_renyi.txt","w+")
for v in sol.get_edgelist():
	e.write(str(v[0])+" "+str(v[1])+"\n")
e.close()
