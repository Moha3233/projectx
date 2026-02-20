import numpy as np
import matplotlib.pyplot as plt

class EnergyFunnel:

    def generate_funnel(self, base_energy):
        x = np.linspace(0, 10, 100)
        y = base_energy - np.log(x + 1) * 10

        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_title("Energy Funnel Simulation")
        ax.set_xlabel("Conformational Search")
        ax.set_ylabel("Energy")

        return fig
