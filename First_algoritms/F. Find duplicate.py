def double_number(numbers):
    duplicate_list = set(
        [number for number in numbers if numbers.count(number) > 1]
    )
    return duplicate_list


def main():
    k = int(input())
    numbers = list(map(int, input().split()))[:k]
    duplicate = double_number(numbers)
    print(*duplicate)


if __name__ == "__main__":
    main()