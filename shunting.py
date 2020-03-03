#Dylan Creaven
# =The Shunting Yard algoritm for regex

infix ="(a|b).c*"
print("Input: "+infix)

#Expected output ab|c*.
print("Expected Output: ab|c*.")

#convert input to a stack-ish list
infix=list(infix)[::-1]



#operator stack
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
             postfix.append(opers.push())
         opers.append(c)
    else:
    #typically we just push the character to the output
         postfix.append(c)

#pop all operators to the output
while (opers):
    postfix.append(opers.pop())
    


#convert output list to string
postfix=''.join(postfix)


##Print result
print("Output: "+postfix)
