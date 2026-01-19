"""
Módulo de estilos para gráficas del proyecto
Autor: Proyecto Corhuila
Fecha: 2025
"""

import matplotlib.pyplot as plt
import seaborn as sns

# Colores institucionales
COLORES = {
    'aprobado': '#2ecc71',      # Verde
    'no_aprobado': '#e74c3c',   # Rojo
    'primario': '#3498db',       # Azul
    'secundario': '#9b59b6',     # Morado
    'advertencia': '#f39c12',    # Naranja
    'info': '#1abc9c',           # Turquesa
    'exito': '#27ae60',          # Verde oscuro
    'peligro': '#c0392b'         # Rojo oscuro
}

def configurar_estilo_global():
    """
    Configura el estilo global para todas las gráficas del notebook
    """
    sns.set_style("whitegrid")
    plt.rcParams['figure.figsize'] = (10, 6)
    plt.rcParams['font.size'] = 10
    plt.rcParams['axes.labelsize'] = 12
    plt.rcParams['axes.titlesize'] = 14
    plt.rcParams['xtick.labelsize'] = 10
    plt.rcParams['ytick.labelsize'] = 10
    plt.rcParams['legend.fontsize'] = 10
    plt.rcParams['figure.titlesize'] = 16
    plt.rcParams['axes.grid'] = True
    plt.rcParams['grid.alpha'] = 0.3
    

def grafica_barras_aprobados(conteo_estado, total_estudiantes, titulo=None, figsize=(10, 6)):
    """
    Crea una gráfica de barras para mostrar estudiantes aprobados vs no aprobados
    
    Parámetros:
    -----------
    conteo_estado : pd.Series
        Serie con el conteo de aprobados y no aprobados
    total_estudiantes : int
        Total de estudiantes
    titulo : str, optional
        Título personalizado para la gráfica
    figsize : tuple, optional
        Tamaño de la figura (ancho, alto)
    
    Returns:
    --------
    fig, ax : matplotlib figure and axes
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    # Colores
    colores = [COLORES['aprobado'], COLORES['no_aprobado']]
    
    # Crear barras
    barras = ax.bar(conteo_estado.index, conteo_estado.values, 
                    color=colores, alpha=0.7, edgecolor='black', linewidth=2)
    
    # Agregar valores en las barras
    for i, barra in enumerate(barras):
        altura = barra.get_height()
        ax.text(barra.get_x() + barra.get_width()/2., altura,
                f'{int(altura)}\n({altura/total_estudiantes*100:.1f}%)',
                ha='center', va='bottom', fontsize=12, fontweight='bold')
    
    # Configurar etiquetas
    ax.set_xlabel('Estado', fontsize=12, fontweight='bold')
    ax.set_ylabel('Cantidad de Estudiantes', fontsize=12, fontweight='bold')
    
    if titulo is None:
        titulo = 'Distribución de Estudiantes: Aprobados vs No Aprobados\n(Corte 1: 30%, Corte 2: 30%, Corte 3: 40%)'
    
    ax.set_title(titulo, fontsize=14, fontweight='bold')
    ax.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    return fig, ax


def grafica_pastel_aprobados(conteo_estado, titulo=None, figsize=(8, 8)):
    """
    Crea una gráfica de pastel para mostrar la proporción de aprobados vs no aprobados
    
    Parámetros:
    -----------
    conteo_estado : pd.Series
        Serie con el conteo de aprobados y no aprobados
    titulo : str, optional
        Título personalizado para la gráfica
    figsize : tuple, optional
        Tamaño de la figura (ancho, alto)
    
    Returns:
    --------
    fig, ax : matplotlib figure and axes
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    # Colores
    colores_pastel = [COLORES['aprobado'], COLORES['no_aprobado']]
    explode = (0.05, 0.05)  # Separar un poco las secciones
    
    # Crear gráfica de pastel
    ax.pie(conteo_estado.values, 
           labels=conteo_estado.index, 
           autopct='%1.1f%%',
           startangle=90,
           colors=colores_pastel,
           explode=explode,
           shadow=True,
           textprops={'fontsize': 12, 'fontweight': 'bold'})
    
    if titulo is None:
        titulo = 'Proporción de Estudiantes Aprobados vs No Aprobados\n(Nota mínima: 3.0)'
    
    ax.set_title(titulo, fontsize=14, fontweight='bold', pad=20)
    ax.axis('equal')
    
    plt.tight_layout()
    return fig, ax


