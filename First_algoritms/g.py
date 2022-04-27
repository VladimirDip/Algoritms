""" First solution"""


# def anagramm(string1, string2):
#     if len(string1) == len(string2):
#         for letter in string1:
#             if letter in string2:
#                 continue
#             else:
#                 return False
#         return True
#     return False

# def main():
#     string1 = input()
#     string2 = input()
#     print(anagramm(string1, string2))

""" Second solution"""


def annagramm(word1, word2):
    if word1 == word2:
        return True
    else:
        return False


def main():
    word1 = ''.join(sorted(list(input())))
    word2 = ''.join(sorted(list(input())))
    results = annagramm(word1, word2)
    print(results)


if __name__ == '__main__':
    main()


