import numpy as np
import pandas as pd
from pulp import LpMinimize, LpProblem, LpVariable, lpSum
from scipy.optimize import linear_sum_assignment

def northwest_corner_method(supply, demand, costs):
    rows, cols = len(supply), len(demand)
    allocation = np.zeros((rows, cols))

    i, j = 0, 0

    while i < rows and j < cols:
        quantity = min(supply[i], demand[j])
        allocation[i, j] = quantity
        supply[i] -= quantity
        demand[j] -= quantity

        if supply[i] == 0:
            i += 1
        if demand[j] == 0:
            j += 1

    return allocation

# Початкові дані
supply = [230, 250, 170, 150]
demand = [140, 90, 160, 110, 150]
costs = np.array([
    [40, 19, 25, 25, 35],
    [49, 26, 27, 18, 38],
    [46, 27, 36, 40, 45],
    [140, 90, 160, 110, 150]
])

allocation = northwest_corner_method(supply, demand, costs)

print("Оптимальний розподіл:")
print(allocation)



