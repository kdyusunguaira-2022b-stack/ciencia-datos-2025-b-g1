"""
Universal Graph System - Comprehensive Test Suite
Demonstrates the system works with ANY dataset type
"""

import sys
sys.path.append('..')

from function_graph_md import crear_grafica_universal, GraphStyle, COLORES, guardar_grafica
import numpy as np


def test_1_business_sales():
    """Test 1: Business sales data (not student grades!)"""
    print("\n" + "="*60)
    print("TEST 1: Business Sales Analysis")
    print("="*60)
    
    products = ['Laptop', 'Phone', 'Tablet', 'Watch', 'Headphones']
    sales = [45, 68, 32, 51, 39]
    
    style = GraphStyle(
        title='Product Sales Performance - Q4 2024',
        xlabel='Product Category',
        ylabel='Units Sold (Thousands)',
        colors=[COLORES['exito'], COLORES['primario'], COLORES['advertencia'], 
                COLORES['info'], COLORES['secundario']]
    )
    
    fig, ax = crear_grafica_universal('bar', sales, products, style)
    paths = guardar_grafica(fig, 'test_sales', formatos=['png'], verbose=False)
    print(f"✓ Created business sales bar chart: {paths['png']}")


def test_2_survey_pie():
    """Test 2: Survey response distribution"""
    print("\n" + "="*60)
    print("TEST 2: Customer Survey Results")
    print("="*60)
    
    responses = [156, 89, 34, 21]
    labels = ['Very Satisfied', 'Satisfied', 'Neutral', 'Dissatisfied']
    
    style = GraphStyle(
        title='Customer Satisfaction Survey - 300 Responses',
        figsize=(9, 9),
        colors=[COLORES['exito'], COLORES['aprobado'], 
                COLORES['advertencia'], COLORES['peligro']]
    )
    
    fig, ax = crear_grafica_universal('pie', responses, labels, style)
    paths = guardar_grafica(fig, 'test_survey', formatos=['png'], verbose=False)
    print(f"✓ Created survey pie chart: {paths['png']}")


def test_3_quality_histogram():
    """Test 3: Manufacturing quality control"""
    print("\n" + "="*60)
    print("TEST 3: Quality Control Distribution")
    print("="*60)
    
    # Simulated product measurements
    measurements = np.random.normal(100, 12, 1000)
    
    style = GraphStyle(
        title='Product Quality Distribution (n=1000)',
        xlabel='Measurement (mm)',
        ylabel='Frequency',
        figsize=(11, 6),
        colors=[COLORES['info']]
    )
    
    fig, ax = crear_grafica_universal(
        'hist',
        measurements,
        None,
        style,
        bins=25,
        threshold=95,
        threshold_colors={'below': COLORES['peligro'], 'above': COLORES['exito']},
        threshold_label='Quality Threshold (95mm)'
    )
    paths = guardar_grafica(fig, 'test_quality', formatos=['png'], verbose=False)
    print(f"✓ Created quality histogram: {paths['png']}")


def test_4_department_performance():
    """Test 4: Multi-department grouped comparison"""
    print("\n" + "="*60)
    print("TEST 4: Department Performance Comparison")
    print("="*60)
    
    departments = ['Engineering', 'Sales', 'Marketing', 'Support', 'HR']
    
    performance_data = {
        '2023': [78, 85, 72, 80, 88],
        '2024': [82, 89, 75, 83, 90],
        '2025 Target': [85, 92, 80, 87, 93]
    }
    
    style = GraphStyle(
        title='Department Performance - 3 Year Comparison',
        xlabel='Department',
        ylabel='Performance Score',
        figsize=(13, 7),
        colors=[COLORES['advertencia'], COLORES['primario'], COLORES['exito']]
    )
    
    fig, ax = crear_grafica_universal(
        'grouped_bar',
        performance_data,
        departments,
        style,
        rotation=0,
        add_hline=80,
        hline_label='Company Average (80)'
    )
    paths = guardar_grafica(fig, 'test_departments', formatos=['png'], verbose=False)
    print(f"✓ Created grouped bar chart: {paths['png']}")


