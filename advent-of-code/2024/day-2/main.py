def safe_distance(a, b, ascending):
    if ascending:
        return (b - a) <= 3 and (b - a) >= 1
    else:
        return (a - b) <= 3 and (a - b) >= 1

with open("input", "r") as file :

    safe = 0

    for line in file:
        line = line.strip()
        numbers = line.split()

        numbers = [int(num) for num in numbers]

        print(numbers)

        ascending = True
        if numbers[0] > numbers[1]:
            ascending = False 

        is_safe = True
        unsafe = 2
        # check safeness
        for i in range(len(numbers) - 1):
            if (numbers[i] == numbers[i + 1]) or (not safe_distance(numbers[i], numbers[i + 1], ascending)):
                unsafe -= 1
            if unsafe == 0:
                is_safe = False
                break
        if is_safe:
            safe += 1
    print(safe)

