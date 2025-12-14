import numpy as np
import matplotlib.pyplot as plt

# Système :
# x1 - 2 x2 = -1
# -x1 + 3 x2 = 3

A = np.array([[ 1, -2],
              [-1,  3]], dtype=float)
b = np.array([-1, 3], dtype=float)

# Solution (x1, x2)
x1_sol, x2_sol = np.linalg.solve(A, b)
print("Solution :", (x1_sol, x2_sol))

# Paramètre pour tracer (axe horizontal = x1)
x1 = np.linspace(-2, 6, 400)

# Droite 1 : x1 - 2x2 = -1  ->  x2 = (x1 + 1)/2
x2_l1 = (x1 + 1) / 2

# Droite 2 : -x1 + 3x2 = 3  ->  x2 = (x1 + 3)/3
x2_l2 = (x1 + 3) / 3

plt.figure(figsize=(7, 4.5))
plt.plot(x1, x2_l1, label=r"$\ell_1: x_1 - 2x_2 = -1$")
plt.plot(x1, x2_l2, label=r"$\ell_2: -x_1 + 3x_2 = 3$")

# Point d'intersection
plt.scatter([x1_sol], [x2_sol], zorder=5)
plt.annotate(f"({x1_sol:.0f}, {x2_sol:.0f})", (x1_sol, x2_sol),
             textcoords="offset points", xytext=(8, 8))

# Axes qui se croisent en (0,0) comme sur la figure
ax = plt.gca()
ax.spines["left"].set_position("zero")
ax.spines["bottom"].set_position("zero")
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")
ax.set_xlabel(r"$x_1$")
ax.set_ylabel(r"$x_2$", rotation=0, labelpad=10)

plt.xlim(-2, 6)
plt.ylim(-2, 4)
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()
