# ile najmiej liter mozna dopisac do ciagu (string), zeby znalesc w nim caly alfabet

def lcs(string1, string2):
    m = len(string1)
    n = len(string2)
    c = [[0 for x in range(n)] for x in range(m)]
    for i in range(1, m):
        c[i][0] = 0
    for j in range(0, n):
        c[0][j] = 0
    for j in range(1, n):
        for i in range(1, m):
            if string1[i] == string2[j]:
                c[i][j] = c[i - 1][j - 1] + 1
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
            else:
                c[i][j] = c[i][j - 1]
    return c[m - 1][n - 1]


ABC = "abcdefghijklmnopqrstuvwxyz"
STRING = "pjatk"
print(lcs(ABC, STRING))
