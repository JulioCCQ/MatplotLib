import matplotlib.pyplot as plt

#Diccionario
Valores = {'2015':181033, '2016':190169, '2017':197381, '2018':202039, '2019':202640}

#Se declaran los valores del diccionario y se insertan titulos
plt.plot(Valores.keys(), Valores.values(), marker='.')
plt.title('Matricula')      
plt.xlabel('Año')          
plt.ylabel('Matricula')

#se recorre el diccionario con un ciclo for para imprimirlos
for x,y in zip(Valores.keys(), Valores.values()): 
 plt.text(x, y, str(y)) #Se imprimen los valores Y en cada punto

plt.show()