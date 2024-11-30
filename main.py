import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
import plot_functions

def test_should_plot_normal_distribution():
    data = plot_functions.plot_normal_distribution()
    assert len(data) == 200  # Ensure 200 points are generated
    assert np.isclose(np.mean(data), 0, atol=0.5)  
    assert np.isclose(np.std(data), 1, atol=0.5)  


