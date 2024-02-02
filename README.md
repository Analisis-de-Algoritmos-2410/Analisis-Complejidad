# Reto 1 - Analisis de complejidad - Analisis de algoritmos

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

