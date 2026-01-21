# FInd all functions name. 

import ast

class FunctionNameFinder(ast.NodeVisitor):
    """Finds all function names"""
    
    def __init__(self):
        self.function_names = []
    
    def visit_FunctionDef(self, node):
        # Add function name to list
        self.function_names.append(node.name)
        # Keep visiting (in case there are nested functions)
        self.generic_visit(node)

# ============================================
# TEST IT
# ============================================

code = """
def login(username, password):
    pass

def logout():
    pass

def send_email(to, subject, body):
    pass
"""

tree = ast.parse(code)
finder = FunctionNameFinder()
finder.visit(tree)

print("Functions found:")
for name in finder.function_names:
    print(f"  - {name}()")

# OUTPUT:
# Functions found:
#   - login()
#   - logout()
#   - send_email()