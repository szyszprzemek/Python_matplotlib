import matplotlib.pyplot as plt

x = [1,2,3]
y = [5,7,4]

x2 = [1,2,3]
y2 = [10,14,12]

plt.plot(x,y,label="Accel")
plt.plot(x2,y2,label="Accel2")
plt.xlabel("Time [s]")
plt.ylabel("Accel [g]")
plt.title("Test graph")
plt.legend()
plt.show()
