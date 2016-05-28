
class FileLabel:
	yes=0
	rlbl = {}
	def __inti__(self):
		print "Initiated"
		self.yes=0

	def openkey(self, filename):
		print "Hey I cam here"
		d = {}
		key=filename.split("\n")
		for line in key:
			c=line.split(' ',1)
			d[int(c[0])] = c[1].replace("\n","")
		print d
		self.rlbl = d
		self.yes = 1
		print "Bye i just left"
"""
k = FileLabel()
k.__inti__()
c = "0 A\n1 B\n2 C"
k.openkey(c)
"""


