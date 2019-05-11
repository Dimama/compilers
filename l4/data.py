MARKER = '$'

precedence = {op: p for p, ops in enumerate(reversed([
    {'**', 'abs', 'not'},
    {'*', '/', 'mod', 'rem'},
    {'+\'', '-\''},
    {'+"', '-"', '&'},
    {'<', '<=', '=', '/>', '>', '>='},
    {'and', 'or', 'xor'},
])) for op in ops}

prefix = {'abs', 'not', '+\'', '-\''}

variables = {chr(i) for i in range(ord('a'), ord('z') + 1)}
constants = {chr(i) for i in range(ord('0'), ord('9') + 1)}

all_tokens = set(precedence) | variables | constants | {'(', ')', MARKER}
