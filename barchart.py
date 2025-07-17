import matplotlib.pyplot as plt

categories = ['Math', 'Physics', 'Chemistry', 'English']
scores = [85, 90, 78, 88]

plt.bar(categories, scores, color='skyblue')
plt.title("Bar Chart Example")
plt.xlabel("Subjects")
plt.ylabel("Scores")
plt.grid(axis='y')
plt.show()
