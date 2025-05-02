import re

def load_macros(filename):
    macro_map = {}
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            i = 0
            while i < len(lines):
                line = lines[i].strip()
                if line.startswith("MACRO"):
                    i += 1
                    macro_header = lines[i].strip()
                    parts = re.split(r'[ ,]+', macro_header)
                    macro_name = parts[0]
                    parameters = parts[1:]
                    body = []
                    i += 1
                    while i < len(lines) and lines[i].strip() != "MEND":
                        body.append(lines[i].strip())
                        i += 1
                    macro_map[macro_name] = (parameters, body)
                i += 1
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    return macro_map

def expand_macro(macro, arguments):
    parameters, body = macro
    if len(arguments) != len(parameters):
        return f"ERROR: Incorrect number of arguments for {macro}\n"
    expanded_lines = []
    for line in body:
        expanded_line = line
        for param, arg in zip(parameters, arguments):
            expanded_line = expanded_line.replace(param, arg)
        expanded_lines.append("+" + expanded_line)
    return "\n".join(expanded_lines) + "\n"

def process_assembly(filename, macro_map):
    expanded_code = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = re.split(r'[ ,]+', line)
                instruction = parts[0]
                if instruction in macro_map:
                    arguments = parts[1:]
                    expanded_code.append(expand_macro(macro_map[instruction], arguments))
                else:
                    expanded_code.append(line)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    return "\n".join(expanded_code)

def main():
    macro_file = "macro.txt"
    assembly_file = "assembly.txt"
    
    macro_map = load_macros(macro_file)
    expanded_code = process_assembly(assembly_file, macro_map)
    
    print("\nExpanded Assembly Code:")
    print(expanded_code)

if __name__ == "__main__":
    main()
