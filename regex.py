#Dylan Creaven - Graph Theory Project
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
        
class Fragment:
    #start state of NFA fragment
    start = None
    #accept state of NFA fragment
    accept = None
    
    #Constructor
    def __init__(self,start,accept):
        self.start=start
        self.accept=accept

def shunt(infix):
    #convert input to a stack list
    infix=list(infix)[::-1]

    #operator stackIndexError: list index out of range
    opers =[]

    #Output List. 
    postfix=[]
    #operator precedence
    prec={'*':100,  '.':90,  '|':80,   ')':70,    '(':60}

    #loop through input one character at a time
    while infix:
        #pop a character from the input
        c=infix.pop() 
        #decide what to do based on character
        if c== '(':
            #push an open bracket to opers stack
            opers.append(c)
        elif c==')':
            #pop the operators stack until you find an open bracket
            while opers[-1]!='(':

                 postfix.append(opers.pop())
            #get rid of '('
            opers.pop()
        elif c in prec:
            #push any operators on opers stack with hight prec to output
            while opers and prec[c] < prec[opers[-1]]:
                postfix.append(opers.pop())
            opers.append(c)
        else:
        #typically we just push the character to the output
            postfix.append(c)

    #pop all operators to the output
    while(opers):
        postfix.append(opers.pop())
    #convert output list to string
    return ''.join(postfix)

def compile(infix):
    postfix = shunt(infix)
    postfix=list(postfix)[::-1]
    
    nfa_stack = []
    while(postfix):
        #pop character from postfix
        c= postfix.pop()
        if(c=='.'):#pop two frags off stack
            frag1=nfa_stack.pop()
            frag2=nfa_stack.pop()
            #point from end of frag2 to start of frag1
            frag2.accept.edges.append(frag1.start)
            #create new fragmentfor combo of frag1 and frag2
            newfrag=Fragment(frag2.start,frag1.accept)
            
        elif(c=='|' ):
            #pop 2 frags off stack
            frag1=nfa_stack.pop()
            frag2=nfa_stack.pop()
            #create new start and accept states
            accept = State()
            start= State(edges=[frag2.start,frag1.start])
            #point old accept states at new one
            frag2.accept.edges.append(accept)
            frag1.accept.edges.append(accept)
            newfrag=Fragment(start,accept)
            
        elif(c=='*'):
            #pop single fragment off stack
             frag= nfa_stack.pop()
             #create new start and accept state
             accept = State()
             #point arrows i
             start= State(edges=[frag.start,accept])
             frag.accept.edges=[frag.start,accept]
             #create new instance of fragment to represent the new nfa
             newfrag= Fragment(start,accept)
        else:
            accept = State()
            start = State(label=c,edges=[])
            #create new instance of fragment to represent the new nfa
            newfrag = Fragment(start,accept)
        #push new nfa to stack
        nfa_stack.append(newfrag)
            

    #the nfa stack should have exactly one nfa one it -  the answer
    return nfa_stack.pop()

#add a state to a set and follow all of the Epsilon arrows
def follow(state,current):
    #only do something when we havent already seen this state
    if state not in current:
        #put state into current
        current.add(state)
        #see whether state is labelled by Epsilon
        if state.label is None:
            #loop through the states pointed to by this state
            for x in state.edges:
                #follow all of their epsilons too
                follow(x, current)

def match(regex, s):
    #return true if regex=s (fully matches, no partial match)
    # compile regex into nfa
    nfa = compile(regex)


    #try to match the regular expression to the string s

    #the current set of states 
    current= set()
    #add first state and follow all epsilons arrows
    follow(nfa.start, current)

    # the previous set of states
    previous = set()

    for char in s:#loop through characters in string
        #keep track of where we are
        previous = current
        #create a new empty set for states were gonna be in
        current = set()
        #loop trhough previous states
        for state in previous:
            #only follow arrows not labelled Epsilon
            if state.label is not None:
                #if label of state is equal to character we've read
                if state.label==char:
                    #append the state at end of arrow to current.
                     follow(state.edges[0],current)
            
    #see if nfa matches string s
    return nfa.accept in current
    
print(match("a.b|b*","bbbbb"))
