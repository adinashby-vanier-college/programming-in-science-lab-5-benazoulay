# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    result = ''
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                result += '*'
            else:
                result += ' '
        result += '\n'
    return result.strip()

# 1
# 12
# 123
# 1234
def number_pattern(n):
    result = ''
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            result += str(j)
        result += '\n'
    return result.strip()

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    return (n * (n + 1)) // 2

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    result = ''
    for i in range(1, n + 1):
        for j in range(1, n - i + 1):
            result += ''
        
    return centered_star_pyramid(n)