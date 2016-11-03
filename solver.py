import pulp


class Solver:
    def __init__(self, problem_name, what_to_do):
        self.problem_name = problem_name
        self.prob = pulp.LpProblem(self.problem_name, what_to_do)

    def kendala(self, *fks):
        for val in fks:
            self.prob += val

    def tujuan(self, ft):
        self.prob += ft

    def hasil(self, *args):
        result = self.prob.solve()
        try:
            assert result == pulp.LpStatusOptimal
            for res in args:
                print "Penyelesaian variabel {} adalah {}".format(res.name, res.value())
        except AssertionError:
            print "Tidak ada penyelesaian!"
