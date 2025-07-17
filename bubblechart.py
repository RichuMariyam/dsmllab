import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]
sizes = [100, 300, 500, 700, 900]  # Size of bubbles

plt.scatter(x, y, s=sizes, alpha=0.5, c='green')
plt.title("Bubble Chart Example")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True)
plt.show()
