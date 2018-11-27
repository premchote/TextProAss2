import re

text = "aaaaabbbbbccccccccccddddddddddddddddddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffffffffffffffffffffgggggggggg"
term = {} #initial the term vector
for t in set(text):
    term[t] = [i for i, x in enumerate(text) if x == t]
branch = {} #initial branch
freq = {key:len(term[key]) for key in term.keys()} #Counting each character
total_freq = sum(freq.values())
i=0 #initial number of brach
new_freq = freq #For making Huffman tree
table = {} #Initial encoding table

while True:
    print(branch)
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
for t in set(text):
    text = text.replace(t,table[t])
    



