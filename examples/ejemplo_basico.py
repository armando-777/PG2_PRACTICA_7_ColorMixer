
"""
Ejemplo básico de uso de ColorMixer
"""

import sys
import os

# Agregar src al path para poder importar
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from color_mixer.color_core import ColorMixerCore
from color_mixer.estructuras import Color
from color_mixer.inventario_manager import InventarioManager
from color_mixer.visual_exports import VisualExporter

def ejemplo_mezcla_colores():
    """Demuestra mezcla básica de colores."""
    print("=== Ejemplo: Mezcla de Colores ===")
    
    # Crear mixer usando patrón Builder
    mixer = ColorMixerCore()
    
    # Agregar colores con porcentajes
    mixer.agregar_color_preset("rojo_ferrari", 60.0)\
         .agregar_color_preset("blanco_perla", 40.0)
    
    # Realizar mezcla
    resultado = mixer.mezclar_colores()
    
    print(f"Colores mezclados:")
    for color in mixer.colores_actuales:
        print(f"  - {color.nombre}: {color.to_hex()}")
    
    print(f"\nResultado: {resultado.nombre}")
    print(f"HEX: {resultado.to_hex()}")
    print(f"RGB: {resultado.to_rgb()}")
    
    # Guardar mezcla
    if mixer.guardar_mezcla_personal("Mi_Color_Personalizado"):
        print("✓ Mezcla guardada exitosamente")
    
    print()

def ejemplo_inventario():
    """Demuestra gestión de inventario."""
    print("=== Ejemplo: Inventario de Autos ===")
    
    # Obtener gestor de inventario (Singleton)
    inventario = InventarioManager()
    
    # Crear mixer para obtener colores
    mixer = ColorMixerCore()
    mixer.agregar_color_preset("rojo_ferrari", 85.0)\
         .agregar_color_preset("negro_carbón", 15.0)
    
    colores_ferrari = mixer.colores_actuales.obtener_colores()
    
    # Registrar auto
    exito = inventario.registrar_auto(
        "Ferrari 488 Spider",
        "FER488SP01",
        colores_ferrari,
        mixer.porcentajes_actuales
    )
    
    if exito:
        print("✓ Ferrari registrado exitosamente")
        
        # Obtener información del auto
        info = inventario.obtener_color_auto("FER488SP01")
        print(f"Modelo: {info['modelo']}")
        print(f"Color resultante: {info['color_resultante']['nombre']}")
        print(f"HEX: {info['color_resultante']['hex']}")
    
    print()

def ejemplo_exportacion():
    """Demuestra exportación visual."""
    print("=== Ejemplo: Exportación Visual ===")
    
    # Crear algunos colores
    mixer = ColorMixerCore()
    mixer.agregar_color_preset("rojo_ferrari", 40.0)\
         .agregar_color_preset("azul_marino", 35.0)\
         .agregar_color_preset("dorado", 25.0)
    
    colores = mixer.colores_actuales.obtener_colores()
    resultado = mixer.mezclar_colores()
    colores.append(resultado)
    
    # Crear exportador
    exporter = VisualExporter()
    
    # Exportar en diferentes formatos
    if exporter.exportar_paleta_svg(colores, "ejemplo_paleta"):
        print("✓ Paleta SVG exportada")
    
    if exporter.generar_reporte_colores(colores, "ejemplo_reporte"):
        print("✓ Reporte HTML generado")
    
    print("Archivos guardados en 'colormixer_exports/'")
    print()

def main():
    """Función principal."""
    print("ColorMixer - Ejemplos de Uso")
    print("=" * 40)
    
    try:
        ejemplo_mezcla_colores()
        ejemplo_inventario()
        ejemplo_exportacion()
        
        print("✓ Todos los ejemplos ejecutados exitosamente")
        
    except Exception as e:
        print(f"Error ejecutando ejemplos: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()