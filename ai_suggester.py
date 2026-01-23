def get_ai_suggestions(code):
    suggestions = []

    if not code.strip():
        return ["No code provided for analysis."]

    if "print(" in code:
        suggestions.append("Avoid using print statements in production code. Use logging instead.")

    if "global" in code:
        suggestions.append("Avoid global variables for better maintainability.")

    if "def " in code and '"""' not in code:
        suggestions.append("Add docstrings to your functions for better readability.")

    if len(code.splitlines()) > 20:
        suggestions.append("Consider splitting long code into smaller functions.")

    if "except:" in code:
        suggestions.append("Avoid bare except clauses. Catch specific exceptions.")

    if not suggestions:
        suggestions.append("Your code looks well structured. Good job!")

    return suggestions

