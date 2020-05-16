# Overview.MD
### Graph Theory Project 2020
### Dylan Creaven - G00354442

## Introduction
This repository contains two python files (regex.py and shunting.py) that work together as a program to receive a regular expression and a string from the user. The program converts the regular expression into a Non-Deterministic Finite Automaton (NFA) and compares the NFA to the string inputted and sees if the two matches. It outputs the result of this comparison to the console e.g. a regular expression might be:
`a.b|c*`

and a string that MATCHES that regular expressions’ NFA would be something like:
`ab`

This would output a TRUE result to the console.
Also, in the repository is a python file (hello.py) and a C file (hello.c). These are test files from the beginning of the project development process and don’t contribute anything to the repository's main function and thus can be ignored.

## Run
To run this program, you will first need to download python onto your computer
#### To install Python:
First you must make see if you already have python installed or not. This can be done by going into your PC's command prompt (typing cmd in bottom left search bar on Windows/ Ctrl+Del+T on Linux. Once you have the command prompt open simply type "python --version"
and enter.
If you do not have python installed, the console will spit out an error message at you. If you do,
it will say what version of python you have installed e.g. Python 3.8.2.
To install python, you must go to https://www.python.org/downloads/windows/ or the equivalent on Linux. Choose the Latest version of Python displayed on the page (at the time of writing this MD Document it is 3.8.3), the site will bring you to the page for that version of Python, scroll down to the Files section and choose the executable files from the list e.g.
> Windows x86 executable installer

Once downloaded, run the .exe file. Follow the on-screen instructions on how to install Python. Wait for installation to finish and then close the window. Python should now be installed. Remember you can confirm that python is installed by typing "python --version" into the command prompt and if Python has been installed the console
should output the version of python installed
#### How to Run the Program
##### To run the program 
Firstly, to download the project, you need to copy the link of the repository
> https://github.com/dylancreaven/projectGraphTheory
Then open a command prompt on your computer and enter the command in this format: `git clone REPOSITORY_URL`.
This should **clone** the entire repository onto your local machine. Open the project folder in file explorer so it should look something like:

![file_explorer](/images/file_explorer.png)

