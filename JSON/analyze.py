import ast
from typing import List, Union, Tuple, Set

def analyze_python_code(node: ast.AST, current_function: str = '') -> Tuple[List[str], List[str]]:
    variable_names = []
    printed_variable_names = []
    
    def extract_names_from_expr(expr: ast.expr) -> None:
        """Recursively extract variable names from an expression."""
        if isinstance(expr, ast.Name):
            variable_name = f"{current_function}.{expr.id}" if current_function else expr.id
            printed_variable_names.append(variable_name)
        elif isinstance(expr, ast.Call):
            for arg in expr.args:
                extract_names_from_expr(arg)
    
    def extract_names_from_call(call_node: ast.Call) -> None:
        for arg in call_node.args:
            if isinstance(arg, ast.Name):
                variable_name = f"{current_function}.{arg.id}" if current_function else arg.id
                printed_variable_names.append(variable_name)
            elif isinstance(arg, ast.Call):
                extract_names_from_call(arg)
            elif isinstance(arg, ast.JoinedStr):  # f-string detection
                for value in arg.values:
                    if isinstance(value, ast.FormattedValue):
                        extract_names_from_expr(value.value)
    
    for child_node in ast.iter_child_nodes(node):
        # Update the current function scope if inside a function definition
        if isinstance(child_node, ast.FunctionDef):
            current_function = child_node.name
            # Extract function arguments
            for arg in child_node.args.args:
                variable_name = f"{current_function}.{arg.arg}"
                variable_names.append(variable_name)
        
        if isinstance(child_node, ast.Assign):
            for target in child_node.targets:
                if isinstance(target, ast.Name):
                    variable_name = f"{current_function}.{target.id}" if current_function else target.id
                    variable_names.append(variable_name)
                    
        elif isinstance(child_node, ast.For):
            if isinstance(child_node.target, ast.Name):
                variable_name = f"{current_function}.{child_node.target.id}" if current_function else child_node.target.id
                variable_names.append(variable_name)

        elif isinstance(child_node, ast.Call):
            if isinstance(child_node.func, ast.Name) and child_node.func.id == 'print':
                extract_names_from_call(child_node)
        
        child_variable_names, child_printed_variable_names = analyze_python_code(child_node, current_function)
        variable_names.extend(child_variable_names)
        printed_variable_names.extend(child_printed_variable_names)

    return variable_names, printed_variable_names

def analyze_file(file_path: str) -> Union[Tuple[List[str], List[str], Set[str]], None]:
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        
        tree = ast.parse(content)
        variable_names, printed_variable_names = analyze_python_code(tree)

        # Deduplicate while preserving order
        seen_vars = set()
        unique_variable_names = []
        for v in variable_names:
            if v not in seen_vars:
                unique_variable_names.append(v)
                seen_vars.add(v)

        seen_printed_vars = set()
        unique_printed_variable_names = []
        for v in printed_variable_names:
            if v not in seen_printed_vars:
                unique_printed_variable_names.append(v)
                seen_printed_vars.add(v)

        # Find variables that have not been printed
        not_printed = set(unique_variable_names) - set(unique_printed_variable_names)

        return unique_variable_names, unique_printed_variable_names, not_printed
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def analyze(file_path: str) -> None:
    result = analyze_file(file_path)
    assert result, "Could not analyze the file."
    unique_variable_names, unique_printed_variable_names, not_printed = result
    assert len(list(not_printed)) < 1, f"Variables not printed:\n{list(not_printed)}"