def grafica_histograma_notas(df, columna='Nota_Final', bins=10, titulo=None, figsize=(10, 6)):
    """
    Crea un histograma de distribución de notas
    
    Parámetros:
    -----------
    df : pd.DataFrame
        DataFrame con los datos
    columna : str
        Nombre de la columna con las notas
    bins : int
        Número de bins para el histograma
    titulo : str, optional
        Título personalizado para la gráfica
    figsize : tuple, optional
        Tamaño de la figura (ancho, alto)
    
    Returns:
    --------
    fig, ax : matplotlib figure and axes
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    # Crear histograma
    n, bins_edges, patches = ax.hist(df[columna], bins=bins, 
                                      color=COLORES['primario'], 
                                      alpha=0.7, edgecolor='black', linewidth=1.5)
    
    # Colorear barras según si están por encima o debajo de 3.0
    for i, patch in enumerate(patches):
        if bins_edges[i] < 3.0:
            patch.set_facecolor(COLORES['no_aprobado'])
        else:
            patch.set_facecolor(COLORES['aprobado'])
    
    # Línea vertical en 3.0 (nota mínima)
    ax.axvline(x=3.0, color='red', linestyle='--', linewidth=2, label='Nota mínima (3.0)')
    
    # Configurar etiquetas
    ax.set_xlabel('Nota Final', fontsize=12, fontweight='bold')
    ax.set_ylabel('Frecuencia', fontsize=12, fontweight='bold')
    
    if titulo is None:
        titulo = 'Distribución de Notas Finales'
    
    ax.set_title(titulo, fontsize=14, fontweight='bold')
    ax.legend()
    ax.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    return fig, ax


def grafica_barras_por_corte(df, figsize=(12, 6)):
    """
    Crea una gráfica de barras agrupadas mostrando las notas por corte
    
    Parámetros:
    -----------
    df : pd.DataFrame
        DataFrame con los datos de estudiantes
    figsize : tuple, optional
        Tamaño de la figura (ancho, alto)
    
    Returns:
    --------
    fig, ax : matplotlib figure and axes
    """
    import numpy as np
    
    fig, ax = plt.subplots(figsize=figsize)
    
    # Datos
    estudiantes = df['Nombres'] + ' ' + df['Apellidos'].str[0] + '.'
    corte1 = df['Corte 1']
    corte2 = df['Corte 2']
    corte3 = df['Corte 3']
    
    # Configuración de barras
    x = np.arange(len(estudiantes))
    width = 0.25
    
    # Crear barras
    ax.bar(x - width, corte1, width, label='Corte 1 (30%)', 
           color=COLORES['primario'], alpha=0.8)
    ax.bar(x, corte2, width, label='Corte 2 (30%)', 
           color=COLORES['secundario'], alpha=0.8)
    ax.bar(x + width, corte3, width, label='Corte 3 (40%)', 
           color=COLORES['info'], alpha=0.8)
    
    # Línea de nota mínima
    ax.axhline(y=3.0, color='red', linestyle='--', linewidth=1.5, label='Nota mínima (3.0)')
    
    # Configurar etiquetas
    ax.set_xlabel('Estudiantes', fontsize=12, fontweight='bold')
    ax.set_ylabel('Notas', fontsize=12, fontweight='bold')
    ax.set_title('Notas por Corte de cada Estudiante', fontsize=14, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(estudiantes, rotation=45, ha='right')
    ax.legend()
    ax.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    return fig, ax


def mostrar_estadisticas_tabla(df):
    """
    Muestra una tabla con estadísticas descriptivas de las notas
    
    Parámetros:
    -----------
    df : pd.DataFrame
        DataFrame con los datos de estudiantes
    """
    print("=" * 60)
    print("ESTADÍSTICAS DESCRIPTIVAS DE LAS NOTAS")
    print("=" * 60)
    
    estadisticas = df[['Corte 1', 'Corte 2', 'Corte 3', 'Nota_Final']].describe()
    print(estadisticas.round(2))
    
    print("\n" + "=" * 60)
    print("RESUMEN DE APROBACIÓN")
    print("=" * 60)
    
    conteo = df['Estado'].value_counts()
    print(conteo)
    
    print(f"\nTotal de estudiantes: {len(df)}")
    print(f"Aprobados: {conteo.get('Aprobado', 0)} ({conteo.get('Aprobado', 0)/len(df)*100:.2f}%)")
    print(f"No aprobados: {conteo.get('No Aprobado', 0)} ({conteo.get('No Aprobado', 0)/len(df)*100:.2f}%)")
    print("=" * 60)


def guardar_grafica(fig, nombre_archivo, carpeta_output='data/output/img', dpi=300):
    """
    Guarda una gráfica en la carpeta de salida
    
    Parámetros:
    -----------
    fig : matplotlib figure
        Figura a guardar
    nombre_archivo : str
        Nombre del archivo (sin extensión)
    carpeta_output : str
        Ruta de la carpeta de salida
    dpi : int
        Resolución de la imagen
    """
    import os
    
    # Crear carpeta si no existe
    os.makedirs(carpeta_output, exist_ok=True)
    
    # Guardar en formato PNG y PDF
    ruta_png = os.path.join(carpeta_output, f"{nombre_archivo}.png")
    ruta_pdf = os.path.join(carpeta_output, f"{nombre_archivo}.pdf")
    
    fig.savefig(ruta_png, dpi=dpi, bbox_inches='tight')
    fig.savefig(ruta_pdf, bbox_inches='tight')
    
    print(f"✓ Gráfica guardada en:")
    print(f"  - {ruta_png}")
    print(f"  - {ruta_pdf}")
