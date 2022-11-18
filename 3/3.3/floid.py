N = 7
F = [[[None] * N for j in range(N)] for k in range(N + 1)]
W = """
0	11	7	5			12
11	0			13	8	14
7		0	15		10	
5		15	0		9	
	13			0	6	
	8	10	9	6	0	
12	14					0""".lstrip()
W = [line.split("\t") for line in W.splitlines()]
# $F^0_ij = W_ij$
F[0] = [[float("+inf") if x == "" else int(x) for x in line] for line in W]
for k in range(0, N):
    for i in range(0, N):
        for j in range(0, N):
            F[k + 1][i][j] = min(F[k][i][j], F[k][i][k] + F[k][k][j])
print(*F[N], sep="\n")
