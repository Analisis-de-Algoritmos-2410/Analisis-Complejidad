# Reto 1 - Analisis de complejidad - Analisis de algoritmos

Para ver la nota en HackMD para poder visualizar los _underbraces_ bien, este es el [enlace](https://hackmd.io/@Galindooo/S1FXjaD9T).

## Busqueda binaria en el ID

Teniendo en cuenta que se puede buscar en una lista ordenada los ID's de los registros, se puede analizar la complejidad algoritmica de la busqueda binaria en dichos ID's.

Sea $n$ la cantidad de registros existentes en el sistema, la premisa principal dela busqueda binaria es calcular un punto medio en la lista para verificar si el ID que se busca es mayor o menor que ese punto medio, en tal caso, al escoger alguna de las dos mitades se disminuye el problema a un tamaño $n/2$.

Teniendo eso en cuenta, se puede denominar que por cada iteración o elección de mitades se disminuye el problema a $\frac{n}{2^i}$ donde $i$ es el numero de la _elección_. 

$$\underbrace{1, 2, 3, }_{n/2}\underbrace{4}_{mid},\underbrace{5, 6, 7}_{n/2}$$

Por cada elección se hace un trabajo constante $c$, entonces se puede determinar la complejidad de la siguiente manera.

Para encontrar el numero de _elecciones_ necesarias para reducir $n = 1$ se puede:

$$\begin{align}
    \frac{n}{2^i} &= 1 \\
    n &= 2^i \\
    \log_2n &= \log_22^i \\
    \log_2n &= i\log_22 \\
    \log_2n &= i
\end{align}$$

De esta manera sabemos que va a tomar un maximo de $\log_2n$ _elecciones_ para encontrar el ID indicado. Teniendo en cuenta que el trabajo en cada _elección_ es $c$, entonces se puede afirmar que:

$$\sum_{i=0}^{\log_2n}c = \log_2n\cdot c = \Theta(\log n)$$

## Busqueda lineal en el nombre

Para realizar la busqueda lineal es necesario ver que en el peor de los casos, el nombre no existe en el registro de los censos. Con base en esto, se puede afirmar que se va a recorrer todas las posiciones del arreglo buscando el nombre.

Siendo $n$ el tamaño del arreglo, la complejidad de dicha busqueda lineal es de $O(n)$. En el peor caso se puede dar la siguiente expresión tomando en cuenta que por cada posición del arreglo se asume que se hace un trabajo constante $c$.

$$\sum_{i=0}^nc = n \cdot c = O(n)$$


## Comparacion de tiempos de ejecucion

En función de comparar los tiempos de ejecución de las dos busquedas, se plantea una grafica teniendo en cuenta varios tamaños de los arreglos generados para el censo, siendo $n$ el tamaño de los arreglos, se generan $1000$ arreglos los cuales van aumentando progresivamente su tamaño.

Se ejecutan las busquedas en los arreglos con un elemento random de los mismos, los resultados se muestran de la siguiente manera:

![image](https://hackmd.io/_uploads/HkYka1q5T.png)

Se puede visualizar los tiempos registrados para la busqueda lineal y binaria en tal caso, viendo como se cumple el comportamiento asintotico de la busqueda lineal $O(n)$ teniendo una forma lineal en cuanto al tiempo de ejecución.

En contraste, se puede ver como la busqueda binaria no supera el segundo en el tiempo de ejecución, cumpliendo así el comportamiento asintotico de la busqueda binaria $\Theta(\log n)$ tomando en cuenta que $\log_2(1000) \approx 10$. En lugar de hacer $1000$ operaciones aproximadamente, se hacen $10$ operaciones.