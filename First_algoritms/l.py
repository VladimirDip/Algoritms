from itertools import zip_longest


def define_anagrams(first, second):
    li = list(zip_longest(first, second))

    for letter in li:

        if letter[0] != letter[1]:
            return letter[1]


def main():
    first_list = sorted(map(str, input()))
    second_list = sorted(map(str, input()))
    print(define_anagrams(first_list, second_list))


if __name__ == '__main__':
    main()
