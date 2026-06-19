import sys
import numpy as np
from sympy import mobius

sys.path.append("C:/Users/LOQ/PycharmProjects/kalkulator-ai")
from kalkulator_pkg.symbolic_regression.genetic_engine import GeneticSymbolicRegressor
from kalkulator_pkg.symbolic_regression.genetic_config import GeneticConfig

def main():
    print("Generating pure discrete target data: y = moebius(x) / x")
    X = np.arange(1, 50).reshape(-1, 1)
    
    # Generate exact discrete data
    y_discrete = np.array([float(mobius(int(x[0]))) / float(x[0]) for x in X])

    config = GeneticConfig(
        population_size=1000,
        generations=20,
        operators=["add", "sub", "mul", "div", "moebius"],
        loss_function="mse",
        constant_optimization_rate=0.0
    )

    reg = GeneticSymbolicRegressor(config=config)
    
    print("\n--- Running Kalkulator-AI on Pure Discrete Data ---")
    reg.fit(X, y_discrete, variable_names=["x"])
    
    expr = reg.get_expression()
    print(f"\nFinal Equation Discovered by Kalkulator-AI: {expr}")

if __name__ == "__main__":
    main()
