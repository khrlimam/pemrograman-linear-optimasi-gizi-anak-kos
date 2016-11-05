import pulp
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib.patches import PathPatch
from matplotlib.path import Path

import solver

bayam = 'bayam'
tempe = 'tempe'
problem_name = 'Optimasi Gizi Anak Kos'

# decision variables (variabel keputusan)
x = pulp.LpVariable(bayam, lowBound=0, cat='Integer')
y = pulp.LpVariable(tempe, lowBound=0, cat='Integer')

# objective / fungsi tujuan
max_protein = 14 * x + 57 * y
max_magnesium = 248 * x + 243 * y
maximize = max_protein + max_magnesium

# constraints / fungsi kendala
protein = 14 * x + 57 * y
protein = (protein >= 50)  # 14x+57y >= 50
magnesium = 248 * x + 243 * y
magnesium = (magnesium >= 400)  # 248x+243y >= 400
harga = 2500 * x + 2000 * y
harga = (harga <= 15000)  # 2500x+2000y <= 15000

# magics
solver = solver.Solver(problem_name, pulp.LpMaximize)  # init the solver with maximize solution
solver.tujuan(maximize)  # add objective/fungsi tujuan
solver.kendala(protein, magnesium, harga)  # add constraints/fungsi kendala
solver.hasil(x, y)  # print result if solved

# print max
max_protein = 14 * x.value() + 57 * y.value()
max_magnesium = 248 * x.value() + 243 * y.value()
print "Max protein yang didapat sehari adalah {}g dari total minimal yang dibutuhkan (50g)".format(max_protein)
print "Max magnesium yang didapat sehari adalah {}mg dari total minimal yang dibutuhkan (400mg)".format(max_magnesium)
print "Dengan pengeluaran {:.0f}/hari dari jatah belanja 15000/perhari".format(2500 * x.value() + 2000 * y.value())

# graphic
sns.set_palette('Set1')

# create the plot object
fig, ax = plt.subplots(figsize=(8, 8))
s = np.linspace(0, 10)

plt.plot(s, 50 - s, lw=3, label='protein')
plt.fill_between(s, 0, 50 - s, alpha=0.1)
plt.plot(s, 400 - s, lw=3, label='magnesium')
plt.fill_between(s, 0, 400 - s, alpha=0.1)
# add demains constraint: soldiers <= 40
plt.plot(s, 15000 - s, lw=3, label='harga')
plt.fill_betweenx(s, 0, 15000 - s, alpha=0.1)

# add non-negativity constraints
plt.plot(np.zeros_like(s), s, lw=3, label='tempe non-negative')
plt.plot(s, np.zeros_like(s), lw=3, label='bayam non-negative')

# highlight the feasible region
path = Path([
    (0., 2.), (0., 1.), (0., 7.), (6., 0.), (3., 0.)
])
patch = PathPatch(path, label='feasible region', alpha=0.5)
ax.add_patch(patch)

# labels and stuff
plt.xlabel('bayam', fontsize=16)
plt.ylabel('tempe', fontsize=16)
plt.xlim(-0.5, 100)
plt.ylim(-0.5, 100)
plt.legend(fontsize=14)
plt.show()
