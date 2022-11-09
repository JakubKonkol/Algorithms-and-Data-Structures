#ile najmiej liter mozna dopisac do ciagu (string), zeby znalesc w nim caly alfabet

#ABC = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
STRING = "pjatk"
ABC = "abcdefghijklmnopqrstuvwxyz"

def LCS(string1, string2):
    m = len(string1)
    n = len(string2)
    C = [m+1, n+1]
    for i in range(0, m):
        C[i][0] = 0
    for j in range(0,n):
        C[0,j] = 0
    for i in range(1,m):
        for j in range(1, n):
            if(string1[i-1] == string2[j - 1] ):
                C[i,j] = C[i-1, j-1] +1
            else:
                C[i, j] = max(C[i, j-1], C[i-1, j])
    return C[m,n]

print(LCS(ABC, STRING))



