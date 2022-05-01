
def polidrom(string):
    string2 = string[::-1]
    if string2 == string:
        return True
    else:
        return False


def main():
    string = ''.join(
        letter for letter in str(input()) if letter.isalpha()
    ).lower()
    print(string)
    result = polidrom(string)
    print(result)


if __name__ == '__main__':
    main()