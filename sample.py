def calculate_sum(numbers):
    sum = 0
    for i in range(len(numbers)):
        sum += numbers[i]
    return sum

# Test cases
test_cases = [
    [1, 2, 3],
    [4, 5, 6],
    [-1, 0, 1]
]

for test in test_cases:
    result = calculate_sum(test)
    print(result)
