"""
Universal Graph Styling Module
Author: Proyecto Corhuila
Date: 2025

This module provides a universal styling system for all chart types.
It eliminates redundancy through a single, configurable styling engine.
"""

import matplotlib.pyplot as plt
import seaborn as sns
from typing import Optional, Dict, Any, Tuple, List, Callable
from dataclasses import dataclass, field

# Institutional color palette
COLORES = {
    'aprobado': '#2ecc71',
    'no_aprobado': '#e74c3c',
    'primario': '#3498db',
    'secundario': '#9b59b6',
    'advertencia': '#f39c12',
    'info': '#1abc9c',
    'exito': '#27ae60',
    'peligro': '#c0392b'
}


@dataclass
class GraphStyle:
    """Universal graph styling configuration."""
    figsize: Tuple[int, int] = (10, 6)
    title: str = ''
    xlabel: str = ''
    ylabel: str = ''
    colors: Optional[List[str]] = None
    alpha: float = 0.7
    edge_color: str = 'black'
    edge_width: float = 2
    grid_axis: str = 'y'
    grid_alpha: float = 0.3
    font_size: int = 10
    label_size: int = 12
    title_size: int = 14
    show_legend: bool = False
    tight_layout: bool = True
    
    def __post_init__(self):
        if self.colors is None:
            self.colors = [COLORES['primario']]


def configurar_estilo_global(style: str = "whitegrid", custom_params: Optional[Dict] = None):
    """
    Configure global styling for all visualizations.
    
    Parameters:
    -----------
    style : str
        Seaborn style preset
    custom_params : dict, optional
        Custom matplotlib parameters
    """
    sns.set_style(style)
    
    default_params = {
        'figure.figsize': (10, 6),
        'font.size': 10,
        'axes.labelsize': 12,
        'axes.titlesize': 14,
        'xtick.labelsize': 10,
        'ytick.labelsize': 10,
        'legend.fontsize': 10,
        'figure.titlesize': 16,
        'axes.grid': True,
        'grid.alpha': 0.3
    }
    
    if custom_params:
        default_params.update(custom_params)
    
    plt.rcParams.update(default_params)



def aplicar_estilo_universal(ax: plt.Axes, style: GraphStyle):
    """
    Apply universal styling to any matplotlib axes.
    
    This is the core styling engine that eliminates redundancy.
    
    Parameters:
    -----------
    ax : matplotlib.axes.Axes
        The axes to style
    style : GraphStyle
        Style configuration object
    """
    if style.xlabel:
        ax.set_xlabel(style.xlabel, fontsize=style.label_size, fontweight='bold')
    if style.ylabel:
        ax.set_ylabel(style.ylabel, fontsize=style.label_size, fontweight='bold')
    if style.title:
        ax.set_title(style.title, fontsize=style.title_size, fontweight='bold')
    
    ax.grid(axis=style.grid_axis, alpha=style.grid_alpha)
    
    if style.show_legend:
        ax.legend(fontsize=style.font_size)
    
    if style.tight_layout:
        plt.tight_layout()


def crear_grafica_universal(tipo: str, data: Any, labels: Optional[List] = None,
                           style: Optional[GraphStyle] = None, **kwargs) -> Tuple[plt.Figure, plt.Axes]:
    """
    Universal graph creator - works with any chart type.
    
    This single function replaces all specific graph functions,
    eliminating code duplication entirely.
    
    Parameters:
    -----------
    tipo : str
        Chart type: 'bar', 'pie', 'hist', 'grouped_bar', 'line', 'scatter'
    data : any
        Data to plot (format depends on chart type)
    labels : list, optional
        Labels for data points
    style : GraphStyle, optional
        Styling configuration
    **kwargs : dict
        Chart-specific parameters
    
    Returns:
    --------
    fig, ax : matplotlib figure and axes
    
    Examples:
    ---------
    >>> # Bar chart
    >>> fig, ax = crear_grafica_universal('bar', [10, 20, 15], ['A', 'B', 'C'])
    
    >>> # Pie chart
    >>> fig, ax = crear_grafica_universal('pie', [30, 70], ['Failed', 'Passed'])
    
    >>> # Histogram
    >>> fig, ax = crear_grafica_universal('hist', data_array, bins=20)
    """
    if style is None:
        style = GraphStyle()
    
    fig, ax = plt.subplots(figsize=style.figsize)
    
    # Dispatch to appropriate plotting method
    plot_methods = {
        'bar': _plot_bar,
        'pie': _plot_pie,
        'hist': _plot_histogram,
        'grouped_bar': _plot_grouped_bar,
        'line': _plot_line,
        'scatter': _plot_scatter
    }
    
    if tipo not in plot_methods:
        raise ValueError(f"Tipo '{tipo}' no soportado. Opciones: {list(plot_methods.keys())}")
    
    # Execute plotting
    plot_methods[tipo](ax, data, labels, style, **kwargs)
    
    # Apply universal styling
    aplicar_estilo_universal(ax, style)
    
    return fig, ax


