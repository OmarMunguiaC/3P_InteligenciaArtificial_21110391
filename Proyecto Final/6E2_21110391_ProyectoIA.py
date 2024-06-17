
"""
Materia: Inteligencia Artificial
Profesor: Mauricio Alejandro Cabrera Arellano
Alumno: Omar Josue Munguia Camacho
Registro: 21110391
Grupo: 6E2
"""

"""
Unsupervised Machine Learning utilizando Scikit-Learn
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from sklearn.cluster import KMeans
from sklearn.cluster import MeanShift
from sklearn.datasets._samples_generator import make_blobs
style.use("ggplot")
ms = MeanShift()


"""
Flat Clustering: El Flat Clustering (tambien denominado Semi-unsupervised Machine Learning) tiene como peculiaridad de que
nosotros tenemos que colocar en número de clusters que deseamos, sin embargo la función decidira por si misma cuales puntos de
la gráfica seleccionar para separarlo en cada cluster.
En este caso, seleccionaremos puntos al azar dentro de una grafica x,y de manera manual
"""

x = [1, 5, 1.5, 8, 1, 9]    #Coordenadas x,y para puntos en la grafica
y = [2, 8, 1.8, 8, 0.6, 11]

plt.scatter(x,y)    #Muestra de los puntos de x,y
plt.show()

X = np.array([[1,2],[5,8],[1.5,1.8],[8,8],[1,0.6],[9,11]])  #Colocamos los puntos x,y en un array llamado "X"
kmeans = KMeans(n_clusters=2)   #Colocamos el número de clusters que deseamos
kmeans.fit(X)   #Colocamos la cantidad de clusters que deseamos en el array

centroids = kmeans.cluster_centers_ #Función para encontrar centroides dentro de los clusters creados
labels = kmeans.labels_ #Nombramiento de cada punto para los clusters
print(centroids)
print(labels)
colors = ["g.","r."]    #Ponemos colores a los puntos de cada clusters para separarlos

for i in range(len(X)): #Función para marcar cada punto dentro del cluster que fue decidido por la maquina
    print("Coordenada:", X[i], "Label:", labels[i])
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize = 10)

plt.scatter(centroids[:,0], centroids[:,1], marker = "x", s = 150, linewidths = 5, zorder = 10) #Grafica los centroides y los puntos con los colores de cada cluster
plt.show()


"""
Hierarchical Clustering: A diferencia del Flat Clustering, el Hierarchical Clustering calcula por sus propios algoritmos la cantidad
de clusters que se van a dividir, esto significa que no necesita ninguna acción externa por parte de un humano para decidir como separar
la información de cada cluster.
En este caso, utilizaremos la función "blob" para crear amalgamas de puntos dentro de un rango determinado
"""

centers = [[1,1],[5,5],[3,11]]  #Seleccionamos los puntos centrales donde se crearan los conjuntos
Z, _ = make_blobs(n_samples = 200, centers = centers, cluster_std = 1) #Se generaran un total de 200 puntos con una desviación estandar de 1 desde el punto central
plt.scatter(Z[:,0], Z[:,1]) #Mapeo de los puntos generados
plt.show()

ms.fit(Z) #Introducimos los puntos a la función MeanShift
labelsZ = ms.labels_    
cluster_centers = ms.cluster_centers_
n_clusters_ = len(np.unique(labelsZ)) 
colorsZ = 10*['r.','g.','c.','b.','k.','y.','m.']   #Seleccionamos colores para los clusters

print("Numero estimado de Clusters:", n_clusters_)
print("Centros de los Clusters:", cluster_centers)
print(colorsZ)
print(labelsZ)

for v in range(len(Z)): #Seleccionamos cada punto generado y lo separamos por clusters
    plt.plot(Z[v][0], Z[v][1], colorsZ[labelsZ[v]], markersize = 10)

plt.scatter(cluster_centers[:,0], cluster_centers[:,1], marker = "x", s = 150, linewidths = 5, zorder = 10) #Mapeamos los nuevos clusters junto con el centro aproximado calculado
plt.show()
