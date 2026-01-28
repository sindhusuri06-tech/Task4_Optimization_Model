from pulp import *

# Create optimization problem
model = LpProblem("Production_Optimization", LpMaximize)

# Decision variables
A = LpVariable('Product_A', lowBound=0, cat='Continuous')
B = LpVariable('Product_B', lowBound=0, cat='Continuous')

# Objective function
model += 40 * A + 30 * B, "Maximize_Profit"

# Constraints
model += A <= 40
model += B <= 30
model += A + B <= 60

# Solve problem
model.solve()

# Results
print("Status:", LpStatus[model.status])
print("Optimal Production of Product A:", A.varValue)
print("Optimal Production of Product B:", B.varValue)
print("Maximum Profit:", value(model.objective))
