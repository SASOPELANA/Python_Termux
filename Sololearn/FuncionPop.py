# La función pop() en Python se usa para eliminar
# y devolver un elemento de una lista. 
# Puedes especificar la posición del elemento o
# eliminar el último si no se proporciona
# posición.
# Ejemplos:

# Crear una lista
frutas = ["manzana", "naranja", "banana", "cereza"]

# Eliminar y devolver el último elemento
ultima_fruta = frutas.pop()
print("Última fruta eliminada:", ultima_fruta) 
# Output: cereza

# Eliminar y devolver el elemento en la posición 1
fruta_eliminada = frutas.pop(1)
print("Fruta en la posición 1 eliminada:", fruta_eliminada) 
# Output: naranja

# Lista después de las eliminaciones
print("Lista actualizada:", frutas)  
# Output: ['manzana', 'banana']


