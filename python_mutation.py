# Problem: https://www.hackerrank.com/challenges/python-mutations

def mutate_string(string, position, character):
    string_list = list(string)
    string_list[position] = character
    new_string = ''.join(string_list)
    return new_string
