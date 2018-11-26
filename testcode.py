import re

text = "asdf adsg Asss"
term = {}
for t in text:
    if t in term.keys():
          continue
    else:
          term[t] = [i for i, x in enumerate(text) if x == t]

term_vector = {key:len(term[key]) for key in term.keys()} #Counting each character
