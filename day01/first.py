import re

result = sum([int(''.join([re.sub("\D", "", line)[0], re.sub("\D", "", line)[-1]])) for line in open("data", "r").readlines()])

print(result)
