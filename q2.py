import numpy as np
import matplotlib.pyplot as plt
import math

table = [9, 12, 10, 8, 11, 13, 10, 15, 9, 7,
14, 12, 9, 7, 15, 6, 4, 16, 18, 9,
19, 10, 20, 13, 8, 7, 17, 15, 14, 20,
21, 19, 22, 6, 5, 12, 15, 23, 19, 24,
15, 10, 12, 9, 15, 24 ,6, 24 ,13 ,12]

a = [[4,8],[8,12],[12,16],[16,20],[20,24]]

print('Questão 2:')

#Amplitude
AT = max(table) - min(table) #total
h = AT/5

tOrdenado = sorted(table)
#print("Amplitude", h)
#print(tOrdenado)

#Frequência --- fi
fi = [8, 12, 16, 6, 8]

#Ponto Médio --- xi
xi = []
for i in range(len(a)):
    aux = (a[i][0]+a[i][1])/2
    xi.append(aux)

#Pm * Fr --- fi*xi
mult = []
for i in range (len(xi)):
    aux = xi[i]*fi[i]
    mult.append(aux)
#print(mult)

#Média Amostral
xBarra = sum(mult)/sum(fi)
print("Média Amostral: ", xBarra)

#Frequencia simples acumulada
Fi = []
aux = 0
for i in range(len(fi)):
    aux += fi[i] 
    Fi.append(aux)

#Frequência Relativa
fri = []
aux = 0
for i in range(len(fi)):
    aux = fi[i]/sum(fi) 
    fri.append(aux)

#Frequência percentual
fp = []
aux = 0
for i in range(len(fi)):
    aux = fri[i]*100 
    fp.append(aux)

#Frequência Relativa Acumulada
Fri = []
aux = 0
for i in range(len(fi)):
    aux += fri[i] 
    Fri.append(aux)

#Frequência percentual acumulada
FP = []
aux = 0
for i in range(len(fi)):
    aux += fp[i] 
    FP.append(aux)

#Mediano
cm = len(table)/2 #classe mediana
#print(cm)

#A classe em que cm está é 12 |— 16
id = 2
Me =  ((cm - Fi[id-1])*h/fi[id])+min(a[id])
print("Mediano: ", Me)


#Modal
#A classe com maior frequência é 12 |— 16
id = fi.index(max(fi)) 

d1 = fi[id]-fi[id-1]
d2 = fi[id]-fi[id+1]

Mo = ((d1/(d1+d2))*h)+min(a[2])
print('Modal:' , round(Mo, 2))


#Construção da tabela
plt.figure()
ax=plt.gca()
nomes = ['Coeficiente de mortalidade', 'Frequência (fi)', 'Ponto Médio (xi)', 'Frequência Acumulada (Fi)', 'Fr. Relativa (fri)', 'Fr. percentual (fi%)', 'Fr. Relativa Acumulada', 'Fr. Percentual Acumulada']
valores = [['4 |— 8', 8, xi[0], Fi[0], fri[0], fp[0], Fri[0], FP[0]], ['8 |— 12', 12, xi[1], Fi[1],  fri[1], fp[1], Fri[1], FP[1]], ['12 |— 16', 16, xi[2], Fi[2],  fri[2], fp[2], Fri[2], FP[2]], [ '16 |— 20', 6, xi[3], Fi[3],  fri[3], fp[3], Fri[3], FP[3]], ['20 |— 24', 8, xi[4], Fi[4],  fri[4], fp[4], Fri[4], FP[4]], ['Total', sum(fi), '—', '—',  sum(fri), sum(fp), '—','—'] ]

table = plt.table(cellText=valores,
                  colLabels=nomes,
                  loc='center')
table.auto_set_font_size(False)
table.set_fontsize(7)
plt.axis('off')


#Criando o histograma
end = []
for id, itens in enumerate(xi):
    v = fi[id]
    for t in range(v):
        end.append(itens)
#print(end)
plt.figure(figsize=(5, 2))
plt.hist(end, bins=range(4, 28, 4), color = 'navy') 
plt.title('Histograma | Polígono de Frequências')
plt.xlabel('Mortalidade Geral')
plt.ylabel('Frequência')


#Criando o polígono de frequências
plt.plot(xi,fi,'ro-')

# zip joins x and y coordinates in pairs
for x,y in zip(xi,fi):

    label = "{:.0f}".format(y)

    plt.annotate(label, # this is the text
                 (x,y), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,10), # distance from text to points (x,y)
                 ha='center') # horizontal alignment can be left, right or center

plt.xticks(np.arange(4, 28, 4 ))
plt.yticks(np.arange(0,20,2))


plt.show()
