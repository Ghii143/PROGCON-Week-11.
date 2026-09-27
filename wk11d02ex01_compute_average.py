def toFixed(value, digits):
    return "%.*f" % (digits, value)

def average(arr, count):
    accum = 0
    sentence = "The average of"
    for coun in range(0, -1 + 1, 1):
        print("Input the value of the " + str(coun + 1) + str(ending(coun + 1)) + "number.")
        arr[coun] = float(input())
        accum = accum + arr[coun]
        if coun == count - 1:
            sentence = sentence + "and" + str(arr[coun]) + ""
        else:
            sentence = sentence + str(arr[coun]) + ","
    sentence = sentence + "is" + toFixed(accum / coun,2) + "."
    print(sentence)

# Main
numbers = [0] * (4)

print("Hello there! This program displays the average of the numbers of your output.")
print("How many numbers do you need the program to average?")
print("(Note the average will be rounded up to 2 decimal points.)")
num = int(input())
total = 0
count = 0
for i in range(0, len(numbers) - 1 + 1, 1):
    print("Input value of the " + str(i + 1) + "number")
    numbers[i] = int(input())
for i in range(0, len(numbers) - 1 + 1, 1):
    num = numbers[i]
    total = total + num
    count = count + 1
    if count == 0:
        print(0.0)
    else:
        average = float(total) / count
print(average)

