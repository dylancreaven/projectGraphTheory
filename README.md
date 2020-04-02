# CODE TO BE REVIEWED FOR PROJECT IS REGEX.PY
# Dylan Creaven - G00354442
# README - Graph Theory Project - Non-Deterministic Finite Automaton


Objective of Project: Create a program that was able to create a Non-Deterministic Finite Automaton to represent
a regular expression and match a string to the regular expression.

How to use: Run program, either by double-clicking program or by opening the folder in the command prompt and using the command "python regex.py"
A prompt will appear on the screen asking if you wish to input your own regular expression & string. Type 'Y' if yes and 'N' if no. Anything other than 'Y' or 'N' (or lowercase equivalent) will result in user being asked to
input their choice again.
Then type in your regular expression, and the string you want to see if it matches the regular expression.
Then the program will output if your string is accepted by the regular expression

How each Section of code works: 

State - A class for an object, with edges/arrows coming out of it and labels for each edge

Fragment - A class for a fragment of a Non-Deterministic Finite Automaton with a start state and accept state

shunt(infix) - a function that takes in a regular expression as a string, assumes the string is in infix notation and converts it to postfix notation. Uses a dictionary to create precedence for each operator in a regular expression.

compile(infix) - a function that takes in a regular expression as a string, assumes the string is in infix notation, then calls the shunt function to convert the string to postfix notation.
Then it uses the postifx string and converts that into a list format. Then it goes through each character in the list (i.e the postfix string) and if the character is a letter/number (i.e a non-special character). If the character is a special character (e.g '|') then the program has special 
routes just for those characters. It will pop fragment(s) off the stack and choose the edge/arrow followed by which operator is being looked at.

followEs(state,current) - adds the state to the set (called current) and follows all the E edges/arrows on the state. E edges are indicated by having their label as None

match(regex, s) - takes in a regular expression and a string and tries to match them together. 
Loop through every character in the string and for each one, follow the arrow using the FollowEs function. 
Then if the accept state is the state inside the set current then the NFA(generated based on the regular expression)
matches the string s.


tests=[] - set that contains tests which themselves contain a regular expression and a string and a boolean which indicates what the result of the test should be.
Then loop through every test in the set and try to match the string to the regular expression. If the test passes then nothing will be outputted, 
but if it fails an error will appear indicated what the result SHOULD be.

User Input - After Tests are run, user is prompted if they wish to input their own regular expression and string to match it against. If yes, the user inputs their own regular expression and string
and the program attempts to match them and then outputs the result.




