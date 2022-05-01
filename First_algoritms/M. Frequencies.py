def change_string_to_list(string):
    string = list(map(str, string))
    return string


def change_list_to_string(list):
    list = ''.join(list)
    return list


def sort_list(list):
    new_string_to_list = change_string_to_list(list)
    new_string_to_list = sorted(new_string_to_list)
    new_list_to_string = change_list_to_string(new_string_to_list)
    return new_list_to_string


def main():
    new_string = input()
    res = sort_list(new_string)
    print(res)


if __name__ == '__main__':
    main()
