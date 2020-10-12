#Se importa librería MatPlotLib
import matplotlib.pyplot as plt

#Se declaran diccionario con sus respectivos datos, también un índice de posicionamiento para más adelante darle un uso en especifico 
valores = {'2015':181033, '2016':190169, '2017':197381, '2018':202039, '2019':206640}
indice = (0, 0.1, 0, 0, 0)

#Llamamos la función .pie para identificar tipo de grafica que en este caso es la de pastel, 
# se crea un ciclo for para recorrer el diccionario y se conviertan los datos en strings
plt.pie([float(x) for x in valores.keys()], labels=[str(i) for i in valores.values()],
#Se utiliza explode para utilizar el índice de posicionamiento del diccionario y resaltar una en especifico, determinamos cortono de la grafica, 
           explode=indice, autopct=None, wedgeprops={'edgecolor':'white'})
#.axis para la distribución igualitaria y .title para el titulo de esta grafica 
plt.axis('equal')
plt.title('Matriculas')
#se muestra la grafica con .show
plt.show()