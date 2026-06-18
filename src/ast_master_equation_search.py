import sys
import os
import pandas as pd

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
    
    # RE-TARGET: We previously detrended y by doing a_k * k. 
    # To get raw a_k, we divide by k.
    y = df_100['y_detrended'].values / df_100['k'].values

    config = GeneticConfig(
        population_size=1000,
        generations=100,
        operators=["add", "sub", "mul", "div", "pow", "moebius", "omega", "big_omega", "totient"],
        loss_function="pearson",              # Structural shape search
        constant_optimization_rate=0.0,       # Disable BFGS lazy constants
        n_jobs=1,                             # Force serial execution
        n_islands=1,
        verbose=True,
    )
    
    print(f"Starting AST Structural Search on Raw a_k target (N=100)...")
    print("Optimization: Pearson Correlation, BFGS Disabled.")
    regressor = GeneticSymbolicRegressor(config)
    regressor.fit(X, y, variable_names=["k"])
    
    best_expr = regressor.pareto_front.get_best()
    if best_expr:
        print("\n" + "="*50)
        print(f"Discovered Structural DNA for a_k: {best_expr.expression}")
        print(f"Loss Score (1 - |r|): {best_expr.mse}")
        print("="*50)
    else:
        print("Failed to find a valid equation.")

if __name__ == '__main__':
    main()
