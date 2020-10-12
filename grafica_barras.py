#Se importa la librería Matplotlib
import matplotlib.pyplot as plt

#Se declara el diccionario con sus datos correspondientes 
valores = {'2015':181033, '2016':190169, '2017':197381, '2018':202039, '2019':206640}

 #Se determinan los títulos, los valores y el color de la grafica      
plt.bar(valores.keys(), valores.values(), color='lightgreen')
plt.title('Matricula')      
plt.xlabel('Año')          
plt.ylabel('Matricula')

#Con un ciclo for se recorre el diccionario para imprimir los datos en la gráfica,
#  se centran los datos en cada barra y se muestra la grafica con .show
for x,y in zip(valores.keys(), valores.values()): 
    plt.text(x,y, str(y), horizontalalignment='center')
 
#Funcion para mostrar la grafica
plt.show()