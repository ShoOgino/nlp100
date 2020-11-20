input = "パタトクカシーー"
output = ""
for i in range(len(input)):
    if i%2==1:
        output+=input[i]
print(output)