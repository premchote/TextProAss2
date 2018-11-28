import pickle as pk
import numpy as np
import re
import sys,getopt
from array import array
from pickle import dump
"""
Type -h to print help
"""
#######################################################
############# -s char #################################
def ModeC(inputfile): #Function for character mode
    f = open(inputfile,'r')
    text = f.read()
    f.close()
    term = {} #initial the term vector
    for t in set(text):
        term[t] = [i for i, x in enumerate(text) if x == t]
    branch = {} #initial branch
    freq = {key:len(term[key]) for key in term.keys()} #Counting each character
    total_freq = sum(freq.values())
    i=0 #initial number of brach
    new_freq = freq #For making Huffman tree
    EoFkey ='EoF_' #generate EoF to encode with text
    while EoFkey in new_freq:
        EoFkey += '_' #make sure that EoFkey is not duplicate with text inside

    new_freq[EoFkey] = 1#add EoF in the vector
    table = {} #Initial encoding table

    while True:
        if (len(new_freq) < 2):
            break
        
        new_freq = {f:new_freq[f] for f in sorted(new_freq ,key = lambda f : new_freq[f])} #Sort key by values

        if type(list(new_freq.keys())[0]) is str and type(list(new_freq.keys())[1]) is str: #Connect str to str
            branch[i] = {
                            0 : list(new_freq.keys())[0],
                            1 : list(new_freq.keys())[1]
                        }
        elif type(list(new_freq.keys())[0]) is int and type(list(new_freq.keys())[1]) is str: #Connect branch to str
            branch[i] = {
                            0 : branch[list(new_freq.keys())[0]],
                            1 : list(new_freq.keys())[1]
                        }
            del branch[list(new_freq.keys())[0]]
                
        elif type(list(new_freq.keys())[0]) is str and type(list(new_freq.keys())[1]) is int: #Connect str to branch
            branch[i] = {
                            0 : list(new_freq.keys())[0],
                            1 : branch[list(new_freq.keys())[1]]
                        }
            del branch[list(new_freq.keys())[1]]
                
        elif type(list(new_freq.keys())[0]) is int and type(list(new_freq.keys())[1]) is int: #Connect branch to branch
            branch[i] = {
                            0 : branch[list(new_freq.keys())[0]],
                            1 : branch[list(new_freq.keys())[1]]
                        }
            del branch[list(new_freq.keys())[0]]
            del branch[list(new_freq.keys())[1]] #Delete unused keys
        new_freq[i] = list(new_freq.values())[0] +list(new_freq.values())[1] #Add branch to dict
        new_freq = {list(new_freq.keys())[i]:list(new_freq.values())[i] for i in range(2,len(new_freq))} #Delete 2 minimum
        i+=1

    def table_encode(branch,code=''): #Getting the coding table from dictionary
        for b in (0,1):
            try:
                if type(branch[b]) is dict:
                    table_encode(branch[b],code+str(b))
                else:
                    table[branch[b]] = code+str(b)
            except:
                continue
    #table will be like
    #{'a' :'0','b' : '01','c':'101'}

    branch = list(branch.values())[0]
    table_encode(branch)
    #encoding text
    data = ''
    for t in text:
        data += table[t] #change text to code


    table[True] = table[EoFkey]
    del table[EoFkey]
    #Adding EOF

    data = data + table[True] # Adding the EoF at the start and the end of File


    codearray = array('B') #Initial array

    if len(data)%8 != 0:
        data = data + '0'*(8-len(data)%8) #Make them to be bytes
    for i in range(0,len(data),8):
        codearray.append(int(data[i:i+8],2)) #Add data to the array

    try:
            os.remove('infile.bin') #If the file already exist, delete the file
    except:
            print('')
    f = open('infile.bin','w+b')
    codearray.tofile(f)
    f.close() #close file



    try:
            os.remove('infile-symbol-model.pkl') #If the file already exist, delete the file
    except:
            print('')
    pickle_out = open('infile-symbol-model.pkl','wb')
    dump(table,pickle_out)#Export the table
    pickle_out.close() #close file



    decode_table = {value:key for key,value in table.items()}


#######################################################

#######################################################
def main(argv):
    inputfile = argv[len(argv)-1] #initial inputfile
    print("The inputfile is ",inputfile)
    try:
        opts, args = getopt.getopt(argv,"hi:s:o::",["ifile=","Mode","ofile="])
    except getopt.GetoptError:
        print('Please input argument with this patterm huff-compress.py [-s {char (For character)/word (For String)}] <outputfile> or -h to print help')
        exit()
    for opt, arg in opts:
        #print(opts)
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
            
    if Mode: #Choose character mode
        ModeC(inputfile)
    #print('Output file is "', outputfile)

if __name__ == "__main__":
   main(sys.argv[1:])
