"""
Universal Graph Styling Library - Refactored
Provides a universal visualization system for ANY dataset type
"""

# Primary exports: Universal system (function_graph_md)
from .function_graph_md import (
    # Core universal components
    GraphStyle,
    crear_grafica_universal,
    aplicar_estilo_universal,
    
    # Configuration
    configurar_estilo_global,
    COLORES,
    
    # Specialized wrappers (backward compatible)
    grafica_barras_aprobados,
    grafica_pastel_aprobados,
    grafica_histograma_notas,
    grafica_barras_por_corte,
    
    # Utilities
    mostrar_estadisticas_tabla,
    guardar_grafica
)

# Legacy support: Import from graficas and function_graph_json
try:
    from .graficas import (
        configurar_estilo_global as _legacy_config,
        COLORES as _legacy_colores
    )
except ImportError:
    pass

try:
    from .function_graph_json import (
        crear_grafica_barras,
        crear_grafica_pastel,
        crear_histograma,
        crear_barras_agrupadas,
        imprimir_tabla_formateada,
        DEFAULT_STYLE
    )
except ImportError:
    # Fallback if function_graph_json doesn't exist
    crear_grafica_barras = None
    crear_grafica_pastel = None
    crear_histograma = None
    crear_barras_agrupadas = None
    imprimir_tabla_formateada = None
    DEFAULT_STYLE = None

__all__ = [
    # ====================================
    # UNIVERSAL SYSTEM (Recommended)
    # ====================================
    'GraphStyle',              # Type-safe configuration
    'crear_grafica_universal', # Universal creator (works with ANY chart type)
    'aplicar_estilo_universal', # Universal styling engine
    
    # Configuration
    'configurar_estilo_global',
    'COLORES',
    
    # ====================================
    # SPECIALIZED WRAPPERS (Backward Compatible)
    # ====================================
    'grafica_barras_aprobados',
    'grafica_pastel_aprobados',
    'grafica_histograma_notas',
    'grafica_barras_por_corte',
    
    # ====================================
    # UTILITIES
    # ====================================
    'mostrar_estadisticas_tabla',
    'guardar_grafica',
    
    # ====================================
    # LEGACY SUPPORT (function_graph_json)
    # ====================================
    'crear_grafica_barras',      # Generic bar chart
    'crear_grafica_pastel',       # Generic pie chart
    'crear_histograma',           # Generic histogram
    'crear_barras_agrupadas',     # Generic grouped bars
    'imprimir_tabla_formateada',  # Table formatter
    'DEFAULT_STYLE'               # Default configuration
]
