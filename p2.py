def main():
    theSum = 0
    valueOne = 1
    valueTwo = 1
    while valueTwo < 4000000:
        # New value
        valueTemp = valueOne + valueTwo
        if valueTemp%2 == 0:
            theSum = theSum + valueTemp
        # Update
        valueOne = valueTwo
        valueTwo = valueTemp
    print(theSum)

if __name__ == "__main__":
    main()
