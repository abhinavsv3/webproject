class Matrix:
       def sCreateMatrix(self, file):
        print "Loading the graph"
        m=[] # original graph
        f = file.split("\n")
        for line in f:
            print line

            m.append(map(int, line.split()))
        print m
        if len(m[-1]) != len(m[-2]):
            del m[-1]
        mt = [[row[i] for row in m] for i in range(3)]
        print "M", m 
        print "Mt", mt
        x = list(set(mt[0]).union(mt[2])) 
        print "List of nodes",x
"""
        num = len(x)
        print "Number of nodes",num
        edges = zip(zip(mt[0],mt[2]),mt[1])
        print edges
        print len(edges)
        y = range(0,len(x))
        k =zip(x,y)
        mat = [ [0 for i in range(num)] for j in range(num)]
        mat[0][0] = 1
        print [ mat[i[0][0]][i[0][1]] for i in edges]
   """     
        #non repeating list of nodes
        #renumbering 
    #Formatof number representation in the matrix:
    #"start weight destination"
        y = range(0,len(x))
        self.totnodes = len(x)
        d = dict(zip(x,y))
        self.relabel = dict(zip(y,x))
        mat = [ [0 for i in range(num)] for j in range(num)]
        print [ mat[i[0][0]][i[0][1]] for i in edges]
        print "Loading Complete, Rearraging"
        st = mt[0] = [d[i] for i in mt[0]]
        ds = mt[2] = [d[i] for i in mt[2]]
        wt = mt[1]
        self.start = st
        self.dest = ds
        self.wgt = wt
        self.length = len(st)
        self.edges = zip(zip(st,ds),wt)
        self.nodes = y
        self.initialg()"""

        print "Initi Success"
a = "1 2 3\n2 3 4\n1 2 3"
print a

m = Matrix()
m.sCreateMatrix(a)