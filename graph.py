#!/usr/bin/env python
import operator

class Vertex:  
    '''
        * Vertex contains the vertex children as a list.
        * Vertex contains information bout a vertex.
    '''
    def __init__(self, currentNumber):
        self.currentNumber = currentNumber
        self.children      = []
        # These coming variables are for the Algorithm.
        self.level         = 0 # Increased during the game.
        self.open          = 0
        self.close         = 0
        self.status        = 'notOpened' 
# end __init__()  

# end class Vertex  

'''
# Testing: making a vertex, and give it children of type Vertex
# Making three Vertice 
ver1 = Vertex ( 1 ) 
ver2 = Vertex ( 2 )
ver3 = Vertex ( 3 )
# Printing the current Number of ver1
print ( ver1.currentNumber  )

# Adding ver2 and ver3 as children of vertex ver1
ver1.children.append( ver2 )
ver1.children.append( ver3 )

# printing the currentNumber of the children of ver1
print ( ver1.children[0].currentNumber )
print ( ver1.children[1].currentNumber )
# Result: (OK) it works

graph = [ ver1, ver2, ver3 ]
print ( graph[0].children[1].currentnumber )
'''

class Graph:
    '''
        This class has some graph tools.
    '''
    def __init__(self, currentNumber):
        '''
            This Initilzes the state space graph with the starting Number,
            And it adds the root to the [Graph]
        '''
        # List of vertices [Graph]
        self.stateSpaceGraph = []
        # Making a Vertex for the currentNumber 
        if isinstance(currentNumber, int): # making sure of the type int.
            # Making the starting number the graph ROOT
            self.root = Vertex ( currentNumber )
            # Adding the root to the [Graph]
            self.stateSpaceGraph.append ( self.root )
            '''
            # Testing the Graph constructor 
            print ( root.currentNumber )
            print ( root.level         )
            print ( root.status        )
            '''
# end __init__()

    def generateChildren ( self, vertex ):
        '''
            * This funciotn take a vertex
              and returns its children list.

            * It add the new children to the stateSpaceGraph [graph]
        '''
        # Making the children list of vertex.
        if isinstance(vertex, Vertex): # making sure of the type Vertex.
            children = []
            i = 1
            while i*i <= vertex.currentNumber:
                # Making Vertex for the new child
                newChild       = Vertex ( vertex.currentNumber - i*i )
                # Updating the level
                newChild.level = vertex.level + 1
                # Adding new child to the vertex children list
                children.append             ( newChild )
                # Adding children as  state in the [Graph]
                self.stateSpaceGraph.append ( newChild )
                # Sorting the graph/list based on the currentNumber attribute 
                self.stateSpaceGraph.sort(key = operator.attrgetter('currentNumber'), reverse=True )
                # The next square to be subtract 
                i += 1
            '''
            # Testing
            i = 0
            while i < len(ls):
                print ( ls[i].currentNumber )
                i += 1
            '''
            return children
# end generateChildren()

    def generateStates (self):
        '''
            It fills up the graph with all the game states.
        '''
        for state in self.stateSpaceGraph: 
            self.generateChildren ( state )



# end class graph

'''
# Testing the graph class
graph = Graph ( 20 )
print ( "The Root is: " ,  graph.root.currentNumber)
ls = graph.generateChildren ( Vertex ( 20 ) )

# Testing generateChildren()
i = 0
while i < len(ls):
#    print ( ls[i].currentNumber )
    i += 1

# Testing State Space Graph -- Before generaing all states/nodes.
j = 0
#while j < len(graph.stateSpaceGraph):
#   print ( graph.stateSpaceGraph[j].currentNumber , graph.stateSpaceGraph[j].level )
#    j += 1

# Testing Generating the hole graph
graph.generateStates()

# Testing State Space Graph -- After generating all nodes.
j = 0
while j < len(graph.stateSpaceGraph):
    print ( graph.stateSpaceGraph[j].currentNumber , graph.stateSpaceGraph[j].level )
    j += 1
'''
