import numpy as np
import matplotlib.pyplot as plt


def plot_normal_distribution():
    data = np.random.normal(0, 1, 200)
    plt.scatter(range(len(data)), data, alpha=0.7)
    plt.title("200 Points from a Standard Normal Distribution")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.grid(True)
    plt.show()
    return data
