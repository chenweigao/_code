from __future__ import print_function

import sys


def MatrixChainOrder(array):
    N = len(array)
    Matrix = [[0 for x in range(N)] for x in range(N)]
    Sol = [[0 for x in range(N)] for x in range(N)]
    for i in range(1, N):
        Matrix[i][i] = 0

    for ChainLength in range(2, N):
        for a in range(1, N-ChainLength+1):
            b = a+ChainLength-1

            Matrix[a][b] = sys.maxsize
            for c in range(a, b):
                cost = Matrix[a][c] + Matrix[c+1][b] + \
                    array[a-1] * array[c] * array[b]
                if cost < Matrix[a][b]:
                    Matrix[a][b] = cost
                    Sol[a][b] = c
    return Matrix, Sol


def PrintOptimalSolution(OptimalSolution, i, j):
    if i == j:
        print('A' + str(i), end=' ')
    else:
        print('(', end=' ')
        PrintOptimalSolution(OptimalSolution, i, OptimalSolution[i][j])
        PrintOptimalSolution(OptimalSolution, OptimalSolution[i][j]+1, j)
        print(')', end=' ')


def main():
    array = [30, 35, 15, 5, 10, 20, 25]
    n = len(array)
    Matrix, OptimalSolution = MatrixChainOrder(array)
    print("No. of Operation required: "+str((Matrix[1][n-1])))
    PrintOptimalSolution(OptimalSolution, 1, n-1)


if __name__ == '__main__':
    main()
