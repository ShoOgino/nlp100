input = ["パトカー", "タクシー"]
output = ""
for i in range(len(input[0])):
    for j, item in enumerate(input):
            output+=item[i]
print(output)