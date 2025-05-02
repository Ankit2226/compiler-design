# LR Parser Table Example for a simple grammar (manually created)
action_table = {
    (0, 'id'): ('s', 5),
    (0, '('): ('s', 4),
    (1, '+'): ('s', 6),
    (1, '$'): ('acc',),
    (2, '+'): ('r', 2),
    (2, '*'): ('s', 7),
    (2, ')'): ('r', 2),
    (2, '$'): ('r', 2),
    (3, '+'): ('r', 4),
    (3, '*'): ('r', 4),
    (3, ')'): ('r', 4),
    (3, '$'): ('r', 4),
    (4, 'id'): ('s', 5),
    (4, '('): ('s', 4),
    (5, '+'): ('r', 6),
    (5, '*'): ('r', 6),
    (5, ')'): ('r', 6),
    (5, '$'): ('r', 6),
    # ... add more entries
}

goto_table = {
    (0, 'E'): 1,
    (0, 'T'): 2,
    (0, 'F'): 3,
    (4, 'E'): 8,
    (4, 'T'): 2,
    (4, 'F'): 3,
    # ... add more entries
}

productions = {
    1: ('E', ['E', '+', 'T']),
    2: ('E', ['T']),
    3: ('T', ['T', '*', 'F']),
    4: ('T', ['F']),
    5: ('F', ['(', 'E', ')']),
    6: ('F', ['id']),
}

def lr_parse(tokens):
    stack = [0]
    tokens.append('$')
    pointer = 0

    while True:
        state = stack[-1]
        token = tokens[pointer]
        action = action_table.get((state, token))

        if action is None:
            print("Error: Invalid input.")
            return False

        if action[0] == 's':  # Shift
            stack.append(token)
            stack.append(action[1])
            pointer += 1
        elif action[0] == 'r':  # Reduce
            prod_num = action[1]
            lhs, rhs = productions[prod_num]
            for _ in range(len(rhs) * 2):
                stack.pop()
            state = stack[-1]
            stack.append(lhs)
            stack.append(goto_table[(state, lhs)])
            print(f"Reduce using {lhs} → {' '.join(rhs)}")
        elif action[0] == 'acc':
            print("Accepted!")
            return True

# Test the parser
tokens = ['id', '+', 'id', '*', 'id']
lr_parse(tokens)