# ============================================
# Internal plotting functions (single source)
# ============================================

def _plot_bar(ax: plt.Axes, data: Any, labels: List, style: GraphStyle, **kwargs):
    """Internal: Plot bar chart."""
    show_values = kwargs.get('show_values', True)
    value_format = kwargs.get('value_format', None)
    
    bars = ax.bar(labels, data, color=style.colors, alpha=style.alpha,
                  edgecolor=style.edge_color, linewidth=style.edge_width)
    
    if show_values:
        for bar, value in zip(bars, data):
            height = bar.get_height()
            label = value_format(value) if value_format else f'{int(value)}'
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   label, ha='center', va='bottom', 
                   fontsize=12, fontweight='bold')


def _plot_pie(ax: plt.Axes, data: Any, labels: List, style: GraphStyle, **kwargs):
    """Internal: Plot pie chart."""
    explode = kwargs.get('explode', tuple([0.05] * len(data)))
    autopct = kwargs.get('autopct', '%1.1f%%')
    startangle = kwargs.get('startangle', 90)
    
    ax.pie(data, labels=labels, autopct=autopct, startangle=startangle,
           colors=style.colors, explode=explode, shadow=True,
           textprops={'fontsize': 12, 'fontweight': 'bold'})
    ax.axis('equal')


def _plot_histogram(ax: plt.Axes, data: Any, labels: List, style: GraphStyle, **kwargs):
    """Internal: Plot histogram with optional threshold coloring."""
    bins = kwargs.get('bins', 10)
    threshold = kwargs.get('threshold', None)
    threshold_colors = kwargs.get('threshold_colors', None)
    
    n, bins_edges, patches = ax.hist(data, bins=bins, color=style.colors[0],
                                      alpha=style.alpha, edgecolor=style.edge_color,
                                      linewidth=1.5)
    
    # Apply threshold coloring
    if threshold and threshold_colors:
        for i, patch in enumerate(patches):
            if bins_edges[i] < threshold:
                patch.set_facecolor(threshold_colors['below'])
            else:
                patch.set_facecolor(threshold_colors['above'])
        
        # Add threshold line
        threshold_label = kwargs.get('threshold_label', f'Threshold ({threshold})')
        ax.axvline(x=threshold, color='red', linestyle='--', 
                  linewidth=2, label=threshold_label)
        style.show_legend = True


def _plot_grouped_bar(ax: plt.Axes, data: Dict, labels: List, style: GraphStyle, **kwargs):
    """Internal: Plot grouped bar chart."""
    import numpy as np
    
    bar_width = kwargs.get('bar_width', 0.25)
    x = np.arange(len(labels))
    num_groups = len(data)
    offset = bar_width * (num_groups - 1) / 2
    
    for i, (group_name, values) in enumerate(data.items()):
        position = x - offset + (i * bar_width)
        ax.bar(position, values, bar_width, label=group_name,
               color=style.colors[i % len(style.colors)], alpha=style.alpha)
    
    ax.set_xticks(x)
    rotation = kwargs.get('rotation', 0)
    ax.set_xticklabels(labels, rotation=rotation, 
                       ha='right' if rotation > 0 else 'center')
    
    # Add horizontal reference line
    hline = kwargs.get('add_hline', None)
    if hline:
        ax.axhline(y=hline, color='red', linestyle='--', linewidth=1.5,
                   label=kwargs.get('hline_label', ''))
    
    style.show_legend = True


def _plot_line(ax: plt.Axes, data: Any, labels: List, style: GraphStyle, **kwargs):
    """Internal: Plot line chart."""
    marker = kwargs.get('marker', 'o')
    linewidth = kwargs.get('linewidth', 2)
    
    ax.plot(labels, data, color=style.colors[0], marker=marker,
            linewidth=linewidth, alpha=style.alpha)


def _plot_scatter(ax: plt.Axes, data: Tuple, labels: List, style: GraphStyle, **kwargs):
    """Internal: Plot scatter chart."""
    x_data, y_data = data
    size = kwargs.get('size', 50)
    
    ax.scatter(x_data, y_data, c=style.colors[0], s=size, alpha=style.alpha,
               edgecolors=style.edge_color, linewidth=style.edge_width)


# ============================================
# Specialized wrappers (backward compatible)
# ============================================

def grafica_barras_aprobados(conteo_estado, total_estudiantes, titulo=None, figsize=(10, 6)):
    """Specialized wrapper using universal graph creator."""
    if titulo is None:
        titulo = 'Distribución de Estudiantes: Aprobados vs No Aprobados\n(Corte 1: 30%, Corte 2: 30%, Corte 3: 40%)'
    
    style = GraphStyle(
        figsize=figsize,
        title=titulo,
        xlabel='Estado',
        ylabel='Cantidad de Estudiantes',
        colors=[COLORES['aprobado'], COLORES['no_aprobado']]
    )
    
    return crear_grafica_universal(
        'bar',
        conteo_estado.values,
        conteo_estado.index.tolist(),
        style,
        value_format=lambda x: f'{int(x)}\n({x/total_estudiantes*100:.1f}%)'
    )



