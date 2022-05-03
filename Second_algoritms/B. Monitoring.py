# def transposed_matrix(matrix):
#     transposed_matrix_list = []
#
#     for n1 in range(len(matrix[0])):
#         transposed_row = []
#         for row in matrix:
#             transposed_row.append(row[n1])
#         transposed_matrix_list.append(transposed_row)
#
#     return transposed_matrix_list
#
#
# def main():
#     count_column = int(input())
#     len_row_matrix = int(input())
#     matrix = []
#     for _ in range(count_column):
#         row_matrix = list(map(int, input().split()))
#         matrix.append(row_matrix)
#
#     res = transposed_matrix(matrix)
#
#     for row in res:
#         print(row)


def main():
    rows = int(input())
    columns = int(input())

    matrix = [list(map(int, input().split())) for _ in range(rows)]
    transport_matrix = zip(*matrix)

    for row in transport_matrix:
        print(*row)


if __name__ == '__main__':
    main()
