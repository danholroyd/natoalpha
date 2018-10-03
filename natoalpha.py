#! /usr/bin/python3

dict = {'a':'Alpha',
 'b':'Bravo',
 'c':'Charlie',
 'd':'Delta',
 'e':'Echo',
 'f':'Foxtrot',
 'g':'Golf',
 'h':'Hotel',
 'i':'India',
 'j':'Juliet',
 'k':'Kilo',
 'l':'Lima',
 'm':'Mike',
 'n':'November',
 'o':'Oscar',
 'p':'Papa',
 'q':'Quebec',
 'r':'Romeo',
 's':'Sierra',
 't':'Tango',
 'u':'Uniform',
 'v':'Victor',
 'w':'Whiskey',
 'x':'X-ray',
 'y':'Yankee',
 'z':'Zulu',
 ' ':' ',
 '1':'One',
 '2':'Two',
 '3':'Three',
 '4':'Four',
 '5':'Five',
 '6':'Six',
 '7':'Seven',
 '8':'Eight',
 '9':'Niner',
 '0':'Zero'}

def nato(string):
  for item in string.lower():
  	print(dict.get(item, 0))

  getName = input("Try another phrase, or leave blank to quit: ")
  if getName:
    nato(getName)
    
# start our function: 
getName = input("What word or phrase would you like to use?\n")
nato(getName)

