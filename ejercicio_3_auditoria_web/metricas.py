"""
Ejercicio 3 - Punto B: Procesamiento de métricas de consumo energético.
"""

try:
    from test_emisiones import calcular_emisiones_carbono
except ImportError:
    from .test_emisiones import calcular_emisiones_carbono


def obtener_metricas_consumo(registros: list) -> dict:
    """Procesa el historial de consumo para calcular totales y la planta de mayor consumo."""
    if not registros:
        return {
            "consumo_total_kwh": 0.0,
            "emisiones_totales_co2": 0.0,
            "planta_mayor_consumo": "N/A",
            "detalle_plantas": []
        }

    consumo_total = 0.0
    emisiones_totales = 0.0
    planta_max_nombre = ""
    planta_max_consumo = -1.0
    detalle_plantas = []

    for reg in registros:
        nombre_planta = reg.get("planta", "Desconocida")
        consumo = float(reg.get("consumo_kwh", 0))
        emisiones = calcular_emisiones_carbono(consumo)

        consumo_total += consumo
        emisiones_totales += emisiones

        if consumo > planta_max_consumo:
            planta_max_consumo = consumo
            planta_max_nombre = nombre_planta

        detalle_plantas.append({
            "planta": nombre_planta,
            "consumo_kwh": consumo,
            "emisiones_co2": emisiones
        })

    return {
        "consumo_total_kwh": round(consumo_total, 2),
        "emisiones_totales_co2": round(emisiones_totales, 2),
        "planta_mayor_consumo": planta_max_nombre,
        "detalle_plantas": detalle_plantas
    }