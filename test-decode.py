from pickle import load

f = open('infile.bin','r+b') #open file
text2 = f.read() #read file
i = ["{0:08b}".format(t) for t in text2] #convert file to be string of binaray
data = ''.join(i) #join all list
f.close() #close file

pkl = open("infile-symbol-model.pkl","r+b")
the_dict = load(pkl)

decode_table = {value:key for key,value in the_dict.items()} #Create a table for decode

B = '' #initial handle data
output = '' #initial output

for b in data:
    B += b
    try:
        decode = decode_table[B]
        if decode == True:
            break
        output += decode
        B = '' #reinitial handle data
    except:
        continue
    
print(output)
