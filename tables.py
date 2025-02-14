from tabulate import tabulate

def process_assembly_code(file_name):
    opcode_table = {
        "START": "01", "MOVER": "04", "MOVEM": "05", "ADD": "03",
        "SUB": "02", "BC": "07", "STOP": "00", "MULT": "03",
        "ORIGIN": "-", "DS": "-", "EQU": "-", "END": "-"
    }

    symbol_table = {}
    literal_table = {}
    location_counter = 200
    literal_list = []
    assembly_code = []

    with open(file_name, "r") as file:
        for line in file:
            words = line.strip().split()
            if words and "LTORG" not in words: 
                assembly_code.append(words)

    for line in assembly_code:
        if line[0] not in opcode_table and line[0] not in ["END"]:  
            symbol_table[line[0]] = location_counter

        for word in line:
            if word.startswith("='") and word.endswith("'"):
                if word not in literal_table:
                    literal_list.append(word)

        location_counter += 1

    for line in assembly_code:
        if "END" in line:
            for literal in literal_list:
                if literal not in literal_table:
                    literal_table[literal] = location_counter
                    location_counter += 1
            break

    print("\nSymbol Table:")
    print(tabulate(symbol_table.items(), headers=["Symbol", "Address"], tablefmt="grid"))

    print("\nLiteral Table:" if literal_table else "\nLiteral Table is empty!")
    if literal_table:
        print(tabulate(literal_table.items(), headers=["Literal", "Address"], tablefmt="grid"))

    print("\nOpcode Table:")
    opcode_table_filtered = {k: v for k, v in opcode_table.items() if k != "LTORG"} 
    print(tabulate(opcode_table_filtered.items(), headers=["Mnemonic", "Opcode"], tablefmt="grid"))

process_assembly_code("assembly_program.txt")
