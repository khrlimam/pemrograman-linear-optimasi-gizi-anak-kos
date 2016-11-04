import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib.patches import PathPatch
from matplotlib.path import Path


class Graphic:
    def __init__(self, **kwargs):
        sns.set_palette('Set1')
        # create the plot object
        self.fig, self.ax = plt.subplots(figsize=kwargs['figsize'])
        self.s = np.linspace(kwargs['linspace'][0], kwargs['linspace'][1])

    def lines(self, *args):
        for line in args:
            plt.plot(self.s, line['equation'] * self.s, lw=3, label=line['label'])
            plt.fill_between(self.s, 0, line['equation'] * self.s, alpha=0.1)

    def feasible_region(self, *coors):
        # highlight the feasible region
        path = Path(tuple(coors))
        # label = 'HP'
        patch = PathPatch(path, label='hp', alpha=0.5)
        self.ax.add_patch(patch)

    def nonnegative_constraints(self, **kwargs):
        plt.plot(np.zeros_like(self.s), self.s, lw=3, label=kwargs['x'])
        plt.plot(np.zeros_like(self.s), self.s, lw=3, label=kwargs['y'])

    def setup(self, **kwargs):
        plt.xlabel(kwargs['xlabel'], fontsize=16)
        plt.ylabel(kwargs['ylabel'], fontsize=16)
        plt.xlim(kwargs['xlim'][0], kwargs['xlim'][1])
        plt.ylim(kwargs['ylim'][0], kwargs['ylim'][1])
        plt.legend(fontsize=14)

    def show(self):
        plt.show()
