from collections import Counter


def find_person(all_persons):
    d = Counter(all_persons)
    return [k for k, v in d.items() if (v % 2) != 0]


def main():
    len_list_person = int(input())
    all_persons_list = list(map(int, input().split()))[:len_list_person]
    result = find_person(all_persons_list)
    print(result)


if __name__ == '__main__':
    main()