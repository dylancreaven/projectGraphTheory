# Overview.MD
### Graph Theory Project 2020
### Dylan Creaven - G00354442

## Introduction
This repository contains two python files (regex.py and shunting.py) that work together as a program to recieve a regular expression and a string from the user. The program converts the regular expression into a Non-Deterministic Finite Automaton (NFA) and compares the NFA to the string inputted and sees if the two match. It outputs the result of this comparison to the console e.g a regular expression might be:
>a.b|c*

and a string that MATCHES that regular expressions's NFA would be something like:
>ab

This would output a TRUE result to the console.
Also in the repository is a python file (hello.py) and a C file (hello.c). These are test files from the beginning of the project development process and dont contribute anything to the repository's main fucntion and thus can be ignored.

## Run
To run this program you will first need to download python onto your computer
#### To install Python:
First you must make see if you already have python istalled or not. This can be done by going into your PC's command prompt (typing cmd in bottom left search bar on Windows/ Ctrl+Del+T on Linux. Once you have the command prompt open simply type "python --version"
and enter.
If you do not have python installed, the console will spit out an error message at you. If you do,
it will say what version of python you have installed e.g Python 3.8.2.
To install python, you must go to https://www.python.org/downloads/windows/ or the equivalent on Linux. Choose the Latest version of Python displayed on the page (at the time lf writing this MD Document it is 3.8.3), the site will bring you to the page for that version of Python, scroll down to the Files section and choos the executable files from the list e.g.
> Windows x86 executable installer

Once downloaded, run the .exe file. Follow the on-screen instructions on how to install Python. Wait for installation to finish and then close the window. Python should now be installed. Remember you can confirm that python is installed by typing "python --version" into the command prompt and if Python has been installed the console
should output the verison of python installed
#### How to Run the Program
To run the program either click on the regex.py file within file explorer or type "python regex.py" in the command prompt (must be within the project folder within command prompt i.e.
