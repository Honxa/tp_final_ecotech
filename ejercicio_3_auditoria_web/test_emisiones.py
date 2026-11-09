"""
Ejercicio 3 - Punto A: Pruebas unitarias para el algoritmo de cálculo de emisiones.
"""

import unittest


def calcular_emisiones_carbono(consumo_kwh: float, factor_emision: float = 0.4) -> float:
    """Calcula las emisiones de CO2 equivalente según el consumo energético en kWh."""
    if consumo_kwh < 0:
        raise ValueError("El consumo energético en kWh no puede ser negativo.")
    return round(consumo_kwh * factor_emision, 2)


class TestCalculoEmisiones(unittest.TestCase):
    """Casos de prueba para verificar la precisión e integridad de calcular_emisiones_carbono."""

    def test_calculo_nominal_factor_defecto(self):
        self.assertEqual(calcular_emisiones_carbono(100.0), 40.0)

    def test_calculo_nominal_factor_custom(self):
        self.assertEqual(calcular_emisiones_carbono(250.0, factor_emision=0.5), 125.0)

    def test_calculo_consumo_cero(self):
        self.assertEqual(calcular_emisiones_carbono(0.0), 0.0)

    def test_excepcion_consumo_negativo(self):
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-50.0)


if __name__ == "__main__":
    unittest.main()