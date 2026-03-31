#!/usr/bin/env python3


def mirror_matrix(matrix: list) -> list:
    return [row[::-1] for row in matrix]


def mirror_matrix_vertical(matrix: list) -> list:
    return matrix[::-1]


def rotate_90(matrix: list) -> list:
    n = len(matrix)
    return [[matrix[n - 1 - j][i] for j in range(n)] for i in range(n)]


def main() -> None:
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(rotate_90(matrix))


if __name__ == "__main__":
    main()
