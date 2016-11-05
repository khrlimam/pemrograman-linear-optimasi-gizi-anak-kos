import numpy as np
import pulp
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib.patches import PathPatch
from matplotlib.path import Path

import solver

bayam = 'bayam'
tempe = 'tempe'
problem_name = 'Optimasi Gizi Anak Kos'

# decision variables (variabel keputusan)
x = pulp.LpVariable(bayam, lowBound=0, cat=pulp.LpInteger)  # define variable as kuadran 1
y = pulp.LpVariable(tempe, lowBound=0, cat=pulp.LpInteger)  # define variable as kuadran 1

# objective / fungsi tujuan
max_protein = 14 * x + 57 * y
max_magnesium = 248 * x + 243 * y
maximize = max_protein + max_magnesium

# constraints / fungsi kendala
protein = 14 * x + 57 * y >= 50  # 14x+57y >= 50
magnesium = 248 * x + 243 * y >= 400  # 248x+243y >= 400
harga = 2500 * x + 2000 * y <= 15000 # 2500x+2000y <= 15000

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