def grafica_pastel_aprobados(conteo_estado, titulo=None, figsize=(8, 8)):
    """Specialized wrapper using universal graph creator."""
    if titulo is None:
        titulo = 'Proporción de Estudiantes Aprobados vs No Aprobados\n(Nota mínima: 3.0)'
    
    style = GraphStyle(
        figsize=figsize,
        title=titulo,
        colors=[COLORES['aprobado'], COLORES['no_aprobado']]
    )
    
    return crear_grafica_universal(
        'pie',
        conteo_estado.values,
        conteo_estado.index.tolist(),
        style
    )



def grafica_histograma_notas(df, columna='Nota_Final', bins=10, titulo=None, figsize=(10, 6)):
    """Specialized wrapper using universal graph creator."""
    if titulo is None:
        titulo = 'Distribución de Notas Finales'
    
    style = GraphStyle(
        figsize=figsize,
        title=titulo,
        xlabel='Nota Final',
        ylabel='Frecuencia',
        colors=[COLORES['primario']]
    )
    
    return crear_grafica_universal(
        'hist',
        df[columna],
        None,
        style,
        bins=bins,
        threshold=3.0,
        threshold_colors={'below': COLORES['no_aprobado'], 'above': COLORES['aprobado']},
        threshold_label='Nota mínima (3.0)'
    )



def grafica_barras_por_corte(df, figsize=(12, 6)):
    """Specialized wrapper using universal graph creator."""
    estudiantes = (df['Nombres'] + ' ' + df['Apellidos'].str[0] + '.').tolist()
    
    data_dict = {
        'Corte 1 (30%)': df['Corte 1'].tolist(),
        'Corte 2 (30%)': df['Corte 2'].tolist(),
        'Corte 3 (40%)': df['Corte 3'].tolist()
    }
    
    style = GraphStyle(
        figsize=figsize,
        title='Notas por Corte de cada Estudiante',
        xlabel='Estudiantes',
        ylabel='Notas',
        colors=[COLORES['primario'], COLORES['secundario'], COLORES['info']]
    )
    
    return crear_grafica_universal(
        'grouped_bar',
        data_dict,
        estudiantes,
        style,
        rotation=45,
        add_hline=3.0,
        hline_label='Nota mínima (3.0)'
    )



def mostrar_estadisticas_tabla(df, columnas=None, estado_col='Estado'):
    """
    Universal statistics table display function.
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame with data
    columnas : list, optional
        Columns to analyze
    estado_col : str
        Status column name
    """
    if columnas is None:
        columnas = ['Corte 1', 'Corte 2', 'Corte 3', 'Nota_Final']
    
    def print_section(title, content, width=60):
        print("=" * width)
        print(title.upper())
        print("=" * width)
        print(content)
        print("=" * width)
    
    # Descriptive statistics
    print_section(
        "Estadísticas Descriptivas de las Notas",
        df[columnas].describe().round(2).to_string()
    )
    
    # Status summary
    print()
    if estado_col in df.columns:
        conteo = df[estado_col].value_counts()
        summary = [str(conteo)]
        summary.append(f"\nTotal de estudiantes: {len(df)}")
        
        for estado, cantidad in conteo.items():
            pct = (cantidad / len(df) * 100)
            summary.append(f"{estado}: {cantidad} ({pct:.2f}%)")
        
        print_section("Resumen de Aprobación", "\n".join(summary))


def guardar_grafica(fig, nombre_archivo, carpeta_output='data/output/img', 
                   formatos=['png', 'pdf'], dpi=300, verbose=True):
    """
    Universal graph saving function with multi-format support.
    
    Parameters:
    -----------
    fig : matplotlib.figure.Figure
        Figure to save
    nombre_archivo : str
        Filename without extension
    carpeta_output : str
        Output directory
    formatos : list
        Output formats ['png', 'pdf', 'svg', 'jpg']
    dpi : int
        Image resolution
    verbose : bool
        Print confirmation
    
    Returns:
    --------
    dict : {format: filepath}
    """
    import os
    
    os.makedirs(carpeta_output, exist_ok=True)
    
    saved_paths = {}
    for formato in formatos:
        filepath = os.path.join(carpeta_output, f"{nombre_archivo}.{formato}")
        save_kwargs = {'bbox_inches': 'tight'}
        
        if formato in ['png', 'jpg']:
            save_kwargs['dpi'] = dpi
        
        fig.savefig(filepath, **save_kwargs)
        saved_paths[formato] = filepath
    
    if verbose:
        print(f"✓ Gráfica guardada en:")
        for path in saved_paths.values():
            print(f"  - {path}")
    
    return saved_paths
