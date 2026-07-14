import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize
from scipy.optimize import linprog

x_points = np.array([80,
75,
70,
65,
60,
55,
50,
45])
y_points = np.array([10.2,
10,
9.9,
9.9,
9.8,
9.7,
9.6,
9.5])

y_error = np.array([0.1,
    0.1,
    0.1,
    0.1,
    0.1,
    0.1,
    0.1,
    0.1])

y_large = y_points+y_error
y_small = -y_points+y_error

A_upper = np.column_stack((x_points, np.ones(len(x_points))))
A_lower = -A_upper

A = np.vstack((A_upper,A_lower))

b = np.concatenate((y_large,y_small))

result = linprog(
    [-1,0],
    A_ub=A,
    b_ub=b,
    bounds=[(None,None),(None,None)]

gradient = result.x[0]
intercept = result.x[1]
print("largest gradient is:",gradient,".Smallest intercept is:",intercept)

fig, ax = plt.subplots()
ax.errorbar(x_points,y_points,y_error)
x = np.linspace(x_points[0],x_points[-1],100)
y = gradient*x+intercept
plt.plot(x, y, '-r', label='largest')
plt.show()

