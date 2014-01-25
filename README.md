hackenpy
========

Text-based Hackenbush in Python.

how to play
-----------

Run ```python hacken.py```. 

You will be prompted to setup the playing field. Type in ```b``` or ```r``` to place a blue or red edge. 

Edges are automatically numbered (i.e. b1, b2, r1, r2).

If there are one or more edges already placed, you will be asked which edge to connect to the new one. If you don't specify, the new edge will be connected to the ground.

When finished placing edges, type in ```x``` to start playing. 

The playing field is represented as below:
<pre>
| ---- b1 b1 ---- r1 r1 ---- r2 r1 ---- b2
| ---- r3 r3 ---- b3
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

On each player's turn, the game shows a list of their available edges. Enter the edge name to remove it and all edges "above" it. 

By default blue goes first. Run with ```-r``` to start with Red (see Options).

Whichever player runs out of available edges loses.

options
-------

Following options are available. Append them to the script run command (i.e. ``` python hacken.py -r```). 

<pre>
-r				Red goes first.
-board1			Play a sample game.
</pre>

how it works
------------

The playing field is represented by a graph.

The ground is represented by a single vertex. 

Blue and Red edges are connected either to the ground, or to a single other edge.

When an edge is removed, the ```displayFromVertex``` function figures out how to update and display the playing field through depth-first search starting from the 'ground' vertex. This models how edges "float off" out of play if not connected to the ground.

to do
-----

- [ ] Testing - any bugs?
- [ ] Better visual representation
- [ ] Streamline the graph representation
    - [ ] Get rid of Vertex class (not needed)
	- [ ] Allow Graph direct indexing (```Graph[x]```)