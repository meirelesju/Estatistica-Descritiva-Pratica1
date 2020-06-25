import matplotlib.pyplot as plt
import math

display = ["80 |— 100", "100 |— 120", "120 |— 140", "140 |— 160", "160 |— 180", "180 |— 200"]
a = [[80 ,100], [100, 120], [120, 140], [140, 160], [160, 180], [180, 200]]
fi = [30,80,40,10,4,6]
print('Questão 1:')

#Ponto Médio --- xi
xi = []
for i in range(len(a)):
    aux = (a[i][0]+a[i][1])/2
    xi.append(aux)

#Pm * Fr --- fi*xi
mult = []
for i in range(len(xi)):
    aux = xi[i]*fi[i]
    mult.append(aux)
#print(mult)

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

#Média Amostral
xBarra = sum(mult)/sum(fi)
print('Média: ', round(xBarra, 3))

#Desvio Padrão
#(xi - x̄)
sub = [] 
for i in range(len(xi)):
    aux = xi[i] - xBarra
    sub.append(aux)

# Σ fi*(xi - x̄)^2 
somatorio = 0
aux = 0
for i in range(len(xi)):
    aux = fi[i] * (math.pow(sub[i], 2))
    somatorio += aux
    #print(aux)

# √(somatório/n-1)
div = somatorio/(sum(fi)-1)
raiz = math.pow(div, 1/2) 
print('Desvio Padrão:', round(raiz, 3))

#Coeficiente de variação
cv = (raiz/xBarra)*100
print ('Coeficiente de Variação: ', round(cv, 3),'%')

#Percentagem de mulheres que têm pressão igual ou maior que 120mm
p1 = 100-FP[1]
print('Mulheres que têm pressão igual ou maior que 120mm: ', round(p1, 2), '%')

#Percentagem de mulheres que têm pressão igual ou maior que 100mm
p2 = 100-FP[0]
print('Mulheres que têm pressão igual ou maior que 100mm: ', round(p2, 2), '%')

#Construção do gráfico de barras
plt.bar(display,fi, color= "green")
plt.xticks(display)
plt.ylabel('No. De Mulheres')
plt.xlabel('Pressão Siatólica')

#Construção do Gráfico de Pizza
fig1, ax1 = plt.subplots(figsize=(6, 6))
wp = { 'linewidth' : 1, 'edgecolor' : "black" } 

explode = (0.1, 0.1, 0, 0.4, 0.4, 0.4)
wedges = ax1.pie(fi, explode=explode, autopct='%1.1f%%', shadow=True, startangle=90, colors= ['darkred', 'salmon', 'coral', 'peru', 'goldenrod', 'palegoldenrod'])
plt.legend(labels=display, fontsize=10)
ax1.set_title("Gráfico de Pizza")
ax1.axis('equal')
plt.rcParams['font.size'] = 14

#Construção do histograma
end = []
for id, itens in enumerate(xi):
    v = fi[id]
    for t in range(v):
        end.append(itens)
#print(end)
plt.figure(figsize=(5, 2))
plt.hist(end, bins=range(80, 220, 20)) 
plt.title('Histograma')
plt.xlabel('No. De Mulheres (frequência)')
plt.ylabel('Pressão Siatólica(mm de Hg)')


#Construção da tabela
plt.figure()
ax=plt.gca()
nomes = ['Pressão Siatólica', 'No. De Mulheres', 'Ponto Médio (xi)', 'Frequência Acumulada (Fi)', 'Fr. Relativa (fri)', 'Fr. percentual (fi%)', 'Fr. Relativa Acumulada', 'Fr. Percentual Acumulada']
valores = [['80 |— 100', 30, xi[0],  Fi[0], round(fri[0],3), round(fp[0],3), round( Fri[0],3), round(FP[0],3)], ['100 |— 120', 80, xi[1],  Fi[1], round( fri[1],3), round(fp[1],3),round( Fri[1],3), round(FP[1],3)], ['120 |— 140', 40, xi[2],  Fi[2], round(fri[2],3), round(fp[2],3), round(Fri[2],3), round(FP[2],3)], ['140 |— 160', 10, xi[3],  Fi[3],  round(fri[3],3), round(fp[3],3), round(Fri[3],3), round(FP[3],3)], ['160 |— 180', 4, xi[4],  Fi[4],  round(fri[4],3), round(fp[4],3), round(Fri[4],3), round(FP[4],3)], ['180 |— 200', 6, xi[5],  Fi[5],  round(fri[5],3), round(fp[5],3), round(Fri[5],3), round(FP[5],3)], ['Total', sum(fi) , '—', '—',  sum(fri), sum(fp), '—','—'] ]

table = plt.table(cellText=valores,
                  colLabels=nomes,
                  loc='center')
table.auto_set_font_size(False)
table.set_fontsize(7)
plt.axis('off')

plt.show()




