def is_valid_identifier(input_string):
    a_count = 0
    b_count = 0
    
    for char in input_string:
        if char == 'a':
            a_count += 1
        elif char == 'b':
            b_count += 1
        else:
            return False
    
    if a_count > 0:
        a_sequence_index = input_string.find('a')
        b_sequence_index = input_string.find('b', a_sequence_index)
        
        return a_sequence_index < b_sequence_index if b_sequence_index != -1 else False
    
    return b_count >= 1

while True:
    user_input = input("Enter a string: ")
    
    if user_input == 'exit':
        break
    else:
        print()
    
    if is_valid_identifier(user_input):
        print(f'"{user_input}" is a valid identifier.\n')
    else:
        print(f'"{user_input}" is not a valid idetifier.\n')
    