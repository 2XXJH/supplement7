import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
import sys
sys.path.append(".")
from src import plot_functions
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))









def test_should_plot_normal_distribution():
    data = plot_functions.plot_normal_distribution()
    assert len(data) == 200  # Ensure 200 points are generated
    assert np.isclose(np.mean(data), 0, atol=0.5)  
    assert np.isclose(np.std(data), 1, atol=0.5)  

def test_should_plot_line():
    try:
        plot_functions.plot_line(2, 1, -10, 10)
    except Exception as e:
        assert False, f"plot_line raised an exception: {e}"
