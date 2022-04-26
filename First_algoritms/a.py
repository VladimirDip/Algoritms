def solve_qadratic_equation(a, x, b, c):
    y = a * x ** 2 + b * x + c
    return y


if __name__ == '__main__':
    variables = list(map(int, input().split()))
    result = solve_qadratic_equation(*variables)
    print(result)