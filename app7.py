from sympy import symbols, Eq, solve, sympify
x = symbols('x')
expression = input("Please enter your expression")
try:
    left, right = expression.split('=')
    left = sympify(left)
    right = sympify(right)
    expression = Eq(left, right)
    solution = solve(expression, x)
    for i in range(0,len(solution)):
        solution[i] = str(solution[i]).replace("sqrt","√￣")
        print("x",i+1,": ",solution[i])
except Exception as e:
    print("error:",e)
