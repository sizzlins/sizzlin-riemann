import sys
import os
import pandas as pd
import numpy as np
import sympy as sp

sys.path.append("C:/Users/LOQ/PycharmProjects/kalkulator-ai")
from kalkulator_pkg.symbolic_regression.genetic_engine import GeneticSymbolicRegressor
from kalkulator_pkg.symbolic_regression.genetic_config import GeneticConfig

def main():
    csv_path = os.path.join(os.path.dirname(__file__), 'detrended_results.csv')
    try:
        df = pd.read_csv(csv_path)
    except FileNotFoundError:
        print(f"File not found: {csv_path}. Please run exact_vasyunin_solver.py first.")
        return

    # Use N=100 dataset
    df_100 = df[df['N'] == 100].copy()
    X = df_100[['k']].values
    
    # Calculate totient(k) and envelope
    df_100['totient'] = df_100['k'].apply(lambda x: int(sp.totient(x)))
    df_100['envelope'] = np.sqrt(df_100['totient'])

    # Calculate residuals R_k = (a_k * k) / sqrt(totient(k))
    df_100['R_k'] = df_100['y_detrended'] / df_100['envelope']
    y_res = df_100['R_k'].values

    # We want to find the oscillator. 
    # Because it might have a constant scaling factor, we allow some constant optimization.
    config = GeneticConfig(
        population_size=1000,
        generations=100,
        operators=["add", "sub", "mul", "div", "pow", "moebius", "omega", "big_omega", "totient", "prime_pi"],
        loss_function="huber",                # Exact values matter now, not just correlation
        constant_optimization_rate=0.1,       # Allow scaling to find the amplitude
        n_jobs=1,                             # Force serial execution
        n_islands=1,
        verbose=True,
    )
    
    print(f"Starting Phase 5: Residual AST Search (N=100)...")
    print("Optimization: Huber Loss, BFGS Enabled.")
    regressor = GeneticSymbolicRegressor(config)
    regressor.fit(X, y_res, variable_names=["k"])
    
    best_expr = regressor.pareto_front.get_best()
    if best_expr:
        print("\n" + "="*50)
        print(f"Discovered Prime Oscillator for R_k: {best_expr.expression}")
        print(f"Loss Score (Huber): {best_expr.mse}")
        print("="*50)
    else:
        print("Failed to find a valid equation.")

if __name__ == '__main__':
    main()
