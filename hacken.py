import sys
		
class Vertex:
	def __init__(self, label):
		self.label = str(label)
		self.connections = []
		
class Graph:
	def __init__(self):
		self.V = {}
		self.E = {}
	def addVertex(self, label):
		self.V[str(label)] = {}
	def addEdge(self, label, v1, v2):
		v = [v1,v2]
		v.sort()
		v = [str(n) for n in v]
		self.E[label] = (v[0], v[1])
		self.V[v[0]][label] = v[1] 
	
class Hackenbush:
	def __init__(self):
		self.Field = Graph()
		self.Field.addVertex('0')
		self.blues = 0
		self.reds = 0
		self.nodes = 0
	def inPlay(self):
		return [e for e in self.Field.E]
	def allNodes(self):
		return [v for v in self.Field.V]
	def lastBlue(self):
		return "b" + str(self.blues)
	def lastRed(self):
		return "r" + str(self.reds)
	def lastNode(self):
		return self.nodes
	def addNode(self):
		self.nodes = self.nodes + 1
		self.Field.addVertex(self.nodes)
	def addBlue(self, v1=0, v2=0):
		self.blues = self.blues + 1
		index = self.lastBlue()
		self.Field.addEdge(index, str(v1), str(v2))
	def addRed(self, v1=0, v2=0):
		self.reds = self.reds + 1
		index = self.lastRed()
		self.Field.addEdge(index, str(v1), str(v2))
	def removeEdge(self, edge):
		for v in self.Field.V:
			if edge in self.Field.V[v]:
				self.Field.V[v].pop(edge)
		self.Field.E.pop(edge)
	def displayFromVertex(self, vertex):
		seen = set()
		seenE = set()
		last = ["0"]
		sys.stdout.write("|\n|")
		def recurse(next, level=0):
			seen.add(next)
			#print next + ":"+ str(self.Field.V[next])
			edges = self.Field.V[next] 
			for label in edges:
				
				v = edges[label]
				if v not in seen or label not in seenE:
					seen.add(v)
					seenE.add(label)
					if next != last[0]:
						print 
						sys.stdout.write("|")
						sys.stdout.write("               " * level + "---- " + label + " ---- " + v + " ")
					else:
						sys.stdout.write("---- " + label + " ---- " + v + " ")
					last[0] = v
					recurse(v, level+1)
				#if next == vertex:
				#	print 
				#	sys.stdout.write("|")
		recurse(vertex)
		print
		sys.stdout.write("|\n|")
		notseenE = set(self.Field.E).difference(seenE)
		for e in notseenE:
			self.removeEdge(e)
			
		print
		
	def display(self):
		self.displayFromVertex('0')
		#print self.Field.E
		#print self.Field.V
		
	def setup(self):
		print "Setup the playing field."
		entry = None
		while entry != "x":
			entry = raw_input("(n)ode or (b)lue edge or (r)ed edge? (d) to display. (x) to finish. ")
			if entry == 'n':
				self.addNode()
			elif entry == 'b' or entry == 'r':
				v1 = None
				v2 = None
				while v1 == None:
					print "1st node to connect to:"
					print self.allNodes()
					v1 = raw_input()
					if v1 not in self.allNodes():
						v1 = None
				while v2 == None:
					print "2nd node to connect to:"
					print self.allNodes()
					v2 = raw_input()
					if v2 not in self.allNodes():
						v2 = None
						
				if entry == 'b':
					self.addBlue(v1, v2)
				else:
					self.addRed(v1, v2)
				
				
				print
				self.display()
			elif entry == 'd':
				self.display()
			elif entry != 'x':
				entry = None
					
					
	def play(self, first='blue'):
		
		if self.inPlay() == []:
			print "Nothing in play."
			return
		last = None
		player = first
		print
		self.display()
		playerMoves = [v for v in self.inPlay() if v[0] == player[0]]
		
		while playerMoves != []:
			next = " "
			while next not in playerMoves:
				print player[0].upper() + player[1:] + "'s turn"
				print "Remove which edge? "
				print playerMoves
				next = raw_input()
			self.removeEdge(next)
			last = next

			if player == 'blue':
				player = 'red'
			else:
				player = 'blue'
			

			print
			self.display()
			
			playerMoves = [v for v in self.inPlay() if v[0] == player[0]]

		if last[0] == 'b':
			print "Blue wins!"
		else:
			print "Red wins!"
			
	
def main():
	test = Hackenbush()
	player = 'blue'
	if '-board1' in sys.argv:
		test.addNode()
		test.addBlue(0,1)
		test.addNode()
		test.addRed(1,2)
		test.addNode()
		test.addRed(3,2)
		test.addNode()
		test.addBlue(4,2)
		
		test.addNode()
		test.addRed(0, 5)
		test.addNode()
		test.addBlue(6,5)
	else:
		test.setup()
	if '-r' in sys.argv:
		player = 'red'

	test.play(player)
main()
	
