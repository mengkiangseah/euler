ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
powers = ["one", "ten", "hundred", "thousand"]

def numbertostring(number):
    if number == 0:
        return "zero"
    elif number < 0:
        return "negative"
    elif number < 20:
        return ones[number]
    elif number < 100:
        return tens[int(number/10)] + ones[number%10]
    elif number < 1000 and number%100 == 0:
        return ones[int(number/100)] + powers[2]
    elif number < 1000 and number%100 != 0:
        return ones[int(number/100)] + powers[2] + "and" + numbertostring(number%100)
    elif number == 1000:
        return ones[1] + powers[3]
    else:
        return ""




def main():
    count = 0
    for x in range(1, 1001):
        count = count + len(numbertostring(x))
    print(count)


if __name__ == "__main__":
    main()
