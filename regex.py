#Dylan Creaven - G00354442
#Graph Theory Project 2020
import shunting
import argparse
class State:
    """A State with one or two edges/arrows, with all edges/arrows labelled w/ label"""
  # Constructor.
    def __init__(self, label=None, edges=None):
        # Every state has 0, 1, or 2 edges from it.
        self.edges = edges if edges else []
        # Label for the arrows. None means epsilon.
        self.label = label
        
class Fragment:
    """A fragment of a Non-Deterministic Finite Automaton with a start state and accept state"""
    #Constructor
    def __init__(self,start,accept):
        self.start=start
        self.accept=accept


def compile(infix):
    """Return Fragment of NFA that represents infix regex"""
    #convert infix to postfix
    postfix = shunting.shunt(infix)
    #make a listfix stack of chars and invert it
    postfix=list(postfix)[::-1] 
    #stack for nfa fragments
    nfa_stack = []
    while(postfix):
        #pop character from postfix
        c= postfix.pop()
        if(c=='.'):#pop two frags off stack
            frag1=nfa_stack.pop()
            frag2=nfa_stack.pop()
            #point from end of frag2 to start of frag1
            frag2.accept.edges.append(frag1.start)
            #frag2's start state is new start state
            start = frag2.start
            #frag1s new accept state 
            accept = frag1.accept
        elif(c=='|' or c=='/' or c=="\\"):
            #pop 2 frags off stack
            frag1=nfa_stack.pop()
            frag2=nfa_stack.pop()
            #create new start and accept states
            accept = State()
            start= State(edges=[frag2.start,frag1.start])
            #point old accept states at new one
            frag2.accept.edges.append(accept)
            frag1.accept.edges.append(accept)
        elif(c=='*'):
            #pop single fragment off stack
             frag= nfa_stack.pop()
             #create new start and accept state
             accept = State()
             #point arrows i
             start= State(edges=[frag.start,accept])
             frag.accept.edges=[frag.start,accept]     
        else:
            accept = State()
            start = State(label=c,edges=[accept])
        #create new instance of fragment to represent the new nfa
        newfrag = Fragment(start,accept)
        #push new nfa to stack
        nfa_stack.append(newfrag)
    #the nfa stack should have exactly one nfa one it -  the answer
    return nfa_stack.pop()

def followEs(state, current):
    """Add a state to a set and follow all e arrows/edges"""
    #only do something when we haven't already seen the state
    if state not in current:
        #put the state itself into the state
        current.add(state)
        #See whether state is labelled be E
        if state.label is None:
            #Loop through the states pointed to by this state
            for x in state.edges:
                #follow all of their epsilons too
                followEs(x, current)
                
def match(regex, s):
    """Match a string to an NFA"""
    #this function will return true if and only if the regular expression
    #regex (fully) matches the string s. It returns false otherwise
    
    #compile the regular expression into nfa
    nfa = compile(regex)

    # try to match the regular expression to the string s.
    #the current set of states
    current = set()
    #add the first state, and follow all of epsilon arrows
    followEs(nfa.start, current)
    #the previuos set of states
    previous = set()
    #loop through characters in s
    for c in s:
        previous = current
        #creat a new empty set for states we're about to be in
        current = set()
        #loop through the previous states
        for state in previous:
            #only follow arrows not labeled by E (epsilon)
            if state.label is not None:
                #if the label of the state is = to the character we've read
                if state.label == c:
                    #add the state(s) at the end of the arrow to current.
                   followEs(state.edges[0], current)
    #ask the nfa if it matches the string s.
    return nfa.accept in current	

# concatenation . does not work as required
if __name__ == "__main__":
    """Main code of file, where you test the program and allow user to input their own regular expressions and strings to match together"""
    tests=[
        ["a.b","ab",True],
        ["a.b","c",False],
        ["b*","bbb",True],
        ["b*","ba",False],
        ["a|b","a",True],
        ["a|b","f",False],
        ["a.b|b*","bbbbbbb",True],
        ["a.b\\z","z",True],
        ["a.b\\z","okay",False],
        ["a.b/t*","tttt",True],
        ["a.b/y","Ggggg",False],
        ["b*","",True]        
    ]
   # print("TESTS")
    for test in tests:
        #Uncomment two lines below to have tests and their results printed to screen
        #print("Regex: "+test[0]+" String: "+test[1])
        #print(match(test[0],test[1]))
        assert match(test[0],test[1])==test[2],test[0] +\
        (" Should" if test[2] else " Should not")+" match "+test[1]
     
     
    #add a parser to the script using argparse
    parser = argparse.ArgumentParser(add_help=False,prog='G00354442 - Dylan Creaven\'s Graph Theory Project 2020')
    #use parser to create command line arguments and their help message
    
    #shows name of Project
    parser.add_argument('--name','-name',action='help', help='Project name: %(prog)s')
    #takes in a regular expression 
    parser.add_argument("-regex","--regex",help="Takes in Regular Expression  - Instead of '|', use '\\' or '/' as the OR operator",type=str)
    #takes in a custom string
    parser.add_argument("-string","--string",help="String to match to NFA generated by regular expression",type=str)
    #outputs help section and shows all the possible command line arguments
    parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS, help='Default Help Message of Project Command line')
    args = parser.parse_args()
    #takes in regular expression and string from command line arguments and tries to match them using the match() function
    if(str(args.regex) !="None" and str(args.string) !="None"):
       print("Regex: ",str(args.regex)," String: ", str(args.string), " Result:",  match(str(args.regex), str(args.string)))
       print("Thank you and Goodbye!")
         
    else:
        #Get User Input from command line
        print("Would you like to test your own regular expression and String? ")
        choice = input("Y/N \n\n")
        
        #If yes then recieve regular expression and string from user and try to match them
        while(choice.casefold()!='n'):         
            if(choice.casefold()=='y'):
                regex = input("Please enter your regular expression!: ")
                string = input("Please enter your string to be matched!: ")
                print("Regex: ",regex," String: ", string, " Result:",  match(regex, string))
            else:
                print("Invalid Option - Please Try Again")
            print("\nWould you like to test your own regular expression and String? ")
            choice = input("Y/N \n\n")
        #end program
        print("Thank you and Goodbye!") 