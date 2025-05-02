def shift_reduce_parser(input_string):
    grammar = {
        'E': ['E+E', 'E*E', 'id']
    }

    stack = []
    input_symbols = input_string.split()
    pointer = 0

    def reduce_stack():
        for lhs, productions in grammar.items():
            for rhs in productions:
                rhs_symbols = rhs.split()
                if len(stack) >= len(rhs_symbols):
                    if stack[-len(rhs_symbols):] == rhs_symbols:
                        print(f"Reduce: {' '.join(stack[-len(rhs_symbols):])} -> {lhs}")
                        for _ in range(len(rhs_symbols)):
                            stack.pop()
                        stack.append(lhs)
                        return True
        return False

    while True:
        # Try to reduce as long as possible
        while reduce_stack():
            pass

        if pointer < len(input_symbols):
            # Shift
            print(f"Shift: {input_symbols[pointer]}")
            stack.append(input_symbols[pointer])
            pointer += 1
        else:
            # No more input, try final reduction
            if not reduce_stack():
                break

    # Final result
    if stack == ['E']:
        print("Input is successfully parsed!")
    else:
        print("Error: Input cannot be parsed.")

# Example usage
input_expr = "id + id * id"
shift_reduce_parser(input_expr)
