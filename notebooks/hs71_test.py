from gekko import GEKKO
m = GEKKO(remote=False)
x1,x2,x3,x4 = [m.Var(lb=1,ub=5,value=v) for v in (1,5,5,1)]
m.Equation(x1*x2*x3*x4>=25)
m.Equation(x1**2+x2**2+x3**2+x4**2==40)
m.Minimize(x1*x4*(x1+x2+x3)+x3)
m.solve(disp=False)
print([round(v.value[0],4) for v in (x1,x2,x3,x4)], "obj", round(m.options.OBJFCNVAL,4))
