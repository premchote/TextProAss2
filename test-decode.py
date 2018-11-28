from pickle import load

f = open('infile.bin','r+b') #open file
text2 = f.read() #read file
i = ["{0:08b}".format(t) for t in text2] #convert file to be string of binaray
data = ''.join(i) #join all list
f.close() #close file

pkl = open("infile-symbol-model.pkl","r+b")
the_dict = load(pkl)
#finding EOF
#EOF = the_dict[0]
index = data.find(the_dict[0],len(data)-len(the_dict[0]))
xdata = data[0:index]#delete bit after EOF
#sorted_key = sorted(the_dict,key= lambda m: len(the_dict[m]))
decode_table = {value:key for key,value in the_dict.items()} #Create a table for decode

B = '' #initial handle data
output = '' #initial output

for b in xdata:
    B += b
    try:
        decode = decode_table[B]
        if decode == 0:
            break
        output += decode
        B = '' #reinitial handle data
    except:
        continue
    
