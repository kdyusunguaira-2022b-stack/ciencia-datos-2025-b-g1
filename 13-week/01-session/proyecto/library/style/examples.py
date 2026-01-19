"""
Examples of using the refactored generic graph functions
========================================================

This file demonstrates how to use the generic visualization
functions for different types of data and use cases.
"""

import pandas as pd
import numpy as np
from style.function_graph_json import (
    configurar_estilo_global,
    crear_grafica_barras,
    crear_grafica_pastel,
    crear_histograma,
    crear_barras_agrupadas,
    guardar_grafica,
    COLORES
)

# Configure global style
configurar_estilo_global()

# ========================================
# Example 1: Simple Bar Chart
# ========================================
print("Example 1: Sales by Product")

products = ['Product A', 'Product B', 'Product C', 'Product D']
sales = [2500, 3200, 2800, 3500]

fig, ax = crear_grafica_barras(
    data=sales,
    labels=products,
    title='Monthly Sales by Product',
    xlabel='Products',
    ylabel='Sales ($)',
    colors=[COLORES['primario'], COLORES['exito'], 
            COLORES['info'], COLORES['secundario']],
    show_values=True,
    value_format=lambda x: f'${int(x)}'
)
guardar_grafica(fig, 'example_sales_bar')

# ========================================
# Example 2: Pie Chart for Budget
# ========================================
print("\nExample 2: Budget Allocation")

categories = ['Marketing', 'R&D', 'Operations', 'Sales']
budget = [30000, 45000, 35000, 40000]

fig, ax = crear_grafica_pastel(
    data=budget,
    labels=categories,
    title='Annual Budget Allocation',
    colors=[COLORES['advertencia'], COLORES['primario'], 
            COLORES['exito'], COLORES['secundario']]
)
guardar_grafica(fig, 'example_budget_pie')

# ========================================
# Example 3: Histogram with Threshold
# ========================================
print("\nExample 3: Quality Control Measurements")

# Generate sample quality measurements
np.random.seed(42)
measurements = np.random.normal(100, 15, 500)

fig, ax = crear_histograma(
    data=measurements,
    bins=25,
    title='Product Quality Measurements',
    xlabel='Measurement Value',
    ylabel='Frequency',
    threshold=90,
    threshold_colors={'below': COLORES['peligro'], 
                     'above': COLORES['exito']},
    threshold_label='Minimum Quality Standard (90)'
)
guardar_grafica(fig, 'example_quality_histogram')

# ========================================
# Example 4: Grouped Bar Chart
# ========================================
print("\nExample 4: Quarterly Performance Comparison")

quarters_data = {
    'Q1 2024': [85, 92, 78, 88],
    'Q2 2024': [88, 95, 82, 91],
    'Q3 2024': [92, 98, 85, 94],
    'Q4 2024': [95, 99, 88, 96]
}
teams = ['Team Alpha', 'Team Beta', 'Team Gamma', 'Team Delta']

fig, ax = crear_barras_agrupadas(
    data_dict=quarters_data,
    labels=teams,
    title='Team Performance by Quarter (Scores)',
    xlabel='Teams',
    ylabel='Performance Score',
    colors=[COLORES['primario'], COLORES['secundario'], 
            COLORES['info'], COLORES['exito']],
    add_hline=90,
    hline_label='Target Score (90)',
    rotation=0
)
guardar_grafica(fig, 'example_performance_grouped')

# ========================================
# Example 5: Custom Formatted Bar Chart
# ========================================
print("\nExample 5: Website Traffic Analysis")

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
visitors = [45000, 52000, 48000, 61000, 58000, 65000]

# Custom format function for thousands
def format_thousands(value):
    return f'{int(value/1000)}K\n(+{((value/45000)-1)*100:.1f}%)'

fig, ax = crear_grafica_barras(
    data=visitors,
    labels=months,
    title='Website Monthly Visitors (H1 2024)',
    xlabel='Month',
    ylabel='Unique Visitors',
    color=COLORES['info'],
    show_values=True,
    value_format=format_thousands
)
guardar_grafica(fig, 'example_traffic_bar')

# ========================================
# Example 6: Multi-Dataset Comparison
# ========================================
print("\nExample 6: Revenue vs Expenses Comparison")

months_comparison = {
    'Revenue': [120, 135, 142, 158, 165, 178],
    'Expenses': [80, 85, 88, 95, 98, 102],
    'Profit': [40, 50, 54, 63, 67, 76]
}
months_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

fig, ax = crear_barras_agrupadas(
    data_dict=months_comparison,
    labels=months_labels,
    title='Financial Performance Comparison (in $1000s)',
    xlabel='Month',
    ylabel='Amount ($1000)',
    colors=[COLORES['exito'], COLORES['peligro'], COLORES['primario']],
    bar_width=0.25,
    rotation=0
)
guardar_grafica(fig, 'example_financial_grouped')

# ========================================
# Example 7: Distribution Analysis
# ========================================
print("\nExample 7: Customer Age Distribution")

# Generate sample age data
np.random.seed(123)
ages = np.concatenate([
    np.random.normal(35, 8, 300),  # Main customer base
    np.random.normal(55, 10, 150)  # Secondary segment
])

fig, ax = crear_histograma(
    data=ages,
    bins=30,
    title='Customer Age Distribution',
    xlabel='Age (years)',
    ylabel='Number of Customers',
    color=COLORES['secundario'],
    threshold=45,
    threshold_colors={'below': COLORES['info'], 
                     'above': COLORES['advertencia']},
    threshold_label='Segment Boundary (45 years)'
)
guardar_grafica(fig, 'example_age_distribution')

print("\n" + "="*50)
print("All examples completed successfully!")
print("Check the 'data/output/img/' folder for saved charts")
print("="*50)
