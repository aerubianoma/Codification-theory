# punto 1
suma = [[0,1,2,3],[1,0,3,2],[2,3,0,1],[3,2,1,0]]
producto =  [[0,0,0,0],[0,1,2,3],[0,2,3,1],[0,3,1,2]]

x1 = "1213211"
x2 = "2111321"
x3 = "3322111"

def sumar(a,b):
    result = ""
    for i in range(7):
        result += str(suma[int(a[i])][int(b[i])])
    return result

def multiplicar(x,y):
    result = ""
    for i in range(7):
        result += str(producto[x][int(y[i])])
    return result

results = []
counts = []
for i in range(4):
    for j in range(4):
        for k in range(4):
            results.append(sumar(sumar(multiplicar(i,x1),multiplicar(j,x2)),multiplicar(k,x3)))
print(results)
print(len(results))

for i in results:
    counts.append(i.count("0"))

print(counts)

# punto 5

import math

def condicionProbabilidad(n,k):
    d = abs((-1/n)*(k*math.log2(0.2)+(n-k)*math.log2(0.8))-0.72)
    return d

for n in range(1,1000):
    prob = 0
    for k in range(n+1):
        if condicionProbabilidad(n,k) <= 0.05:
            prob += pow(0.2,k)*pow(0.8,n-k)*math.comb(n,k)
    if prob >= 0.95:
        print(n)
        break
            