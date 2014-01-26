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
		#v.sort()
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
		self.verbose = True
		self.debug = False
	def toggleVerbose(self, set=None):
		if set == None:
			self.verbose = not self.verbose
		elif set == True or set == False:
			self.verbose = set
	def toggleDebug(self, set=None):
		if set == None:
			self.debug = not self.debug
		elif set == True or set == False:
			self.debug = set
	def printVerbose(self, long, short):
		if self.verbose:
			print long
		elif short != None:
			print short
	def printDebug(self, *items):
		out = [str(item) for item in items]
		out = "".join(out)
		if self.debug:
			print out
	def inPlay(self):
		return [e for e in self.Field.E]
	def allNodes(self):
		nodes = [v for v in self.Field.V]
		nodes.sort()
		return nodes
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
	def removeVertex(self, v):
		connections = self.Field.V.pop(v)
		#print connections
		
		# Remove all edges connected to vertex
		for edge in connections:
			self.removeEdge(edge)

		# Find and remove all edges going to vertex (one-way)
		delete = set()
		for node in self.Field.V:
			edges = dict(self.Field.V[node])
			for edge in edges:
				if v in self.Field.V[node][edge]:
					self.Field.V[node].pop(edge)
					
		self.printDebug("Connections: ", self.Field.V)
	
	def displayFromVertex(self, vertex):
		seen = set()
		seenE = set()
		last = ["0"]
		sys.stdout.write("|\n|")
		def recurse(next, level=0):
			seen.add(next)
			#print next + ":"+ str(self.Field.V[next])
			edges = self.Field.V[next] 
			labels = [label for label in edges]
			labels.sort()
			#print labels
			for label in labels:
				v = edges[label]
				if v not in seen or label not in seenE and not (int(v) == 0 and level > 0):
					seen.add(v)
					seenE.add(label)
					if next != last[0]:
						print 
						sys.stdout.write("|")
						sys.stdout.write("             " * level)
						if level == 0:
							sys.stdout.write("____" + label + "____(" + v + ")") 
						else:
							sys.stdout.write("\___" + label + "____(" + v + ")") 
					else:
						sys.stdout.write("____" + label + "____(" + v + ")") 
					last[0] = v
					recurse(v, level+1)
		recurse(vertex)
		print
		sys.stdout.write("|\n|")
		notseenE = set(self.Field.E).difference(seenE)
		for e in notseenE:
			self.removeEdge(e)
			
		print
		self.printDebug("Nodes: ", self.Field.V)
		self.printDebug("Edges: ", self.Field.E)
		self.printDebug()
		
	def display(self):
		print
		self.displayFromVertex('0')
		print
		#print self.Field.E
		#print self.Field.V
		
	def setup(self):
		self.printVerbose("Setup the playing field.", "Setup.")
		entry = None
		while entry != "x":
			self.display()
			self.printVerbose("(n)ode or (b)lue edge or (r)ed edge? (d) to display. (p) to delete node. (x) to finish.", "(n)ode (b)lue (r)ed (d)isplay (p)op node (x) finish")
			entry = raw_input()
			if entry == 'n':
				self.addNode()
				self.printDebug(self.Field.V)
			elif entry == 'b' or entry == 'r':
				v1 = None
				v2 = None
				while v1 == None:
					self.printVerbose("1st node to connect to:", "1st node:")
					print self.allNodes()
					v1 = raw_input()
					if v1 not in self.allNodes():
						v1 = None
				while v2 == None:
					self.printVerbose("2nd node to connect to:", "2nd node:")
					print self.allNodes()
					v2 = raw_input()
					if v2 not in self.allNodes():
						v2 = None
						
				if entry == 'b':
					self.addBlue(v1, v2)
				else:
					self.addRed(v1, v2)
				
				print
				#self.display()
			elif entry == 'd':
				self.display()
			elif entry == 'p':
				v = None
				while v == None:
					print "Select a node."
					print [v for v in self.Field.V]
					v = raw_input()
					if v not in self.Field.V:
						v = None
				self.removeVertex(v)
			elif entry != 'x':
				entry = None
					
	def play(self, first='blue'):
		if self.inPlay() == []:
			print "Nothing in play."
			return
		last = None
		player = first
		playerMoves = [v for v in self.inPlay() if v[0] == player[0]]
		
		while playerMoves != []:
			self.display()
			next = " "
			while next not in playerMoves:
				self.printVerbose(player[0].upper() + player[1:] + "'s turn", None)
				self.printVerbose("Remove which edge?", "Remove:")
				print playerMoves
				next = raw_input()
			self.removeEdge(next)
			last = next

			if player == 'blue':
				player = 'red'
			else:
				player = 'blue'

			playerMoves = [v for v in self.inPlay() if v[0] == player[0]]
		print
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
		test.addRed(2,3)
		test.addNode()
		test.addBlue(2,4)
		test.addNode()
		test.addRed(0, 5)
		test.addNode()
		test.addBlue(5,6)
		test.addBlue(5,0)
		test.addRed(0,2)
	elif '-board2' in sys.argv:
		test.addNode()
		test.addRed(0,1)
		test.addNode()
		test.addRed(1,1)
		test.addRed(1,2)
		test.addBlue(1,2)
		test.addBlue(2,0)
	elif '-girl' in sys.argv:
		test.addNode()
		test.addNode()
		test.addBlue(0,2)
		test.addRed(2,1)
	else:
		test.setup()
	if '-r' in sys.argv:
		player = 'red'
	if '-nv' in sys.argv:
		test.toggleVerbose(False)
	if '-d' in sys.argv:
		test.toggleDebug(True)
	if '-s' in sys.argv:
		test.setup()
	test.play(player)

main()
	
