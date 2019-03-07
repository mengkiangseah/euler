
def checkPytho(sides):
    squareSides = sum([x*x for x in sides if x != max(sides)])
    if squareSides == max(sides) * max(sides):
        return True
    else:
        return False


def main():
    found = False
    for a in reversed(range(1, 999)):
        remainder = 1000 - a
        for b in range(1, remainder):
            c = remainder - b
            if checkPytho([a, b, c]):
                break
        if checkPytho([a, b, c]):
            break
    print([a, b, c])
    print(a * b * c)



if __name__ == "__main__":
    main()
