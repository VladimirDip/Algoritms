def form_of_list(len_form, form, key):
    form = int(form[:len_form])
    new_form = ' '.join(str(form + key))
    return new_form


def main():
    len_form = int(input())
    form = input().replace(' ', '')
    key = int(input())
    new_form = form_of_list(len_form, form, key)
    print(new_form)


if __name__ == '__main__':
    main()