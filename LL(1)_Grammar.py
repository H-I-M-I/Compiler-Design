def find_first(grammar, symbol, computed_first_sets):

    if symbol in computed_first_sets:
        return computed_first_sets[symbol]

    first_set = set()

    if symbol in grammar:
        for production_rule in grammar[symbol]:
            epsilon_flag = True 
            for production_symbol in production_rule:
                production_first_set = find_first(grammar, production_symbol, computed_first_sets)
                first_set.update(production_first_set - {'Ɛ'})

                if 'Ɛ' not in production_first_set:
                    epsilon_flag = False
                    break
            if epsilon_flag:
                first_set.add('Ɛ')

    else:
        first_set.add(symbol)

    computed_first_sets[symbol] = first_set

    return first_set

def print_first_sets(first_sets):
    for symbol, first_set in first_sets.items():
        formatted_first_set = [x if x != 'i' else 'id' for x in first_set]
        print(f'FIRST({symbol}) = {{{", ".join(formatted_first_set)}}}')

def compute_first(grammar):
    first_sets = {}
    computed_first_sets = {}

    for symbol in grammar:
        first_sets[symbol] = find_first(grammar, symbol, computed_first_sets)

    return first_sets

def first_sets(first_sets):
    for symbol, first_set in first_sets.items():
        formatted_first_set = [x if x not in predefined_terminals else f"'{x}'" for x in first_set]
        print(f'FIRST({symbol}) = { {{ ", ".join(formatted_first_set) }} }')

predefined_terminals = {'id','(', ')'}

grammar = {
    "E": ["TE'"],
    "E'": ["+TE'", 'Ɛ'],
    "T": ["FT'"],
    "T'": ["*FT'", 'Ɛ'],
    "F": ["(E)", "id"],
}

first_sets = compute_first(grammar)
print_first_sets(first_sets)
