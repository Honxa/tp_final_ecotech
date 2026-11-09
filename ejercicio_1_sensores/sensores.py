"""
Ejercicio 1 - EcoTech Solutions
Módulo de sanitización y análisis estadístico de lecturas de sensores.
"""

def limpiar_registro_sensor(registro_raw: dict) -> dict:
    """
    Normaliza los datos crudos de un sensor procesando ID, temperatura y ubicación.
    """
    sensor_id_raw = registro_raw.get("sensor_id", "")
    sensor_id = str(sensor_id_raw).strip() if sensor_id_raw else "DESCONOCIDO"

    temp_raw = registro_raw.get("temperatura", 0)
    if isinstance(temp_raw, (int, float)):
        temperatura = float(temp_raw)
    else:
        temp_str = str(temp_raw).strip().lower()
        temp_str = temp_str.replace("°", "").replace("c", "").replace("f", "").strip()
        try:
            temperatura = float(temp_str)
        except ValueError:
            temperatura = 0.0

    ubicacion_raw = registro_raw.get("ubicacion")
    if ubicacion_raw and str(ubicacion_raw).strip():
        ubicacion = str(ubicacion_raw).strip()
    else:
        ubicacion = "Área No Asignada"

    return {
        "sensor_id": sensor_id,
        "temperatura": temperatura,
        "ubicacion": ubicacion
    }


def generar_resumen_sensores(lista_sensores_limpios: list, umbral_temperatura: float) -> tuple:
    """
    Retorna los IDs de sensores que superan el umbral térmico y el promedio global.
    """
    if not lista_sensores_limpios:
        return ([], 0.0)

    sensores_alerta = []
    sumatoria_termica = 0.0

    for sensor in lista_sensores_limpios:
        temp = sensor["temperatura"]
        sumatoria_termica += temp
        if temp > umbral_temperatura:
            sensores_alerta.append(sensor["sensor_id"])

    promedio = sumatoria_termica / len(lista_sensores_limpios)
    return (sensores_alerta, round(promedio, 2))


if __name__ == "__main__":
    registros_crudos = [
        {"sensor_id": " SENSOR-001 ", "temperatura": "24.5C", "ubicacion": "Planta Norte"},
        {"sensor_id": "SENSOR-002", "temperatura": "38.2°c", "ubicacion": "  Planta Sur  "},
        {"sensor_id": " SENSOR-003 ", "temperatura": "41.0 C"},
        {"sensor_id": "SENSOR-004 ", "temperatura": "19.0C", "ubicacion": "Planta Este"},
        {"sensor_id": " SENSOR-005", "temperatura": "36.8°C", "ubicacion": ""},
    ]

    sensores_limpios = [limpiar_registro_sensor(r) for r in registros_crudos]
    alertas, promedio = generar_resumen_sensores(sensores_limpios, 35.0)

    print("Sensores limpios:", sensores_limpios)
    print("Alertas:", alertas)
    print("Promedio térmico:", promedio)