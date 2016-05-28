class Matrix:
    def MatrixCreateGraph(self,file):
        m = []
        print "Loading the graph"
        f = file.split("\n")
        for line in f:
            print line
            m.append(map(int, line.split()))
        print "m",m
        if len(m[-1]) != len(m[-2]):
            del m[-1]
        mt = [[row[i] for row in m] for i in range(2)]
        x = list(set(mt[0]).union(mt[1]))
        print "Loading Complete, Rearraging"
        y = range(0,len(x))
        self.totnodes = len(x)
        d = dict(zip(x,y))
        self.relabel = dict(zip(y,x))
        st = mt[0] = [d[i] for i in mt[0]]
        ds = mt[1] = [d[i] for i in mt[1]]
        #print "MT ", mt[1], len(mt[1])
        wt = [1 for i in range(0,len(mt[1]))]
        #print "Wt", wt
        self.start = st
        self.dest = ds
        self.wgt = wt
        self.length = len(st)
        self.edges = zip(zip(st,ds),wt)
        self.nodes = y
        self.initialg()
        print "2 coloumn graph created Successfully"