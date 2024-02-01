def busqueda_binaria(inf, sup, arr, target):
    if inf > sup:
        return -1
    else:
        medio = inf + (sup - inf) // 2
        if arr[medio].id == target:
            return medio
        elif arr[medio].id > target:
            return busqueda_binaria(inf, medio - 1, arr, target)
        else:
            return busqueda_binaria(medio + 1, sup, arr, target)


def busqueda_lineal(arr, target):
    for persona in arr:
        if persona.nombre == target:
            return persona
    return -1
