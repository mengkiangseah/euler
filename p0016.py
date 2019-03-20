def duplicate(number, power):
    for x in range(0, power - 1):
        carry = 0
        for y in range(0, len(number)):
            number[y] = number[y] + number[y] + carry
            carry = int(number[y]/10)
            number[y] = number[y]%10

        while carry != 0:
            number.append(carry%10)
            carry = int(carry/10)
        print(x+2, end = ": ")
        printnumber(number)
    return number

def printnumber(number):
    # print(number[::-1])
    for each in number[::-1]:
        print(each, end = "")
    print(" ")




def main():
    print(sum(duplicate([2], 1000)))


if __name__ == "__main__":
    main()
