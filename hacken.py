import sys

class Vertex:
	def __init__(self, label, connections=[]):
		self.label = label
		self.connections = set(connections)

class Graph:
	def __init__(self):
		self.V = {}
	def add(self, vertex):
		self.V[vertex.label] = vertex.connections
	
class Hackenbush:
	def __init__(self):
		self.Field = Graph()
		self.Field.add(Vertex('|'))
		self.blues = 0
		self.reds = 0
	def inPlay(self):
		return [key for key in self.Field.V.keys() if key != '|']
	def lastBlue(self):
		return "b" + str(self.blues)
	def lastRed(self):
		return "r" + str(self.reds)
	def addBlue(self, other="|"):
		self.blues = self.blues + 1
		index = self.lastBlue()
		self.Field.add(Vertex(index, [other]))
		self.Field.V[other].add(index)
	def addRed(self, other="|"):
		self.reds = self.reds + 1
		index = self.lastRed()
		self.Field.add(Vertex(index, [other]))
		self.Field.V[other].add(index)
	def remove(self, vertex):
		connections = self.Field.V.pop(vertex)
		for v in connections:
			self.Field.V[v].remove(vertex)
	def displayFromVertex(self, vertex):
		seen = set()
		def recurse(next):
			seen.add(next)
			#print next + ":"+ str(self.Field.V[next])
			for v in self.Field.V[next]:
				if v not in seen:
					seen.add(v)
					print next +  " ---- " + v, 
					recurse(v)
				if next == vertex:
					print 
		recurse(vertex)
		notseen = set(self.Field.V).difference(seen)
		for v in notseen:
			self.Field.V.pop(v)
		print
	def display(self):
		self.displayFromVertex('|')
		#print self.Field.V
		#print
		
	def setup(self):
		print "Setup the playing field."
		color = None
		while color != "x":
			color = raw_input("(b)lue or (r)ed? (x) to finish. ")
			if color == 'b' or color == 'r':
				inPlay = self.inPlay()
				connect = None
				while connect == None:
					if inPlay != []:
						print "Connect to what? Leave blank for ground."
						print inPlay
						connect = raw_input()
					else:
						connect = ""
					if connect == "" or inPlay == []:
						if color == 'b':
							self.addBlue()
						else:
							self.addRed()
					elif connect in inPlay:
						if color == 'b':
							self.addBlue(connect)
						else:
							self.addRed(connect)
					else:
						connect = None
				print
				self.display()
			elif color != 'x':
				color = None
					
					
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
			self.remove(next)
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
		test.addBlue()
		test.addRed(test.lastBlue())
		test.addBlue(test.lastRed())
		test.addRed(test.lastRed())
		test.addRed()
		test.addBlue(test.lastRed())
	else:
		test.setup()
	if '-r' in sys.argv:
		player = 'red'

	test.play(player)
main()
	
