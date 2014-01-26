hackenpy
========

Text-based Hackenbush in Python.

how to play
-----------

Run ```python hacken.py```. 

You will be prompted to setup the playing field. Type in ```n``` to place a node. ```b``` or ```r``` to place a blue or red edge. ```s``` to show the playing field. ```d``` to delete an edge or node.

When placing an edge, you will be asked which two nodes to connect. To connect to the ground, specify ```0```.

When finished placing edges, type in ```f``` to start playing. 

The playing field is represented as below. Blue and red edges are numbered ```b1, b2, r1, r2```. Nodes are numbered ```(1), (2), (3)```.
<pre>
|
|____b1____(1)____r1____(2)____b2____(4)
|                          \___r2____(3)
|____r3____(5)____b3____(6)
|
</pre>

This is equivalent to:
<pre>
| = Blue
# = Red

  #   /
   # /		
	#		|
	#		|
	|		#
	|		#
-----------------
</pre>

On each player's turn, the game shows a list of their available edges. Type in an edge name to remove it. If one or more edges becomes disconnected from the ground, they are removed from play. ```s``` shows the playing field.

By default blue goes first. Run with ```-r``` to start with red (see Options).

Whichever player runs out of available edges loses.

options
-------

Following options are available. Append them to the script run command (i.e. ``` python hacken.py -r```). 

<pre>
-r				Red goes first.
-nv				Less verbose instructions.
-d				Show debug information.
-game1			Play sample game 1.
-game2			Play sample game 2.
-game3			Play sample game 3.
-s				Use with -game option to edit the game.
</pre>

how it works
------------

The playing field is represented by a graph.

The ground is represented by a single vertex. 

Blue and Red edges are connected either to the ground, or to a single other edge.

When an edge is removed, the ```displayFromVertex``` function figures out how to update and display the playing field through depth-first search starting from the 'ground' vertex. This models how edges "float off" out of play if not connected to the ground.

to do
-----

- [ ] Bug testing
- [x] Better visual representation
- [x] Streamline the graph representation
    - [x] Get rid of Vertex class (not needed)