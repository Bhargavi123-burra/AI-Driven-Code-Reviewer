import ast

#parse a simple python expression
node = ast.parse('x+y')
print(ast.dump(node, indent=2))