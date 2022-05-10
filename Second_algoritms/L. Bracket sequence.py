def is_correct_bracket_seq(seq):

    # First solution

    # items = []
    # is_good = True
    # for bracket in seq:
    #     if bracket in '[{(':
    #         items.append(bracket)
    #     elif bracket in '])}':
    #         if len(items) == 0:
    #             is_good = False
    #             break
    #
    #         open_bracket = items.pop()
    #         if open_bracket == '(' and bracket == ')':
    #             continue
    #         elif open_bracket == '[' and bracket == ']':
    #             continue
    #         elif open_bracket == '{' and bracket == '}':
    #             continue
    #         is_good = False
    #         break
    #
    # if is_good and len(items) == 0:
    #     return True
    #
    # return False

# Second solution

    while ('[]' in seq) or ('()' in seq) or ('{}' in seq):
        seq = seq.replace('[]', '')
        seq = seq.replace('()', '')
        seq = seq.replace('{}', '')
    return not bool(seq)


def main():
    seq = input()
    res = is_correct_bracket_seq(seq)
    print(res)


if __name__ == '__main__':
    main()
