#!/usr/bin/env python

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
            This Initilzes the state space graph with currentNumber.
        '''
        # Making a Vertex for the currentNumber 
        if isinstance(currentNumber, int): # making sure of the type int.
            self.root = Vertex ( currentNumber )
            '''
            # Testing the Graph constructor 
            print ( root.currentNumber )
            print ( root.level         )
            print ( root.status        )
            '''
# end __init__()

    def generateChildren ( self, vertex ):
        '''
            This funciotn take a vertex
            and returns its children list.
        '''
        # Making the children list of vertex.
        if isinstance(vertex, Vertex): # making sure of the type Vertex.
            children = []
            i = 1
            while i*i < vertex.currentNumber:
                children.append ( Vertex (vertex.currentNumber - i*i) )
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


# end class graph

'''
# Testing the graph class
graph = Graph (  12  )
print ( "The Root is: " ,  graph.root.currentNumber)
ls = graph.generateChildren ( Vertex ( 12 ) )
i = 0
while i < len(ls):
    print ( ls[i].currentNumber )
    i += 1
'''
