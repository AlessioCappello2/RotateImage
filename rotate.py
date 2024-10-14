def rotate90(m, n):
    for i in range(n//2):
        for j in range(i, n-i-1):
            start = m[i][j]
            m[i][j] = m[n-j-1][i]
            m[n-j-1][i] = m[n-i-1][n-j-1]
            m[n-i-1][n-j-1] = m[j][n-i-1]
            m[j][n-i-1] = start

    return m

m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
n = 4
print(rotate90(m, n))
