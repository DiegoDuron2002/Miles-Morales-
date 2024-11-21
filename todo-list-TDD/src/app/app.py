from __future__ import absolute_import

class App:
    @staticmethod
    def add(a,b):
        return a+b

    @staticmethod
    def resta(a,b):
        return a-b

    @staticmethod
    def multiplicacion(a,b):
        return a*b

    @staticmethod
    def division(a,b):
        if b == 0:
            raise ValueError("No se puede dividir por cero")
        return a / b

    # 1. Verifica si una lista contiene un número primo
    @staticmethod
    def contiene_numero_primo(lista):
        """
        Verifica si hay al menos un número primo en la lista.
        Retorna True si hay un número primo, de lo contrario, False.
        """
        def es_primo(n):
            if n < 2:
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True

        return any(es_primo(num) for num in lista)
       

    # 2. Cuenta los números pares en un rango dado
    @staticmethod
    def contar_pares(inicio, fin):
        """
        Cuenta la cantidad de números pares en el rango desde 'inicio' hasta 'fin' (inclusive).
        Retorna la cantidad de números pares.
        """
        return len([x for x in range(inicio, fin + 1) if x % 2 == 0])
        

    # 3. Encuentra el número máximo en una lista que sea múltiplo de un valor dado
    @staticmethod
    def maximo_multiplo(lista, multiplo):
        """
        Encuentra y retorna el valor máximo de la lista que es múltiplo del parámetro 'multiplo'.
        Si no hay múltiplos, retorna None.
        """
        multiplos = [x for x in lista if x % multiplo == 0]
        return max(multiplos) if multiplos else None

        

    # 4. Verifica si una palabra es palíndroma (se lee igual en ambos sentidos)
    @staticmethod
    def es_palindromo(palabra):
        """
        Verifica si la palabra es un palíndromo (igual al leerla al revés).
        Retorna True si es palíndromo, de lo contrario, False.
        """
        return palabra == palabra[::-1]

    # 5. Calcula la suma de los primeros n números impares
    @staticmethod
    def suma_primeros_impares(n):
        """
        Calcula y retorna la suma de los primeros 'n' números impares.
        """
        return sum(x for x in range(1, 2 * n, 2))

    # 6. Verifica si todos los elementos de una lista son únicos
    @staticmethod
    def elementos_unicos(lista):
        """
        Verifica si todos los elementos de la lista son únicos.
        Retorna True si son únicos, de lo contrario, False.
        """
        return len(lista) == len(set(lista))

    # 7. Calcula el factorial de un número sin usar recursión
    @staticmethod
    def calcular_factorial(numero):
        """
        Calcula y retorna el factorial de 'numero' usando un ciclo.
        """

        if numero < 0:
            raise ValueError("El factorial no está definido para números negativos")
        factorial = 1
        for i in range(1, numero + 1):
            factorial *= i
        return factorial
        

    # 8. Cuenta la cantidad de vocales en una cadena
    def contar_vocales(cadena):
        """
        Cuenta y retorna la cantidad de vocales en la cadena.
        """
        return sum(1 for c in cadena.lower() if c in "aeiou")

    # 9. Encuentra el segundo número mayor en una lista
    @staticmethod
    def segundo_mayor(lista):
        """
        Encuentra y retorna el segundo número más grande en la lista.
        Si no existe, retorna None.
        """
        
        if len(lista) < 2:
            return None
        unicos = list(set(lista))
        unicos.sort(reverse=True)
        return unicos[1] if len(unicos) > 1 else None

    # 10. Calcula la serie de Fibonacci hasta n términos
    @staticmethod
    def fibonacci(n):
        """
        Genera y retorna una lista con los primeros 'n' términos de la serie de Fibonacci.
        """
        if n <= 0:
            return []
        fib = [0, 1]
        while len(fib) < n:
            fib.append(fib[-1] + fib[-2])
        return fib[:n]
