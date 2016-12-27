from graph import Graph
import math 


'''
    The Algorithm 
'''
def isSquare(integer): # to check if the number is a perfect square
    root = math.sqrt(integer)
    if int(root + 0.5) ** 2 == integer:
        return True
    else:
        return False


class InputError(Exception):
     def __init__(self, value):
         self.value = value
     def __str__(self):
         return repr(self.value)

maxsize = 1e500

class Vertex(object): # To generate nodes with heuristic values
    def __init__(self, i_depth,i_playerNum,numremains, i_value=0): #i_depth is our level in the tree now// i_playerNum is the current player(computer or Human)
        self.i_depth = i_depth  # how deep are we in the tree (decreases every iteration)
        self.i_playerNum = i_playerNum  # (either +1 or -1)
        self.numremains=numremains # remaining number from subtraction  ( needed to keep track of the number )
        self.i_value = i_value  # gamestate: -inf, 0 or +inf
        self.children = []
        self.createChildren()

    def createChildren(self): # recursion function to create children from the tree and assigning heuristic value to each one

        if self.i_depth >= 0: # if we  pass the DEPTH of  0 function stops ( recursion base case)

             for i in range(0,self.numremains): #Loop from 0 to the remaining number from subtraction
                v = self.numremains-(i*i) #value of the new child from subtraction
                self.children.append(Vertex(self.i_depth - 1, -self.i_playerNum, v,
                                          self.realVal(v)))  # add to childrens list, depth goes down, switching players "computer and human"

    def realVal(self, value):# To assign heuristic values to nodes
        if (value == 0):
            return maxsize * self.i_playerNum  #  this means human is winning 
        elif (value < 0):
            return maxsize * -self.i_playerNum  # this means computer is winning
        return 0  # neither winning nor losing state
  #end class vertex

def MinMax(vertex, i_depth, i_playerNum):# recursion function stops if it reached the deadend
    if (i_depth == 0) or (abs(vertex.i_value) == maxsize):  # have we reached depth 0 or the best node ( winning node)?
        return vertex.i_value # passing the best node up to the current node

    i_bestValue = maxsize * -i_playerNum  # this to make computer think of the best value to win

    for i in range(len(vertex.children)):#loop on children of the vertex
        child = vertex.children[i]
        i_val = MinMax(child, i_depth - 1, -i_playerNum)
        if (abs(maxsize * i_playerNum - i_val) < abs(maxsize * i_playerNum - i_bestValue)): # checking if the value of the child is closer to the value that makes the win
            i_bestValue = i_val  # if so assign it


    return i_bestValue

 #end function minmax
def winCheck(total, i_playerNum):#check if the move selected is a winning move
    if total <= 0:
        print("*" * 30)
        if i_playerNum > 0:
            if total == 0:
                print("\tHuman won!")
                exit(1)
            else:
                print("\tToo many chosen, you lost!")#when human subtract number bigger than the actual number
        else:
            if total == 0:
                print("\tComputer won!")
                exit(1)
            else:
                print("\tComputer lost..")
        print("*" * 30)
        return 0
    return 1
  #end function wincheck


# the output >> playing game and calling functions
if __name__ == '__main__':

    i_depth = 1
    i_curPlayer = 1 # this means human is starting i.e. computer is -1
    print("""Instructions: pick up the starting number.
               \t\t\t.""")
    totalNum=int(input())
    graph= Graph(totalNum)
    graph.generateStates() # generating state space graph of all the possible moves
    j=0


    for j in range(len(graph.stateSpaceGraph)):
       if (j==len(graph.stateSpaceGraph)-1):
           i_depth=(graph.stateSpaceGraph[j].level)+1#to know the depth of the graph


    while (totalNum >= 0):
        ## HUMAN TURN
        print("\n%d total number remain. Enter your desired square number to be subtracted." % totalNum)
        i_choice = int(input("\n:               "))


        totalNum-= int(float(i_choice*i_choice))  # store choice of human
        ## COMPUTER TURN
        if winCheck(totalNum, i_curPlayer): # check if human won or not
            i_curPlayer *= -1 # switch players ( computer turn now )
            vertex = Vertex(i_depth, i_curPlayer, totalNum)
            bestChoice = -1
            i_bestValue =  -i_curPlayer * maxsize
            for i   in range(len(vertex.children)):
                n_child = vertex.children[i]
                #print(vertex.children[i].i_value) test case
                i_val = MinMax(n_child, i_depth, -i_curPlayer) # assiging best value
                #if (abs(i_curPlayer * maxsize - (i_val) ) <= abs(i_curPlayer * maxsize - (i_bestValue))):# test condition to check if the computer choosed the right number
                if(isSquare(i+1)==True & (i+1*i+1)<=totalNum): # ensure that the computer only subtract valid square number
                    #i_bestValue = i_val
                    bestChoice = i
            bestChoice+=1 # the loop starts from 0 , of course we don't want to choose 0 :')
            if bestChoice==0: # if there is no possible moves  .. choose 1
                bestChoice=1
            print("Comp chooses: " + str(bestChoice))

            totalNum -= int(bestChoice) # subtracting the remaining number from computer choice


            winCheck(totalNum, i_curPlayer) # to check if the computer had won
            i_curPlayer *= -1  #  if not .. switch players again
