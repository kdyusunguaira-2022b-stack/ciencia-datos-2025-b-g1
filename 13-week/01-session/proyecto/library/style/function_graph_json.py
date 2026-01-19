"""
Generic Graph Styling Module - Refactored
Author: Proyecto Corhuila
Date: 2025

This module provides reusable, modular functions for creating 
professional visualizations with consistent styling.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from typing import Optional, Tuple, Dict, List, Any

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

# Default style configuration
DEFAULT_STYLE = {
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


def configurar_estilo_global(style: str = "whitegrid", custom_params: Optional[Dict] = None):
    """
    Configure global styling for all visualizations.
    
    Parameters:
    -----------
    style : str
        Seaborn style preset ('whitegrid', 'darkgrid', 'white', 'dark', 'ticks')
    custom_params : dict, optional
        Custom matplotlib parameters to override defaults
    
    Example:
    --------
    >>> configurar_estilo_global()
    >>> configurar_estilo_global('dark', {'font.size': 12})
    """
    sns.set_style(style)
    params = {**DEFAULT_STYLE, **(custom_params or {})}
    plt.rcParams.update(params)



def _setup_figure(figsize: Tuple[int, int]) -> Tuple[plt.Figure, plt.Axes]:
    """Helper function to create figure and axes."""
    return plt.subplots(figsize=figsize)


def _add_value_labels(ax: plt.Axes, bars: Any, values: List, 
                       format_func: Optional[callable] = None,
                       fontsize: int = 12, **kwargs):
    """
    Generic function to add value labels on bars.
    
    Parameters:
    -----------
    ax : matplotlib axes
        The axes object
    bars : bar container
        The bar objects
    values : list
        Values to display
    format_func : callable, optional
        Function to format the label text
    fontsize : int
        Font size for labels
    """
    for bar, value in zip(bars, values):
        height = bar.get_height()
        label = format_func(value) if format_func else str(value)
        ax.text(bar.get_x() + bar.get_width()/2., height,
                label, ha='center', va='bottom', 
                fontsize=fontsize, fontweight='bold', **kwargs)


def _configure_axes(ax: plt.Axes, xlabel: str = '', ylabel: str = '', 
                    title: str = '', grid_axis: str = 'y', **kwargs):
    """
    Generic function to configure axes properties.
    
    Parameters:
    -----------
    ax : matplotlib axes
        The axes object to configure
    xlabel : str
        X-axis label
    ylabel : str
        Y-axis label
    title : str
        Plot title
    grid_axis : str
        Axis for grid ('x', 'y', 'both')
    """
    if xlabel:
        ax.set_xlabel(xlabel, fontsize=12, fontweight='bold')
    if ylabel:
        ax.set_ylabel(ylabel, fontsize=12, fontweight='bold')
    if title:
        ax.set_title(title, fontsize=14, fontweight='bold')
    
    ax.grid(axis=grid_axis, alpha=0.3)
    plt.tight_layout()


def crear_grafica_barras(data: Any, labels: List[str], 
                         colors: Optional[List[str]] = None,
                         title: str = '', xlabel: str = '', ylabel: str = '',
                         show_values: bool = True, 
                         value_format: Optional[callable] = None,
                         figsize: Tuple[int, int] = (10, 6),
                         **kwargs) -> Tuple[plt.Figure, plt.Axes]:
    """
    Generic bar chart creator with full customization.
    
    Parameters:
    -----------
    data : array-like
        Data values for bars
    labels : list
        Labels for each bar
    colors : list, optional
        Colors for bars (defaults to color scheme)
    title : str
        Chart title
    xlabel : str
        X-axis label
    ylabel : str
        Y-axis label
    show_values : bool
        Whether to show values on bars
    value_format : callable, optional
        Function to format value labels
    figsize : tuple
        Figure size (width, height)
    **kwargs : dict
        Additional bar plot parameters
    
    Returns:
    --------
    fig, ax : matplotlib figure and axes
    
    Example:
    --------
    >>> data = [10, 20, 15]
    >>> labels = ['A', 'B', 'C']
    >>> fig, ax = crear_grafica_barras(data, labels, title='My Chart')
    """
    fig, ax = _setup_figure(figsize)
    
    # Default colors if not provided
    if colors is None:
        colors = [COLORES['primario']] * len(data)
    
    # Create bars
    bars = ax.bar(labels, data, color=colors, alpha=0.7, 
                  edgecolor='black', linewidth=2, **kwargs)
    
    # Add value labels
    if show_values:
        _add_value_labels(ax, bars, data, value_format)
    
    # Configure axes
    _configure_axes(ax, xlabel, ylabel, title)
    
    return fig, ax


def grafica_barras_aprobados(conteo_estado, total_estudiantes, 
                             titulo: Optional[str] = None, 
                             figsize: Tuple[int, int] = (10, 6)) -> Tuple[plt.Figure, plt.Axes]:
    """
    Bar chart for approved vs not approved students (specialized wrapper).
    
    Parameters:
    -----------
    conteo_estado : pd.Series
        Count of approved and not approved students
    total_estudiantes : int
        Total number of students
    titulo : str, optional
        Custom title
    figsize : tuple
        Figure size
    
    Returns:
    --------
    fig, ax : matplotlib figure and axes
    """
    colors = [COLORES['aprobado'], COLORES['no_aprobado']]
    
    if titulo is None:
        titulo = 'Distribución de Estudiantes: Aprobados vs No Aprobados\n(Corte 1: 30%, Corte 2: 30%, Corte 3: 40%)'
    
    # Custom format function for percentages
    def format_label(value):
        return f'{int(value)}\n({value/total_estudiantes*100:.1f}%)'
    
    return crear_grafica_barras(
        data=conteo_estado.values,
        labels=conteo_estado.index,
        colors=colors,
        title=titulo,
        xlabel='Estado',
        ylabel='Cantidad de Estudiantes',
        value_format=format_label,
        figsize=figsize
    )



def crear_grafica_pastel(data: Any, labels: List[str],
                         colors: Optional[List[str]] = None,
                         title: str = '',
                         explode: Optional[Tuple] = None,
                         autopct: str = '%1.1f%%',
                         figsize: Tuple[int, int] = (8, 8),
                         **kwargs) -> Tuple[plt.Figure, plt.Axes]:
    """
    Generic pie chart creator with full customization.
    
    Parameters:
    -----------
    data : array-like
        Data values for pie slices
    labels : list
        Labels for each slice
    colors : list, optional
        Colors for slices
    title : str
        Chart title
    explode : tuple, optional
        Explode values for each slice
    autopct : str
        Format string for percentage display
    figsize : tuple
        Figure size
    **kwargs : dict
        Additional pie plot parameters
    
    Returns:
    --------
    fig, ax : matplotlib figure and axes
    
    Example:
    --------
    >>> data = [30, 70]
    >>> labels = ['Failed', 'Passed']
    >>> fig, ax = crear_grafica_pastel(data, labels, title='Results')
    """
    fig, ax = _setup_figure(figsize)
    
    # Default colors
    if colors is None:
        colors = [COLORES['primario'], COLORES['secundario']]
    
    # Default explode
    if explode is None:
        explode = tuple([0.05] * len(data))
    
    # Create pie chart
    ax.pie(data, labels=labels, autopct=autopct,
           startangle=90, colors=colors, explode=explode,
           shadow=True, textprops={'fontsize': 12, 'fontweight': 'bold'},
           **kwargs)
    
    if title:
        ax.set_title(title, fontsize=14, fontweight='bold', pad=20)
    
    ax.axis('equal')
    plt.tight_layout()
    
    return fig, ax


def grafica_pastel_aprobados(conteo_estado, titulo: Optional[str] = None, 
                             figsize: Tuple[int, int] = (8, 8)) -> Tuple[plt.Figure, plt.Axes]:
    """
    Pie chart for approved vs not approved students (specialized wrapper).
    
    Parameters:
    -----------
    conteo_estado : pd.Series
        Count of approved and not approved students
    titulo : str, optional
        Custom title
    figsize : tuple
        Figure size
    
    Returns:
    --------
    fig, ax : matplotlib figure and axes
    """
    colors = [COLORES['aprobado'], COLORES['no_aprobado']]
    
    if titulo is None:
        titulo = 'Proporción de Estudiantes Aprobados vs No Aprobados\n(Nota mínima: 3.0)'
    
    return crear_grafica_pastel(
        data=conteo_estado.values,
        labels=conteo_estado.index,
        colors=colors,
        title=titulo,
        figsize=figsize
    )



def crear_histograma(data: Any, bins: int = 10,
                     title: str = '', xlabel: str = '', ylabel: str = 'Frecuencia',
                     color: Optional[str] = None,
                     threshold: Optional[float] = None,
                     threshold_colors: Optional[Dict[str, str]] = None,
                     threshold_label: Optional[str] = None,
                     figsize: Tuple[int, int] = (10, 6),
                     **kwargs) -> Tuple[plt.Figure, plt.Axes]:
    """
    Generic histogram creator with threshold coloring support.
    
    Parameters:
    -----------
    data : array-like
        Data to plot
    bins : int
        Number of bins
    title : str
        Chart title
    xlabel : str
        X-axis label
    ylabel : str
        Y-axis label
    color : str, optional
        Default color for bars
    threshold : float, optional
        Threshold value for conditional coloring
    threshold_colors : dict, optional
        Colors for values {'below': color, 'above': color}
    threshold_label : str, optional
        Label for threshold line
    figsize : tuple
        Figure size
    **kwargs : dict
        Additional histogram parameters
    
    Returns:
    --------
    fig, ax : matplotlib figure and axes
    
    Example:
    --------
    >>> data = np.random.normal(3.5, 0.5, 100)
    >>> fig, ax = crear_histograma(data, bins=15, threshold=3.0,
    ...                             threshold_colors={'below': 'red', 'above': 'green'})
    """
    fig, ax = _setup_figure(figsize)
    
    # Default color
    if color is None:
        color = COLORES['primario']
    
    # Create histogram
    n, bins_edges, patches = ax.hist(data, bins=bins, color=color,
                                      alpha=0.7, edgecolor='black', 
                                      linewidth=1.5, **kwargs)
    
    # Apply threshold coloring if specified
    if threshold is not None and threshold_colors:
        for i, patch in enumerate(patches):
            if bins_edges[i] < threshold:
                patch.set_facecolor(threshold_colors.get('below', color))
            else:
                patch.set_facecolor(threshold_colors.get('above', color))
        
        # Add threshold line
        if threshold_label:
            ax.axvline(x=threshold, color='red', linestyle='--', 
                      linewidth=2, label=threshold_label)
            ax.legend()
    
    # Configure axes
    _configure_axes(ax, xlabel, ylabel, title)
    
    return fig, ax


def grafica_histograma_notas(df, columna: str = 'Nota_Final', bins: int = 10,
                             titulo: Optional[str] = None,
                             figsize: Tuple[int, int] = (10, 6)) -> Tuple[plt.Figure, plt.Axes]:
    """
    Histogram for grade distribution (specialized wrapper).
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame with data
    columna : str
        Column name with grades
    bins : int
        Number of bins
    titulo : str, optional
        Custom title
    figsize : tuple
        Figure size
    
    Returns:
    --------
    fig, ax : matplotlib figure and axes
    """
    if titulo is None:
        titulo = 'Distribución de Notas Finales'
    
    return crear_histograma(
        data=df[columna],
        bins=bins,
        title=titulo,
        xlabel='Nota Final',
        ylabel='Frecuencia',
        threshold=3.0,
        threshold_colors={'below': COLORES['no_aprobado'], 'above': COLORES['aprobado']},
        threshold_label='Nota mínima (3.0)',
        figsize=figsize
    )



def crear_barras_agrupadas(data_dict: Dict[str, List], labels: List[str],
                           colors: Optional[List[str]] = None,
                           title: str = '', xlabel: str = '', ylabel: str = '',
                           bar_width: float = 0.25,
                           add_hline: Optional[float] = None,
                           hline_label: Optional[str] = None,
                           rotation: int = 0,
                           figsize: Tuple[int, int] = (12, 6),
                           **kwargs) -> Tuple[plt.Figure, plt.Axes]:
    """
    Generic grouped bar chart creator.
    
    Parameters:
    -----------
    data_dict : dict
        Dictionary with {group_name: values_list}
    labels : list
        Labels for x-axis categories
    colors : list, optional
        Colors for each group
    title : str
        Chart title
    xlabel : str
        X-axis label
    ylabel : str
        Y-axis label
    bar_width : float
        Width of each bar
    add_hline : float, optional
        Y value for horizontal reference line
    hline_label : str, optional
        Label for horizontal line
    rotation : int
        Rotation angle for x-axis labels
    figsize : tuple
        Figure size
    **kwargs : dict
        Additional bar plot parameters
    
    Returns:
    --------
    fig, ax : matplotlib figure and axes
    
    Example:
    --------
    >>> data = {'Group A': [1, 2, 3], 'Group B': [4, 5, 6]}
    >>> labels = ['X', 'Y', 'Z']
    >>> fig, ax = crear_barras_agrupadas(data, labels)
    """
    fig, ax = _setup_figure(figsize)
    
    # Calculate positions
    x = np.arange(len(labels))
    num_groups = len(data_dict)
    offset = bar_width * (num_groups - 1) / 2
    
    # Default colors
    if colors is None:
        color_keys = ['primario', 'secundario', 'info', 'exito', 'advertencia']
        colors = [COLORES[key] for key in color_keys[:num_groups]]
    
    # Create bars for each group
    for i, (group_name, values) in enumerate(data_dict.items()):
        position = x - offset + (i * bar_width)
        ax.bar(position, values, bar_width, label=group_name,
               color=colors[i % len(colors)], alpha=0.8, **kwargs)
    
    # Add horizontal line if specified
    if add_hline is not None:
        ax.axhline(y=add_hline, color='red', linestyle='--', 
                   linewidth=1.5, label=hline_label or '')
    
    # Configure axes
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=rotation, ha='right' if rotation > 0 else 'center')
    ax.legend()
    _configure_axes(ax, xlabel, ylabel, title)
    
    return fig, ax


def grafica_barras_por_corte(df, figsize: Tuple[int, int] = (12, 6)) -> Tuple[plt.Figure, plt.Axes]:
    """
    Grouped bar chart for grades by evaluation period (specialized wrapper).
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame with student data
    figsize : tuple
        Figure size
    
    Returns:
    --------
    fig, ax : matplotlib figure and axes
    """
    # Prepare data
    estudiantes = df['Nombres'] + ' ' + df['Apellidos'].str[0] + '.'
    
    data_dict = {
        'Corte 1 (30%)': df['Corte 1'].tolist(),
        'Corte 2 (30%)': df['Corte 2'].tolist(),
        'Corte 3 (40%)': df['Corte 3'].tolist()
    }
    
    return crear_barras_agrupadas(
        data_dict=data_dict,
        labels=estudiantes.tolist(),
        colors=[COLORES['primario'], COLORES['secundario'], COLORES['info']],
        title='Notas por Corte de cada Estudiante',
        xlabel='Estudiantes',
        ylabel='Notas',
        add_hline=3.0,
        hline_label='Nota mínima (3.0)',
        rotation=45,
        figsize=figsize
    )



def imprimir_tabla_formateada(titulo: str, contenido: str, ancho: int = 60):
    """
    Generic function to print formatted tables.
    
    Parameters:
    -----------
    titulo : str
        Table title
    contenido : str
        Table content
    ancho : int
        Width of the table border
    
    Example:
    --------
    >>> imprimir_tabla_formateada("Results", "Data here")
    """
    print("=" * ancho)
    print(titulo.upper())
    print("=" * ancho)
    print(contenido)
    print("=" * ancho)


def mostrar_estadisticas_tabla(df, columnas: Optional[List[str]] = None,
                               estado_col: str = 'Estado'):
    """
    Display formatted statistical tables for any dataset.
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame with student data
    columnas : list, optional
        Columns to include in statistics (defaults to grade columns)
    estado_col : str
        Column name containing status/state information
    
    Example:
    --------
    >>> mostrar_estadisticas_tabla(df)
    >>> mostrar_estadisticas_tabla(df, columnas=['Score1', 'Score2'])
    """
    # Default columns
    if columnas is None:
        columnas = ['Corte 1', 'Corte 2', 'Corte 3', 'Nota_Final']
    
    # Descriptive statistics
    estadisticas = df[columnas].describe()
    imprimir_tabla_formateada(
        "Estadísticas Descriptivas de las Notas",
        estadisticas.round(2).to_string()
    )
    
    # Status summary
    print()
    if estado_col in df.columns:
        conteo = df[estado_col].value_counts()
        
        summary_lines = [str(conteo)]
        summary_lines.append(f"\nTotal de estudiantes: {len(df)}")
        
        for estado, cantidad in conteo.items():
            porcentaje = (cantidad / len(df) * 100)
            summary_lines.append(f"{estado}: {cantidad} ({porcentaje:.2f}%)")
        
        imprimir_tabla_formateada(
            "Resumen de Aprobación",
            "\n".join(summary_lines)
        )



def guardar_grafica(fig: plt.Figure, nombre_archivo: str,
                   carpeta_output: str = 'data/output/img',
                   formatos: List[str] = ['png', 'pdf'],
                   dpi: int = 300,
                   verbose: bool = True) -> Dict[str, str]:
    """
    Save figure to multiple formats with full customization.
    
    Parameters:
    -----------
    fig : matplotlib figure
        Figure to save
    nombre_archivo : str
        Filename (without extension)
    carpeta_output : str
        Output directory path
    formatos : list
        List of output formats ('png', 'pdf', 'svg', 'jpg')
    dpi : int
        Image resolution
    verbose : bool
        Whether to print save confirmation
    
    Returns:
    --------
    dict : Dictionary with {format: filepath}
    
    Example:
    --------
    >>> fig, ax = plt.subplots()
    >>> paths = guardar_grafica(fig, 'my_chart', formatos=['png', 'svg'])
    """
    import os
    
    # Create directory if it doesn't exist
    os.makedirs(carpeta_output, exist_ok=True)
    
    saved_paths = {}
    
    # Save in each format
    for formato in formatos:
        filepath = os.path.join(carpeta_output, f"{nombre_archivo}.{formato}")
        
        save_kwargs = {'bbox_inches': 'tight'}
        if formato in ['png', 'jpg']:
            save_kwargs['dpi'] = dpi
        
        fig.savefig(filepath, **save_kwargs)
        saved_paths[formato] = filepath
    
    # Print confirmation
    if verbose:
        print(f"✓ Gráfica guardada en:")
        for formato, path in saved_paths.items():
            print(f"  - {path}")
    
    return saved_paths
