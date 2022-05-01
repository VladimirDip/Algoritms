def delete_zero(numbers):
    new_list = list(number for number in numbers if number != 0)
    return new_list


if __name__ == '__main__':
    k = int(input())
    numbers = list(map(int, input().split()))[:k]
    main_def = delete_zero(numbers)
    print(main_def)