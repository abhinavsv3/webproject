import igraph as ig

g= ig.Graph()
sol = [g.Famous("bull"),
		g.Famous("Zachary"),
		g.Famous("Chvatal"),
		g.Famous("Coxeter"),
		g.Famous("Cubical"),
		g.Famous("Diamond"),
		g.Famous("Dodecahedral"),
		g.Famous("Folkman"),
		g.Famous("Franklin"),
		g.Famous("Frucht"),
		g.Famous("Grotzsch"),g.Famous("Heawood"),g.Famous("Herschel"),
		g.Famous("House"),
		g.Famous("HouseX"),
		g.Famous("Levi"),
		g.Famous("McGee"),
		g.Famous("Meredith"),g.Famous("Noperfectmatching"),g.Famous("Nonline"),g.Famous("Octahedral"),g.Famous("Petersen"),g.Famous("Tutte"),
		g.Famous("Robertson"),g.Famous("Smallestcyclicgroup"),g.Famous("Tetrahedral"),g.Famous("Thomassen"),g.Famous("Zachary"),
		g.Famous("Uniquely3colorable"),g.Famous("Walther")
		]
l = 0
txt = ".txt"
print str(l)+txt
for i in sol:
	e = open(str(l)+txt,"w+")
	for v in i.get_edgelist():
		e.write(str(v[0])+" "+str(v[1])+"\n")
	l = l+1
	e.close()
