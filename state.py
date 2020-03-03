#Dylan Creaven
#Classes in thompsons construction

class State:
    
    
    # Every state has 0,1 or 2 arrows/edges
    edges=[]
    
    
    #Label for the arrows. None means epsilon
    label=None
    
    #is this an accept state?
    #Constructor for the class

    def __init__(self,label=None,edges=[]):
        self.edges=edges
        self.label=label





class Frag:
    #start state of NFA fragment
    start = None
    #accept state of NFA fragment
    accept = None
    
    #Constructor
    def __init__(self,start,accept):
        self.start=start
        self.accept=accept

myInstance=State(label='a',edges=[])
myOtherInstance= State(edges=[myInstance])
myFrag=Frag(myInstance,myOtherInstance)
print(myInstance.label)
print(myOtherInstance.edges[0])
print(myFrag)

