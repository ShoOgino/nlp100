def getNgramCharacter(str, n):
    items=[]
    for i in range(len(str)-(n-1)):
        items.append(str[i:i+n])
    return items

def main():
    input = ["paraparaparadise", "paragraph"]
    x = list(set(getNgramCharacter(input[0], 2)))
    y = list(set(getNgramCharacter(input[1], 2)))
    union = []
    product = []
    differenceXY = []
    differenceYX = []

    union=set(x+y)
    print(union)

    for xitem in x:
        for yitem in y:
            product.append([xitem,yitem])
    print(product)

    for xitem in x:
        if xitem in y:
            pass
        else:
            differenceXY.append(xitem)
    print(differenceXY)


    for yitem in y:
        if yitem in x:
            pass
        else:
            differenceYX.append(yitem)
    print(differenceYX)

if __name__ == '__main__':
    main()



