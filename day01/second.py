import re


digit_map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

with open("data", "r") as f:
    lines = f.read().splitlines()

rgx_not_digit = re.compile("\D")

def replace_written_digits(line):
    for key in digit_map.keys():
        line = line.replace(key, f"{key}{digit_map[key]}{key}")
    return line

def get_first_and_last_digit(line):
    only_digits = rgx_not_digit.sub("", line)
    return f"{only_digits[0]}{only_digits[-1]}"

def main():
    result = sum([int(get_first_and_last_digit(replace_written_digits(line))) for line in lines])
    return result

if __name__=='__main__':
    print(main())
