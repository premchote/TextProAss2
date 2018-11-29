import re
from array import array
from pickle import dump
import os



Testtext  = open('mobydick.txt','r')
Testtext = Testtext.read()
Testtext2 = Testtext
#Testtext = 'I\'m Prem. my name is "Prem" & Maybe; I\'m 24 years old'
######

#####
words = re.findall(r'[A-Za-z0-9]\w+|[A-Za-z0-9]|[&. ,\'-;\"?\n!£$\[\]\{\}\%()]',Testtext) #set of words and numbers
set_words = set(words)

#[A-Za-z0-9]\w+|[A-Za-z0-9]|[&. ,'-;\"?\n!]
    
freq = {} #initial frequency
for word in set_words: #Add words to freq
    try:
        freq[word] = len(re.findall(word, Testtext))
    except:
        freq[word] = len([i for i, x in enumerate(Testtext) if x == word])
EoFkey ='EoF_' #generate EoF to encode with text
while EoFkey in freq:
    EoFkey += '_' #make sure that EoFkey is not duplicate with any text inside
freq[EoFkey] = 1#Add EoF in the freq
new_freq = freq
branch = {} #initial branch
i = 0
while True:
    if (len(new_freq) < 2):
        break
    if i%1000 == 0:
        print(i)
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
    del new_freq[list(new_freq.keys())[0]]
    del new_freq[list(new_freq.keys())[0]]
    #new_freq = {list(new_freq.keys())[i]:list(new_freq.values())[i] for i in range(2,len(new_freq))} #Delete 2 minimum
    i+=1
    
table = {} #initial table
print("Preparing the table")
def table_encode(branch,code=''): #Getting the coding table from dictionary
    for b in (0,1):
        try:
            if type(branch[b]) is dict:
                table_encode(branch[b],code+str(b))
            else:
                table[branch[b]] = code+str(b)
        except:
            continue
branch = list(branch.values())[0]
table_encode(branch)
#table will be like
#{'a' :'0','b' : '01','c':'101'}
#Use the table to encode text
print("Encoding")
data = ''
for w in words:
    data += table[w] #change text to code

table[True] = table[EoFkey]
del table[EoFkey]
print("Preparing the file")

data += table[True]

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
