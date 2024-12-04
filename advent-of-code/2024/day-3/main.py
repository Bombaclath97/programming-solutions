import re

command_pattern = r"(do\(\)|don't\(\)|mul\(\d+,\d+\))" 
pattern = r"mul\((\d+),(\d+)\)"

total = 0

enable_mul = True
with open("input", "r") as file:
    for line in file:
        
        matches = re.finditer(f"{command_pattern}", line)
        for match in matches: 
            token = match.group()
            if token == "do()":
                enable_mul = True
            elif token == "don't()":
                enable_mul = False
            elif enable_mul and token.startswith("mul"):
                numbers = re.match(pattern, token)
                num1, num2 = int(numbers.group(1)), int(numbers.group(2))
                total += num1 * num2

print(total)