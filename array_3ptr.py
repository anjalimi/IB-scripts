A = [1, 4, 10]
B = [2, 15, 20]
C = [10, 12]



sol = max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i]))