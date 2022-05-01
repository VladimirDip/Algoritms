def big_list_users(first_list, second_list):
    merge_lists = list(sorted(filter(lambda a: a != 0, (first_list + second_list))))
    return merge_lists


def main():
    first_list = list(map(int, input().split()))
    m_users_of_server_1 = int(input())
    k_len_user_list_2 = int(input())
    second_list = list(map(int, input().split()))

    res = big_list_users(first_list, second_list)
    print(res)


if __name__ == '__main__':
    main()


