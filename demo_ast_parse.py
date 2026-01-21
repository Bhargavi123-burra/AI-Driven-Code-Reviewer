import ast

code = """
def greet(name):
    return f"Hello,{name}!"
    
print(greet("world"))
"""

tree = ast.parse(code)
print(ast.dump(tree,indent=2))

