def most_frequent_digits(input_string):
    digit_count = {}
    for char in input_string:
        digit = int(char)
        digit_count[digit] = digit_count.get(digit, 0) + 1

    top_three_digits = sorted(digit_count.items(), key=lambda x: (-x[1], x[0]))[:3]

    result = dict(sorted(top_three_digits))

    return result

input_string = input("Введите число: ")
output = most_frequent_digits(input_string)
print(output)
