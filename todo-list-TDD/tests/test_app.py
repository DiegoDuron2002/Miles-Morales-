import sys
sys.path.append('../src')
from src.app.app import App
import unittest


class MyTester(unittest.TestCase):
    def setUp(self):
        self.tester = App()

    def test_suma_ok(self):
        self.assertEqual(self.tester.add(1, 2), 3, "Error en la suma")

    def test_suma_bad(self):
        self.assertNotEqual(App.add(10, 20), 4, "Error en la suma")

    def test_resta_1(self):
        self.assertEqual(App.resta(1, -2), 3, "Error en la resta")

    def test_resta_2(self):
        self.assertEqual(App.resta(10, 5), 5, "Error en la resta")

    def test_multiplicacion_1(self):
        self.assertEqual(App.multiplicacion(1, 2), 2, "Error en la multiplicación")

    def test_multiplicacion_2(self):
        self.assertNotEqual(App.multiplicacion(15, 0), 15, "Error en la multiplicación")

    def test_multiplicacion_3(self):
        self.assertEqual(App.multiplicacion(20, 3), 60, "Error en la multiplicación")

    def test_division_1(self):
        self.assertEqual(App.division(10, 2), 5, "Error en la división")

    def test_division_2(self):
        self.assertEqual(App.division(0, 500), 0, "Error en la división")

    # 1. Test para contiene_numero_primo
    def test_contiene_numero_primo_con_primos(self):
        self.assertTrue(App.contiene_numero_primo([1, 3, 4, 5]))

    def test_contiene_numero_primo_sin_primos(self):
        self.assertFalse(App.contiene_numero_primo([4, 6, 8, 10]))

    def test_contiene_numero_primo_lista_vacia(self):
        self.assertFalse(App.contiene_numero_primo([]))

    # 2. Test para contar_pares
    def test_contar_pares_rango_normal(self):
        self.assertEqual(App.contar_pares(1, 10), 5)

    def test_contar_pares_solo_un_par(self):
        self.assertEqual(App.contar_pares(2, 2), 1)

    def test_contar_pares_sin_pares(self):
        self.assertEqual(App.contar_pares(1, 1), 0)

    # 3. Test para maximo_multiplo
    def test_maximo_multiplo_hay_multiplo(self):
        self.assertEqual(App.maximo_multiplo([1, 3, 6, 9, 12], 3), 12)

    def test_maximo_multiplo_sin_multiplo(self):
        self.assertIsNone(App.maximo_multiplo([1, 5, 7], 4))

    def test_maximo_multiplo_lista_vacia(self):
        self.assertIsNone(App.maximo_multiplo([], 3))

    # 4. Test para es_palindromo
    def test_es_palindromo_palindromo(self):
        self.assertTrue(App.es_palindromo("radar"))

    def test_es_palindromo_no_palindromo(self):
        self.assertFalse(App.es_palindromo("hello"))

    def test_es_palindromo_palabra_vacia(self):
        self.assertTrue(App.es_palindromo(""))

    # 5. Test para suma_primeros_impares
    def test_suma_primeros_impares_positivos(self):
        self.assertEqual(App.suma_primeros_impares(3), 9)

    def test_suma_primeros_impares_cero(self):
        self.assertEqual(App.suma_primeros_impares(0), 0)

    def test_suma_primeros_impares_grande(self):
        self.assertEqual(App.suma_primeros_impares(10), 100)

    # 6. Test para elementos_unicos
    def test_elementos_unicos_unicos(self):
        self.assertTrue(App.elementos_unicos([1, 2, 3, 4]))

    def test_elementos_unicos_no_unicos(self):
        self.assertFalse(App.elementos_unicos([1, 2, 2, 4]))

    def test_elementos_unicos_lista_vacia(self):
        self.assertTrue(App.elementos_unicos([]))

    # 7. Test para calcular_factorial
    def test_calcular_factorial_positivo(self):
        self.assertEqual(App.calcular_factorial(5), 120)

    def test_calcular_factorial_cero(self):
        self.assertEqual(App.calcular_factorial(0), 1)

    def test_calcular_factorial_uno(self):
        self.assertEqual(App.calcular_factorial(1), 1)

    # 8. Test para contar_vocales
    def test_contar_vocales_varias_vocales(self):
        self.assertEqual(App.contar_vocales("hello"), 2)

    def test_contar_vocales_sin_vocales(self):
        self.assertEqual(App.contar_vocales("rhythm"), 0)

    def test_contar_vocales_vocales_mayusculas(self):
        self.assertEqual(App.contar_vocales("AEIOU"), 5)

    # 9. Test para segundo_mayor
    def test_segundo_mayor_lista_varios_elementos(self):
        self.assertEqual(App.segundo_mayor([1, 3, 4, 5]), 4)

    def test_segundo_mayor_lista_dos_elementos(self):
        self.assertEqual(App.segundo_mayor([10, 20]), 10)

    def test_segundo_mayor_lista_un_elemento(self):
        self.assertIsNone(App.segundo_mayor([5]))

    # 10. Test para fibonacci
    def test_fibonacci_cinco_terminos(self):
        self.assertEqual(App.fibonacci(5), [0, 1, 1, 2, 3])

    def test_fibonacci_cero_terminos(self):
        self.assertEqual(App.fibonacci(0), [])

    def test_fibonacci_un_termino(self):
        self.assertEqual(App.fibonacci(1), [0])


if __name__ == '__main__':
    unittest.main()
