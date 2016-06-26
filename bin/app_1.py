import web
import louvaininpy as l
import jsoninpy
import spliterinpy as spl
import webbrowser
import sys

urls = (
  '/', 'index',
  '/home', 'index',
  '/userdisplay','userdisplay',
  '/rscreen','rscreen',
  '/root','rootsonscreen',
  '/anode','anodes',
  '/matrx','nodematrix',
  '/node','nodesonscreen' # Error class not yet here
  )

app = web.application(urls, globals())
render = web.template.render('templates/')

class nodematrix:
    def GET(self):
        #print  "Displaying roots"
        url = "./templates/themat.html"
        new=2
        a=[[12,13,14],[16,17,18],[160,170,180]]
        b= 3
        return render.themat(a,b)

class anodes:
    def GET(self):
        #print  "Displaying roots"
        url = "./templates/fullgraph.html"
        new=2
        webbrowser.open(url,new=new)
        return render.rscreen()

class rootsonscreen:
    def GET(self):
        #print  "Displaying roots"
        url = "./templates/tmp.html"
        new=2
        webbrowser.open(url,new=new)
        return render.rscreen()

class nodesonscreen:
    def GET(self):
        #print  "Displaying nodes"
        url = "./templates/nodes.html"
        new=3
        webbrowser.open(url,new=new)
        return render.rscreen()

class index:
    def GET(self):
        #print  "Home called"
        return render.index()

    def POST(self):
        try: #User login can be done using the data base try it later
            form = web.input(uname="user", pword="password")
            #print  form.uname
            #print  form.pword

            if form.uname == "admin" and form.pword == "admin":
                raise web.seeother("/userdisplay")
            else:
                raise
        except:
            return render.error("Login error")

class userdisplay:
    def GET(self):
        greeting = ""
        #print  "In Here"
        return render.home()
    
    def POST(self):
        try:
            form = web.input(name="Nobody", greet="Hello")
            #print  form.greet
            fn = form.myfile
            x = web.input(myfile={})
            #print  x['keyfile']
            #print  x['myfile'],type(x['myfile'])
            fila = 0
            if x['keyfile'] != "":
                #print  "Key was inserted"
                rbl={}
                vsp = x['keyfile']
                ##print  x['keyfile'].value
                rkey=vsp.split("\n")
                #print  rkey
                if len(rkey[-1]) == 1:
                    del rkey[-1]
                for line in rkey:
                    rc=line.split(' ',1)
                    #print  rc
                    rbl[int(rc[0])] = rc[1]
                #print  rbl
                fila=1
            else:
                print  ""

            c = x['myfile'].value
            #print  "Split",len(c.split("\n")[0])
            #print  x['myfile'].file
            #print  type(x['myfile'].file)
            #print  type(x['myfile'].file.read())
            g = l.louvaininpy()
            if len(c.split("\n")[0]) != 3:
                g.sCreateWeightedGraph(x['myfile'].value)
            else:
                g.sCreateGraph(x['myfile'].value)   

            partition, q= g.louvain()
            #print  partition,q   

            if fila == 1:
                v = [rbl[g.relabel[i]] for i in g.relabel]
                g.relabel = dict(zip(g.relabel.keys(),v))


            #roots  

            r,nn = spl.splitroot(g,partition)
            r.jsonDump("rjson.json")
            nn.jsonDump("alljson.json")
            #print  "JSON Created"




#            url = "./templates/tmp.html"
 #           new=2
  #          webbrowser.open(url,new=new)
   #         url = "./templates/nodes.html"
    #        new=3
     #       webbrowser.open(url,new=new)
      #      c = rscreen()
       #     c.GET()
            return render.rscreen()
        except:
            #print ("Unexpected error:", sys.exc_info()[0])
            return render.error("Error In userdisplay")


class rscreen:
    def GET(self):
        greeting = ""
        #print  "In Heress"
        return render.rscreen()
    
    def POST(self):
        try:
            #print  "Heyasdf"
            return render.userdisplay()
        except:
            return render.error("HAHA")

if __name__ == "__main__":
    app.run()
