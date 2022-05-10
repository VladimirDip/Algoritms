def encryption(string: str, template):
    n = 0
    for i in range(len(string) - len(template) + 1):
        if sorted(template) == sorted(string[i:len(template) + i]):
            n += 1

    print(n)


if __name__ == '__main__':
    string = input()
    template = input()
    res = encryption(string, template)
    print(res)
