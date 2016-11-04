import pulp

import solver

ban_sepeda = 'ban sepeda'
ban_motor = 'ban motor'
problem_name = 'Optimasi Laba Penjualan Ban Motor dan Sepeda'

# decision variables (variabel keputusan)
x = pulp.LpVariable(ban_sepeda, lowBound=0, cat='Integer')
y = pulp.LpVariable(ban_motor, lowBound=0, cat='Integer')

# objective / fungsi tujuan
maximize = 20000 * x + 40000 * y

# constrains / fungsi kendala
mesin1 = 5 * x + 2 * y
mesin1 = (mesin1 <= 800)
mesin2 = 4 * x + 8 * y
mesin2 = (mesin2 <= 800)
mesin3 = 0 * x + 10 * y
mesin3 = (mesin3 <= 800)

# magics
solver = solver.Solver(problem_name, pulp.LpMaximize)  # init the solver
solver.tujuan(maximize)  # tentukan tujuan yang kita inginkan
solver.kendala(mesin1, mesin2, mesin3)  # tambahkan kendala yang kita buat
solver.hasil(x, y)  # print hasil dari kedua variabel jika kasus diselesaikan
