"""
Ejercicio 2 - EcoTech Solutions
Jerarquía de clases para gestión de productos sustentables y persistencia JSON.
"""

import json
import os


class StockInvalidoError(Exception):
    """Excepción lanzada cuando el valor de stock es negativo."""
    def __init__(self, mensaje="El stock no puede ser un valor negativo."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class DispositivoEcologico:
    """Clase base para dispositivos ecológicos del catálogo."""

    def __init__(self, id_producto: str, nombre: str, precio: float, stock: int):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self._stock = 0
        self.stock = stock

    @property
    def stock(self) -> int:
        return self._stock

    @stock.setter
    def stock(self, nuevo_stock: int):
        if nuevo_stock < 0:
            raise StockInvalidoError(
                f"No se puede asignar stock negativo ({nuevo_stock}) a '{self.nombre}'."
            )
        self._stock = nuevo_stock

    def generar_ficha_tecnica(self) -> dict:
        """Devuelve la ficha técnica comercial en formato diccionario."""
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "precio": f"${self.precio:.2f}",
            "stock": self.stock
        }


class PanelSolar(DispositivoEcologico):
    """Especialización para paneles solares fotovoltaicos."""

    def __init__(self, id_producto: str, nombre: str, precio: float, stock: int, eficiencia: float, potencia_w: int):
        super().__init__(id_producto, nombre, precio, stock)
        self.eficiencia = eficiencia
        self.potencia_w = potencia_w

    def generar_ficha_tecnica(self) -> dict:
        """Sobrescribe la ficha técnica agregando especificaciones técnicas del panel."""
        ficha_base = super().generar_ficha_tecnica()
        ficha_base.update({
            "tipo_producto": "Panel Solar Fotovoltaico",
            "potencia_watts": self.potencia_w,
            "eficiencia_porcentaje": f"{self.eficiencia}%"
        })
        return ficha_base


class GestorInventario:
    """Manejo de almacenamiento y serialización de productos."""

    @staticmethod
    def guardar_catalogo_json(lista_dispositivos: list, ruta_archivo: str) -> None:
        datos = [d.generar_ficha_tecnica() for d in lista_dispositivos]
        with open(ruta_archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    try:
        panel_error = PanelSolar("SOL-999", "Panel Defectuoso", 200.0, -5, 18.0, 300)
    except StockInvalidoError as error:
        print("Captura controlada de excepción:", error)

    p1 = PanelSolar("SOL-001", "EcoPanel Ultra 400W", 350.00, 15, 21.5, 400)
    p2 = DispositivoEcologico("BAT-001", "Batería Li-Ion 5kWh", 1200.00, 4)

    ruta_json = os.path.join(os.path.dirname(__file__), "catalogo_ecotech.json")
    GestorInventario.guardar_catalogo_json([p1, p2], ruta_json)