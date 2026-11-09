"""
Ejercicio 3 - Punto B: Vista en Django para la representación del panel de sustentabilidad.
"""

try:
    from django.shortcuts import render
except ImportError:
    render = None

try:
    from metricas import obtener_metricas_consumo
except ImportError:
    from .metricas import obtener_metricas_consumo


def vista_panel_sustentabilidad(request):
    """Vista funcional encargada de construir el contexto y renderizar el panel."""
    registros_simulados = [
        {"planta": "Planta Industrial Norte", "consumo_kwh": 12500.50},
        {"planta": "Planta Ensambladora Sur", "consumo_kwh": 18400.00},
        {"planta": "Centro Logístico Cuyo", "consumo_kwh": 9200.75},
        {"planta": "Planta Textil Este", "consumo_kwh": 14300.20},
    ]

    metricas = obtener_metricas_consumo(registros_simulados)

    contexto = {
        "titulo_panel": "Panel Administrativo de Sustentabilidad - EcoTech Solutions",
        "metricas": metricas,
        "estado_sistema": "Operativo",
    }

    if render:
        return render(request, "sustentabilidad/panel.html", contexto)
    return contexto