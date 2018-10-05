#Miguel Fuentes AI homework 2

#This rearranges the string s according to where the flip f is
def Flip(s,f):
    if f == 4:
        return(s[::-1])
    elif f == 3:
        return(s[0] + s[3] + s[2] + s[1])
    elif f == 2:
        return(s[:2] + s[3] + s[2])
    else: return s

#This is the integer value of the largest pancake which is out of place
def h(s):
    goal = '4321'
    misplacedPancakes = []

    for c in range(len(goal)):
        if(s[c] != goal[c]):
            misplacedPancakes.append(int(s[c]))
    if misplacedPancakes:
        return max(misplacedPancakes)
    return 0

class PancakeStack(object):
    flips = [] #This holds the history of all flips since the initial state
    state = "" #This is the current state

    #This is the constructor
    def __init__(self, parent, flip, initial='4321'):
        if parent is None:
            self.state = initial #Sets the starting node
        else:
            self.flips = parent.flips.copy() #copies the parent's flips
            self.flips.append(flip) #adds the new flip
            self.state = Flip(parent.state,flip) #adjusts state

    def __str__(self):
        return self.state #this is used to print the stack for testing

    __repr__ = __str__


def dfs(initialStack):
    fringe = [] #this is implemented as a stack
    closedSet = []

    fringe.append(PancakeStack(None, 0,initial=initialStack)) #adds the first node to the fringe
    oshit = 0 #This is here so the loop doesn't run forevor in case I messed something up
    while fringe:
        oshit = oshit + 1
        expandedNode = fringe.pop() #expand the top node of the stack

        if expandedNode.state == '4321' or oshit > 10000:
            return expandedNode #check if the solution is found
        elif expandedNode.state not in closedSet: #checks the closedSet before expanding
            #explore subsequent nodes
            stacks = [PancakeStack(expandedNode,2),PancakeStack(expandedNode,3),PancakeStack(expandedNode,4)]
            
            #This does the tiebreaking based on numerical value
            stacks.sort(key=lambda x: int(x.state),reverse=False) 
            for ps in stacks:
                fringe.append(ps) #adds new nodes to the fringe
            closedSet.append(expandedNode.state) #adds this node to the closed set
    return False


def greedy(initialStack):
    fringe = []
    closedSet = []

    fringe.append(PancakeStack(None, 0,initial=initialStack)) #adds the first node to the fringe
    oshit = 0 #This is here so the loop doesn't run forevor if I messed something up
    while fringe:
        oshit = oshit + 1

        #this sorts the fringe by the heuristic h then expands the lowest value node
        fringe.sort(key=lambda x: h(x.state),reverse=True) 
        expandedNode = fringe.pop()

        if expandedNode.state == '4321' or oshit > 10000:
            return expandedNode #checks for the solution
        elif expandedNode.state not in closedSet:
            #explore subsequent nodes
            stacks = [PancakeStack(expandedNode,2),PancakeStack(expandedNode,3),PancakeStack(expandedNode,4)]
            
            #This does the tiebreaking based on numerical value
            stacks.sort(key=lambda x: int(x.state),reverse=False) 
            for ps in stacks:
                fringe.append(ps) #adds new nodes to the fringe
            closedSet.append(expandedNode.state) #adds this node to the closed set
    return False

def ucs(initialStack):
    fringe = []
    closedSet = []

    fringe.append(PancakeStack(None, 0,initial=initialStack)) #adds the first node to the fringe
    oshit = 0 #This is here so the loop doesn't run forevor if I messed something up
    while fringe:
        oshit = oshit + 1

        #this sorts the fringe by the cost then expands the lowest cost node
        fringe.sort(key=lambda x: sum(x.flips),reverse=True) 
        expandedNode = fringe.pop()

        if expandedNode.state == '4321' or oshit > 10000:
            return expandedNode #checks for the solution
        elif expandedNode.state not in closedSet:
            #explore subsequent nodes
            stacks = [PancakeStack(expandedNode,2),PancakeStack(expandedNode,3),PancakeStack(expandedNode,4)]
            
            #This does the tiebreaking based on numerical value
            stacks.sort(key=lambda x: int(x.state),reverse=False) 
            for ps in stacks:
                fringe.append(ps) #adds new nodes to the fringe
            closedSet.append(expandedNode.state) #adds this node to the closed set

def aStar(initialStack):
    fringe = []
    closedSet = []

    fringe.append(PancakeStack(None, 0,initial=initialStack)) #adds the first node to the fringe
    oshit = 0 #This is here so the loop doesn't run forevor if I messed something up
    while fringe:
        oshit = oshit + 1

        #this sorts the fringe by the cost plus the heuristic then expands the lowest cost + heuristic node
        fringe.sort(key=lambda x: sum(x.flips) + h(x.state),reverse=True) 
        expandedNode = fringe.pop()

        if expandedNode.state == '4321' or oshit > 10000:
            return expandedNode #checks for the solution
        elif expandedNode.state not in closedSet:
            #explore subsequent nodes
            stacks = [PancakeStack(expandedNode,2),PancakeStack(expandedNode,3),PancakeStack(expandedNode,4)]
            
            #This does the tiebreaking based on numerical value
            stacks.sort(key=lambda x: int(x.state),reverse=False) 
            for ps in stacks:
                fringe.append(ps) #adds new nodes to the fringe
            closedSet.append(expandedNode.state) #adds this node to the closed set

def prettyPrint(initState,stack):
    #This prints the results in the way described in the homework
    loc = {4:0,3:1,2:2}
    state = initState
    g = 0
    for flip in stack.flips:
        print(state[:loc[flip]] + "|" + state[loc[flip]:] + " g: " + str(g) + " h: " + str(h(state)))
        g = g + flip
        state = Flip(state,flip)
    print(state + " g: " + str(g) + " h: " + str(h(state)))
