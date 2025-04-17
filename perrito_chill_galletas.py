# resuleve: https://dmoj.uclv.edu.cu/problem/perritocaramelos
# por: lambdacreature

n = int(input())
C = []
for i in range(n):
    pair = tuple(map(int, input().split()))
    C.append((i, pair))

C_copy = [u for u in C]
# ordena por la x de cada par
C_copy.sort(key=lambda entry: entry[1][0])
by_X = C_copy

# mapea a cada indice de caramelo a su indice correspondiente en
# la secuencia ordenada por x
to_X = [0 for _ in range(n)]
for x_index, entry in enumerate(by_X):
    c_index, pair = entry
    to_X[c_index] = x_index

sol = [-1 for _ in range(n)]
def optimal(c_index):
    '''
    Toma un indice de una galleta y retorna la cantidad de 
    galletas optimas que se pueden comer empezando por esta
    '''

    global sol

    if sol[c_index] != -1:
        return sol[c_index]
    
    # the spice
    opt = 0
    X_pos = to_X[c_index]
    _, pair = C[c_index]
    for i in range(X_pos):
        # by_X[i] tiene un x menor que la
        # galleta que se esta considerando
        i_c_index, i_pair = by_X[i] 
        if i_pair[1] > pair[1]: continue
        optimal(i_c_index)
        opt = max(opt, sol[i_c_index])

    sol[c_index] = opt + 1
    return sol[c_index]

for i in range(n):
    optimal(i)

print(max(sol))