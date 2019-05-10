class ParseError(Exception):
    pass


def parse(tokens, all_tokens, relation):
    tokens = enumerate(tokens + ['$'])

    res_string = ""
    next_token_no, next_token = next(tokens)
    stack_tail, stack_head = [], '$'
    while True:
        if next_token in all_tokens:
            if stack_head == '$' and next_token == '$':
                break
            current_relation = relation[stack_head][next_token]
            if current_relation in ('<', '='):
                stack_tail.append(stack_head)
                stack_head = next_token
                next_token_no, next_token = next(tokens)
                continue
            if current_relation == '>':
                while True:
                    if stack_head not in ('(', ')'):
                        res_string += stack_head
                    old_stack_head = stack_head
                    stack_head = stack_tail.pop()
                    if relation[stack_head][old_stack_head] == '<':
                        break
                continue
        raise ParseError(next_token_no)

    return res_string
