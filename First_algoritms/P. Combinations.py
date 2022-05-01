import itertools

CHARACTER = {
    2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl',
    6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'
}


def combinations(number_list):
    list_of_letters = [v for k, v in CHARACTER.items() if k in number_list]
    combination = list(map(''.join, itertools.product(*list_of_letters)))
    return combination


def main():
    number = list(map(int, input().split()))
    res = combinations(number)
    print(res)


if __name__ == '__main__':
    main()
