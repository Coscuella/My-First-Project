# LECCIÓN: FUNCIONES EN PYTHON
# Una función es un bloque de código con nombre que puedes reutilizar.
# Se define con `def`, recibe parámetros (entradas) y devuelve algo con `return`.


# 1. La función más simple: no recibe nada, no devuelve nada.
def saludar():
    print("¡Hola, mundo!")


# 2. Con un parámetro: recibe un dato y lo usa.
def saludar_a(nombre):
    print(f"¡Hola, {nombre}!")


# 3. Con return: devuelve un resultado que puedes guardar en una variable.
def sumar(a, b):
    return a + b


# 4. Con condiciones (if / else).
def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False


# 5. Con bucles (for): recorre una lista.
def sumar_lista(numeros):
    total = 0
    for n in numeros:
        total += n
    return total


# 6. Con valor por defecto: si no pasas el segundo argumento, usa 2.
def potencia(base, exponente=2):
    return base ** exponente


# 7. Función con lógica: ¿es par?  (% es el resto de la división)
def es_par(numero):
    return numero % 2 == 0


# 8. Factorial: 5! = 5 * 4 * 3 * 2 * 1 = 120
def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


# 9. Trabajar con texto.
def invertir_texto(texto):
    return texto[::-1]


# 10. Función que usa otras funciones (así se construyen programas grandes).
def resumen_edad(nombre, edad):
    estado = "mayor" if es_mayor_de_edad(edad) else "menor"
    return f"{nombre} tiene {edad} años y es {estado} de edad."


# --- PRUEBA: esto se ejecuta solo si corres `python3 funciones.py` ---
if __name__ == "__main__":
    saludar()
    saludar_a("Brandon")
    print("3 + 4 =", sumar(3, 4))
    print("¿20 es mayor de edad?", es_mayor_de_edad(20))
    print("Suma de [1, 2, 3, 4]:", sumar_lista([1, 2, 3, 4]))
    print("5 al cuadrado:", potencia(5))
    print("2 a la 10:", potencia(2, 10))
    print("¿7 es par?", es_par(7))
    print("Factorial de 5:", factorial(5))
    print("'Python' al revés:", invertir_texto("Python"))
    print(resumen_edad("Ana", 15))
