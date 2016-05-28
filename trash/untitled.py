import web
import louvaininpy as l
import jsoninpy
import spliterinpy as spl
import webbrowser

urls = (
  '/', 'index', '/upload','Upload','/jsons'
)

app = web.application(urls, globals())
render = web.template.render('templates/')

class index:
    def GET(self):
        greeting = ""
        print "In Here"
        return render.index()
    
    def POST(self):
        try:
            form = web.input(name="Nobody", greet="Hello")
            print form.greet
            fn = form.myfile
            x = web.input(myfile={})
            print x['myfile'],type(x['myfile'])
            print x['myfile'].value
            print x['myfile'].file
            print type(x['myfile'].file)
            print type(x['myfile'].file.read())
            g = l.louvaininpy()
            if form.weighted == "Yep":
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




            url = "./templates/tmp.html"
            new=2
            webbrowser.open(url,new=new)
            url = "./templates/nodes.html"
            new=3
            webbrowser.open(url,new=new)
            return render.index()
        except:
            return render.error("Error in Reading the Input")

    def showRoot(self):
        print "Here I come"
    	

if __name__ == "__main__":
    app.run()