def test_5_website_traffic():
    """Test 5: Website analytics trend"""
    print("\n" + "="*60)
    print("TEST 5: Website Traffic Trend")
    print("="*60)
    
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug']
    visitors = [12500, 15200, 14800, 18300, 21400, 19800, 23100, 25600]
    
    style = GraphStyle(
        title='Website Traffic Growth - 2024',
        xlabel='Month',
        ylabel='Unique Visitors',
        colors=[COLORES['primario']]
    )
    
    fig, ax = crear_grafica_universal(
        'line',
        visitors,
        months,
        style,
        marker='o',
        linewidth=3
    )
    paths = guardar_grafica(fig, 'test_traffic', formatos=['png'], verbose=False)
    print(f"✓ Created line chart: {paths['png']}")


def test_6_budget_allocation():
    """Test 6: Budget distribution"""
    print("\n" + "="*60)
    print("TEST 6: Budget Allocation")
    print("="*60)
    
    categories = ['Development', 'Marketing', 'Operations', 'Research', 'Admin']
    budget = [450000, 320000, 280000, 150000, 100000]
    
    style = GraphStyle(
        title='Annual Budget Distribution - $1.3M Total',
        figsize=(10, 10),
        colors=[COLORES['primario'], COLORES['info'], COLORES['secundario'],
                COLORES['advertencia'], COLORES['peligro']]
    )
    
    fig, ax = crear_grafica_universal('pie', budget, categories, style)
    paths = guardar_grafica(fig, 'test_budget', formatos=['png'], verbose=False)
    print(f"✓ Created budget pie chart: {paths['png']}")


def test_7_correlation_scatter():
    """Test 7: Feature correlation analysis"""
    print("\n" + "="*60)
    print("TEST 7: Feature Correlation Analysis")
    print("="*60)
    
    # Simulated correlation between advertising spend and revenue
    ad_spend = np.array([10, 15, 12, 20, 25, 18, 30, 22, 28, 35])
    revenue = ad_spend * 3.5 + np.random.normal(0, 5, 10)
    
    style = GraphStyle(
        title='Advertising Spend vs Revenue Correlation',
        xlabel='Ad Spend ($1000s)',
        ylabel='Revenue ($1000s)',
        colors=[COLORES['exito']],
        figsize=(10, 7)
    )
    
    fig, ax = crear_grafica_universal(
        'scatter',
        (ad_spend, revenue),
        None,
        style,
        size=150
    )
    paths = guardar_grafica(fig, 'test_correlation', formatos=['png'], verbose=False)
    print(f"✓ Created scatter plot: {paths['png']}")


def run_all_tests():
    """Execute all test cases"""
    print("\n" + "="*60)
    print("UNIVERSAL GRAPH SYSTEM - COMPREHENSIVE TEST SUITE")
    print("Testing with 7 different datasets (NOT student grades)")
    print("="*60)
    
    tests = [
        test_1_business_sales,
        test_2_survey_pie,
        test_3_quality_histogram,
        test_4_department_performance,
        test_5_website_traffic,
        test_6_budget_allocation,
        test_7_correlation_scatter
    ]
    
    passed = 0
    failed = 0
    
    for test_func in tests:
        try:
            test_func()
            passed += 1
        except Exception as e:
            print(f"✗ {test_func.__name__} FAILED: {e}")
            failed += 1
    
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    print(f"Total Tests: {len(tests)}")
    print(f"Passed: {passed} ✓")
    print(f"Failed: {failed} ✗")
    print(f"Success Rate: {passed/len(tests)*100:.1f}%")
    print("="*60)
    
    if failed == 0:
        print("\n🎉 ALL TESTS PASSED!")
        print("The universal system works with ANY dataset type!")
    else:
        print(f"\n⚠️ {failed} test(s) need attention")
    
    print("\nAll test outputs saved to: data/output/img/")
    print("="*60)


if __name__ == "__main__":
    run_all_tests()
