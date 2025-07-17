import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y, marker='o', linestyle='-', color='red')  # Custom line with markers
plt.xlabel("X Value")
plt.ylabel("Y = X Squared")
plt.title("Quadratic Plot: y = x²")
plt.grid(True)
plt.show()
