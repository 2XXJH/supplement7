import numpy as np
import matplotlib.pyplot as plt


def plot_normal_distribution():
    """
    Plots 200 points sampled from a standard normal distribution (mean = 0, std dev = 1).
    
    This function generates 200 points randomly sampled from a standard normal distribution and
    displays them on a scatter plot. The x-axis represents the index of each point, and the y-axis
    represents the corresponding values from the distribution.
    
    Returns:
        numpy.ndarray: The 200 sampled points from the normal distribution.
    
    Example:
        data = plot_normal_distribution()
    """
    data = np.random.normal(0, 1, 200)
    plt.scatter(range(len(data)), data, alpha=0.7)
    plt.title("200 Points from a Standard Normal Distribution")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.grid(True)
    plt.show()
    return data

def plot_line(y_intercept, slope, x_min, x_max):
    """
    Plots a line defined by a given y-intercept, slope, and x-boundaries.
    
    This function generates a line plot based on the equation y = slope * x + y_intercept, where
    the x-values range from x_min to x_max. The plot will be displayed with labels and a legend.
    
    Args:
        y_intercept (float): The y-intercept of the line.
        slope (float): The slope of the line.
        x_min (float): The lower bound of the x-values.
        x_max (float): The upper bound of the x-values.
    
    Example:
        plot_line(2, 1, -10, 10)
    """
    x = np.linspace(x_min, x_max, 500)
    y = slope * x + y_intercept
    plt.plot(x, y, label=f"y = {slope}x + {y_intercept}")
    plt.xlim(x_min, x_max)
    plt.title("Line Plot")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()
