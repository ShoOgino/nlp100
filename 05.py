def getNgramCharacter(str, n):
    items=[]
    for i in range(len(str)-(n-1)):
        items.append(str[i:i+n])
    return items

def getNgramWord(str, n):
    words = str.split(" ")
    items = []
    for i in range(len(words) - (n-1)):
        items.append([words[i], words[i+1]])
    return items

def main():
    input = "I am an NLPer"
    items = getNgramWord(input, 2)
    print(items)

if __name__ == '__main__':
    main()