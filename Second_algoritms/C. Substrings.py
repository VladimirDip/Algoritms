# def len_not_doublicate_in_string(string):
#     minimum_len_string = 0
#     letter_wihout_doublicate = []
#
#     for letter in string:
#         if letter not in letter_wihout_doublicate:
#             letter_wihout_doublicate.append(letter)
#         else:
#             if len(letter_wihout_doublicate) > minimum_len_string:
#                 minimum_len_string = len(letter_wihout_doublicate)
#             letter_wihout_doublicate.clear()
#             letter_wihout_doublicate.append(letter)
#
#     if len(letter_wihout_doublicate) > minimum_len_string:
#         minimum_len_string = len(letter_wihout_doublicate)
#     return minimum_len_string
#
#
# def main():
#     main_string = input()
#     res = len_not_doublicate_in_string(main_string)
#     print(res)


def main(string):
    temp_str = []
    result = 0

    for _, letter in enumerate(string, start=1):

        if letter not in temp_str:
            temp_str.append(letter)

        else:
            index = temp_str.index(letter)
            temp_str = temp_str[index + 1:] + list(letter)

        if len(temp_str) > result:
            result = len(temp_str)

    return result


if __name__ == '__main__':
    t = input()
    print(main(t))
