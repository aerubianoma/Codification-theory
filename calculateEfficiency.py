import math

# De 1 a 3 son puntos del taller
# 4 es el punto 8 del parcial

p1 = [0.01,0.09,0.09,0.81]
p2 = [0.001,0.009,0.009,0.009,0.081,0.081,0.081,0.729]
p3 = [0.0001,0.0009,0.0009,0.0009,0.0009,0.0081,0.0081,0.0081,0.0081,0.0081,0.0081,0.0729,0.0729,0.0729,0.0729,0.6561]
p4 = [0.028,0.056,0.083,0.111,0.139,0.167,0.139,0.111,0.083,0.056,0.028]
probabilities = [p1,p2,p3,p4]
results1 = [0,0,0,0]
c = 0
for probability in probabilities:
    for p in probability:
        results1[c] += p*math.log(p,2)
    results1[c] = -1*results1[c]
    c+=1
        
h1 = [3,3,2,1]
h2 = [5,5,5,5,4,3,3,1]
h3 = [10,10,9,9,9,7,6,7,7,7,7,4,3,3,3,1]
h4 = [5,4,4,4,3,2,3,3,4,4,5]
hlen = [h1,h2,h3,h4]
results2 = [0,0,0,0]
for i in range(len(hlen)):
    for j in range(len(hlen[i])):
        results2[i] += probabilities[i][j]*hlen[i][j]

s1 = [2,2,2,2]
s2 = [2,2,3,3,4,4,4,4]
s3 = [2,2,3,3,4,4,5,5,6,6,7,7,8,8,8,8]
s4 = [6,5,4,3,3,2,3,3,4,4,6]
slen = [s1,s2,s3,s4]
results3 = [0,0,0,0]
for i in range(len(slen)):
    for j in range(len(slen[i])):
        results3[i] += probabilities[i][j]*slen[i][j]

for i in range(len(results1)):
    print('Resultado de la eficacia para S'+str(i+2)+':')
    print('entropia')
    print(results1[i])
    print('longitud promedio Huffman')
    print(results2[i])
    print('Eficiencia Huffman')
    print(results1[i]/results2[i])
    print('longitud promedio Shanon-Fano')
    print(results3[i])
    print('Eficiencia Shanon-Fano')
    print(results1[i]/results3[i])
