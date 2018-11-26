import re

Testtext  = open('mobydick.txt','r')
Testtext = Testtext.read()
set_word = Testtext.split() #Delete line breaks
print(len(set_word))
##Testtext_sentense = [line.split('.') for line in Testtext_line] #Split sentense
##line = 0
##Testtext_word = {}
##for sentense in Testtext_sentense:
##    Testtext_word[line] = [word.split(' ') for word in sentense]
##    line += 1
