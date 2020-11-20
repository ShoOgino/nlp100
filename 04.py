import re

input = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can"
indexes=[0, 4, 5, 6, 7, 8, 14, 15, 18]
words = []
ls=[]
tmp=""
map= {}

input = input.replace('.', '')
words = input.split(' ')

print(words)
for i, word in enumerate(words):
    print(word)
    m = re.search(word, input)
    if i in indexes:
        map[word[0]]=m.start()
    else: 
        map[word[:2]]=m.start()
print(map)