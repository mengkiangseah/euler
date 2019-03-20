def main():
    totalList = []
    newList = [1 for x in range(0, 21)]
    totalList.append(newList)

    for row in range(1, 21):
        newList = [1]
        for col in range(1, 21):
            newList.append(totalList[row - 1][col] + newList[col - 1])
        totalList.append(newList)

    # for numbers in totalList:
    #     for number in numbers:
    #         print("{0:11d}".format(number), end=" ")
    #     print("")
    print(totalList[20][20])



if __name__ == "__main__":
    main()
