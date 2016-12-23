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
