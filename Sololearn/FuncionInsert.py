#En Python, el método insert() se utiliza para 
# insertar un elemento en una lista en una
# posición específica. La sintaxis básica es la 
# siguiente:

# lista.insert(posición, elemento)

# Posición: La posición en la que se insertará
# el elemento.
# Elemento: El elemento que se va a insertar.
# Ejemplo: 

frutas = ["manzana", "banana", "cereza"]
frutas.insert(1, "naranja")
print(frutas)

# Este código insertará "naranja" en la posición
# 1 de la lista frutas, desplazando los elementos
# existentes hacia la derecha. El resultado será:
# ['manzana', 'naranja', 'banana', 'cereza']

colors = ["Red", "Blue", "Yellow"]
colors.insert(2, "Green")
colors.append("Black")
print(colors[3])
