import sys
import os

# Add kalkulator-ai to path
kalkulator_path = r"C:\Users\LOQ\PycharmProjects\kalkulator-ai"
if kalkulator_path not in sys.path:
    sys.path.append(kalkulator_path)

from kalkulator_pkg.cli.handlers.evolution import handle_evolve

# Create a mock context
class MockContext:
    def __init__(self):
        self.banned_operators = set()
        self.function_registry = {}
        
ctx = MockContext()
csv_path = os.path.abspath("riemann_data_core.csv")
command = f"evolve f(x) from {csv_path} --hybrid --boost 3"
print(f"Running command: {command}")

# Run evolution
handle_evolve(command, ctx, variables={})
