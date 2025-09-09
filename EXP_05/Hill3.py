import random

# Hill Climbing Algorithm
def hill_climbing(f, x_start, max_iterations=100):
    x = x_start
    for _ in range(max_iterations):
        # Neighbors are x-1 and x+1
        neighbors = [x-1, x+1]
        
        # Find best neighbor
        best_neighbor = max(neighbors, key=f)
        
        # If neighbor is better, move there
        if f(best_neighbor) > f(x):
            x = best_neighbor
        else:
            break   # stop when no better neighbor
        
    return x, f(x)

# Example 1: f(x) = -(x-3)^2 + 9
f1 = lambda x: -(x-3)**2 + 9

# Run hill climbing
print("Example 1:")
solution1 = hill_climbing(f1, x_start=0)
print("Max at x =", solution1[0], "f(x) =", solution1[1])