Either double-click on the regex.py file or type "python regex.py" in the command prompt (must be within the project folder on the command prompt i.e.

![command_prompt](/images/cmdpic.png)

The program will ask if you wish to enter your own regular expression, Enter Y or y for yes and N or n for no. 
The program will then ask you for regular expression e.g. a.b|c*
Enter in your own regular expression, press enter.
Then you will be asked for a string to try to match to the NFA generated from your regular expression e.g. "cccc"
Then the program will output whether the inputted string matches the NFA. 
The program will then ask if you want to again enter in a regular expression/String or Quit the program.

##### You can also use the program using arguments in the command line
You can see all the argument commands, and how to use them by entering "python regex.py --help" into the command line of the project's folder in file explorer. 

The main function that can be used from command line arguments is you can enter in your own regular expression and a string into the command line and it will output if the string matches the NFA created by the regular expression e.g.
`python regex.py -regex a.b\c* -string ccccc`

And this should output the result: True. 

However, the console cannot take in "|" as a command line argument, so if using the command line, you must use "/" or "\" as a substitute for "|", the OR operator in regular expressions.

## Test

There are already Tests within the program code. The tests run just before the program prompts the user if they wish to enter their own regular expression and string.

To add your own tests to the code, go to line 117 where you can see an array called tests. Add your own test inside the [] brackets of the array in this order:
` ["REGULAR EXPRESSION","STRING”, EXPECTED RESULT]`

Examples of tests that are expected to be true and false are:
` ["a.b|c*","ab”, True]`

` ["a.b|c*","tttttt”, False]`

The example tests shown above will both pass and are true so will therefore not output any error out to the screen but a test which doesn't pass i.e. the expected result does not match the actual result, then an error message will appear
Here's an example of a test that will not pass:
`["k|d*","qqqq”, True]`

And the error that appears: 

![error](/images/test_error.png)

The code just below the array of tests is a for loop that goes through each test in the array and **asserts** if the expected result is equal to the actual result and outputs an Assertion Error to the console if they do not match.

## Algorithms
The code can be boiled down to simple steps:
1. Take in a regular expression and convert it from infix to postfix notation. This is a way to re-organise a regular expression so that all the operators e.g "|", "\*" etc. are grouped together and that all the characters read in e.g. 'a', 'd' etc. are also all together, to make for an increase in ease of reading through the regular expression and constructing an NFA based on it. This is done using the shunting algorithm from shunting.py and is imported into regex.py. A regular expression already in postfix notation and is put through the shunting algorithm will come out the exact same way as it went it, it will stay in postfix notation.

A regular expression being converted from infix to postfix as you can see the order of the operators change

![inifx to postfix](/images/infix_to_postfix.png)

A regular expression being converted from postfix to postfix, no order change

![postfix to postfix](/images/postfix_to_postfix.png)

2. The compile function will take in the regular expression in **postfix notation** and will move through its character by character and will start creating the Non-Deterministic Finite Automaton (NFA) based on the characters it encounters throughout the expression

In this diagram there is an example regular expression: a.b|c* which means any string with:
an 'a' followed by a 'b' OR a string with any number of c's e.g. "cccccc" will pass. 
The diagram shows an NFA in image form and how to navigate it. This means that we should, by following the chart, be able to say whether any string matches the nfa i.e. ends up in an accept state (any state with a double circle)


![nfa diagram](/images/explanation_of_nfa.png)

3. The program will then go through the string entered and pass it through the nfa using the match function. If that string should end up in an accept state **and** stays in that state until the string has fully gone through the NFA then they match and the result outputted is "True" otherwise (i.e. if the string doesn't end up in an accept state) then "False" is outputted.

### How to use the argparse package
The argparse package gives you control over what happens when certain arguments are added in the command line.
After importing it at the top of my code, you add the parser to the main method:
`parser = argparse.ArgumentParser()`

And then use "parser.add_argument()" to add custom arguments to the program e.g.
`parser.add_argument("-example", help="this is an example argument")`

This will add a custom argument to the program and can be seen when the help command is used
![custom argument](/images/custom_argument.png)

After all your arguments have been added you must add this line to add the parsed arguments to a variable
`args = parser.parse_args()`

If you wish to use arguments given from the command line in a method within your code, first you must add a type when you're adding an argument e.g.:
`parser.add_argument("-example", help="this is an example argument",type=str)`
This will tell the program to expect a string after the "-example" argument in the command line. Here's an example of what that would look like in your command prompt:
`python regex.py -example EXAMPLE`

After receiving an input, you can use the argument in your code by using `type(args.example)`.The "type" being the type of variable you have chosen e.g. str for a string, int for an Integer. 
Make sure the word after "args." is the same word you named the argument when you added it above. Here's an example of the whole code put together now:
```
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-example", help="this is an example argument",type=str)
args = parser.parse_args()
if(str(args.example) =="Example"): # if string taken in from command line is equal to 'Example'
  print("Here I am using the argument from command line in my code")
```
So, if, within the command line, I entered `python regex.py -example Example`
then the text "Here I am using the argument from command line in my code" shall appear in the console.

## References
This link from tutorialspoint was very useful for me understanding what regular expressions were and how they worked and especially how they worked in **python**
https://www.tutorialspoint.com/python/python_reg_expressions.htm

I used this tutorial on the argparse package and how to change the custom messages for the `--help` argument
The tutorial is aimed at people just starting to learn Python, so the explanations are simple and nearly in layman's terms.
https://www.pythonforbeginners.com/argparse/argparse-tutorial

This is the official documentation from Python about the argparse package, talks about everything the package can do, and how to do it although it is the _official_ documentation which means; it almost expects the reader to have some experience already in Python so the explanations are more difficult than the pythonforbeginner's link above.

https://docs.python.org/3/library/argparse.html

This is from stackoverflow and I used the answer **that is marked as CORRECT** to learn how to take in arguments off the command line and use them within my code and even use them as arguments in functions in my program i.e. taking in regular expressions & strings and using them as arguments for my match function.

https://stackoverflow.com/questions/61563034/use-arguments-from-command-line-in-method


