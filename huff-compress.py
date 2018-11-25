import pickle as pk
import numpy as np
import re
import sys,getopt


"""
Type -h to print help
"""

def char_prepro(text):
    term = {}
    #print(text)
    for t in text:
        if t in term.keys():
            continue
        else:
            term[t] = [i for i, x in enumerate(text) if x == t]
    return term

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:co:",["ifile=","ModeC","ofile="])
   except getopt.GetoptError:
      print('test.py -i <inputfile> [-c (For character)/-s(For String)] -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
          print("Help!!!!!!!!!!!!!!!")
          sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-c","--ModeC"):
          if opt in ("-c"): 
            print("Character mode")#Character mode
          else:
            print("String mode") #String mode
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print('Input file is "', inputfile)
   print('Output file is "', outputfile)

if __name__ == "__main__":
   main(sys.argv[1:])
