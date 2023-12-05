import re


def read_file_by_line(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines


def extract_digit(line):
    extracted_digit = re.findall(r'\d+', line)
    join_digit = ''.join(extracted_digit)
    return int(join_digit[0] + join_digit[-1])


def detect_letter_digit(input_lines):
    spelled_digit_dict = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    new_input_lines = []
    for line in input_lines:
        for key, value in spelled_digit_dict.items():
            line = line.replace(key, key + value + key)
        new_input_lines.append(line)
    return new_input_lines


#get the input
input_lines = read_file_by_line('Day1/input.txt')

#replace spelled digit into digits
new_input_lines = detect_letter_digit(input_lines)

#extract the digits
digits = [extract_digit(line) for line in new_input_lines]
print(sum(digits))
