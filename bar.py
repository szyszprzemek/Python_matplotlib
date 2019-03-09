import matplotlib.pyplot as plt

population_ages = [22, 34, 45, 56, 67, 78, 90, 12, 3, 45, 67, 78, 111, 12, 110,100, 13, 34]

ids = [x for x in range(len(population_ages))]

plt.bar(ids, population_ages)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Graph bar")
plt.legend()
plt.show()