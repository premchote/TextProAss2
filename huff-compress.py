import pickle as pk
import numpy as np
import re
import sys,getopt


"""
Type -h to print help
"""

def char_prepro(text): #For make text as a vector
    term = {}
    for t in text:
        if t in term.keys():
            continue
        else:
            term[t] = [i for i, x in enumerate(text) if x == t]
    return term

def main(argv):
    inputfile = argv[len(argv)-1] #initial inputfile
    print("The inputfile is ",inputfile)
    try:
        opts, args = getopt.getopt(argv,"hi:s:o::",["ifile=","Mode","ofile="])
    except getopt.GetoptError:
        print('Please input argument with this patterm huff-compress.py [-s {char (For character)/word (For String)}] <outputfile> or -h to print help')
        exit()
    for opt, arg in opts:
        print(opts)
        if opt == '-h':
            print("Help!!!!!!!!!!!!!!!")
            exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-s","--Mode"): #Checking mode
            if arg == "char": #Character mode
                Mode = True #True for character
            elif arg == "word":
                Mode = False #False for string
            else:
                print("Mode error") #Not either case
                exit()
        elif opt in ("-o", "--ofile"):
            outputfile = arg
            
    print('Input file is "', inputfile)
    print('Mode is ',Mode)
    #print('Output file is "', outputfile)

if __name__ == "__main__":
   main(sys.argv[1:])
