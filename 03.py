input = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics"
words = []
ls=[]
tmp=""
for i in range(len(input)):
    if input[i]==" ":
        words.append(tmp)
        ls.append(len(tmp))
        tmp=""
    else:
        tmp+=input[i]
print(ls)