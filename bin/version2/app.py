import web
import louvaininpy as l
import jsoninpy
import spliterinpy as spl
import webbrowser

urls = (
  '/', 'index',
  '/home', 'index',
  '/userdisplay','userdisplay',
  '/rscreen','rscreen',
  '/root','rootsonscreen',
  '/node','nodesonscreen' # Error class not yet here
  )

app = web.application(urls, globals())
render = web.template.render('templates/')

class rootsonscreen:
    def GET(self):
        print "Displaying roots"
        url = "./templates/tmp.html"
        new=2
        webbrowser.open(url,new=new)
        return render.rscreen()

class nodesonscreen:
    def GET(self):
        print "Displaying nodes"
        url = "./templates/nodes.html"
        new=3
        webbrowser.open(url,new=new)
        return render.rscreen()

class index:
    def GET(self):
        print "Home called"
        return render.index()

    def POST(self):
        try: #User login can be done using the data base try it later
            form = web.input(uname="user", pword="password")
            print form.uname
            print form.pword

            if form.uname == "admin" and form.pword == "admin":
                raise web.seeother("/userdisplay")
            else:
                raise
        except:
            return render.error("Login error")

class userdisplay:
    def GET(self):
        greeting = ""
        print "In Here"
        return render.home()
    
    def POST(self):
        try:
            form = web.input(name="Nobody", greet="Hello")
            print form.greet
            fn = form.myfile
            x = web.input(myfile={})
            print x['myfile'],type(x['myfile'])
            c = x['myfile'].value
            print "Split",len(c.split("\n")[0])
            print x['myfile'].file
            print type(x['myfile'].file)
            print type(x['myfile'].file.read())
            g = l.louvaininpy()
            if len(c.split("\n")[0]) != 3:
                g.sCreateWeightedGraph(x['myfile'].value)
            else:
                g.sCreateGraph(x['myfile'].value)   

            partition, q= g.louvain()
            print partition,q   

            #roots  

            r,nn = spl.splitroot(g,partition)
            r.jsonDump("rjson.json")
            nn.jsonDump("alljson.json")
            print "JSON Created"




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
            return render.error("Error In userdisplay")

class rscreen:
    def GET(self):
        greeting = ""
        print "In Heress"
        return render.rscreen()
    
    def POST(self):
        try:
            print "Heyasdf"
            return render.userdisplay()
        except:
            return render.error("HAHA")

if __name__ == "__main__":
    app.run()
