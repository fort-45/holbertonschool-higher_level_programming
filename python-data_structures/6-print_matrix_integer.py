#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if not matrix or matrix == [[]]:
        if matrix == [[]]:
            return
    for row in matrix:
        # 3. Check for empty rows
        if not row:
            print()
            continue
        # 4. Iterate through each element (integer) in the current row
        for i in range(len(row)):
            if i == len(row) - 1:
                print("{:d}".format(row[i]))
            else:
                print("{:d} ".format(row[i]), end="")
