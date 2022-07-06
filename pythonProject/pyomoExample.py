import pyomo.opt.solver
import pyomo.environ as pyo

def main():
    model = pyo.ConcreteModel()

    model.x = pyo.Var([1, 2], domain=pyo.NonNegativeReals)

    model.OBJ = pyo.Objective(expr=2 * model.x[1] + 3 * model.x[2])

    model.Constraint1 = pyo.Constraint(expr=3 * model.x[1] + 4 * model.x[2] >= 1)

    opt = pyo.SolverFactory('cplex')
    opt.solve(model)
    model.display()



if __name__ == '__main__':
    main()