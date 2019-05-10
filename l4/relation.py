def make_relation(tokens, variables, constants, prefix, precedence):
    right_associative = {'**'}

    relation = {t: {t: None for t in tokens} for t in tokens}

    relation['('][')'] = '='

    relation['$']['('] = relation['(']['('] = '<'
    relation[')']['$'] = relation[')'][')'] = '>'

    for thing in variables | constants:
        relation['$'][thing] = relation['('][thing] = '<'
        relation[thing]['$'] = relation[thing][')'] = '>'

    for op in precedence:
        relation[op]['$'] = '>'
        relation['$'][op] = '<'

        relation[op]['('] = relation['('][op] = '<'
        relation[op][')'] = relation[')'][op] = '>'

        for thing in variables | constants:
            relation[op][thing] = '<'
            relation[thing][op] = '>'

        if op in prefix:
            for op2 in precedence:
                relation[op2][op] = '<'
                if precedence[op] > precedence[op2]:
                    relation[op][op2] = '>'
                else:
                    relation[op][op2] = '<'
        else:
            for op2 in precedence:
                if precedence[op] < precedence[op2] or precedence[op] == precedence[op2] and op in right_associative and op2 in right_associative:
                    relation[op][op2] = '<'
                    continue
                if precedence[op] > precedence[op2] or precedence[op] == precedence[op2] and op not in right_associative and op2 not in right_associative:
                    relation[op][op2] = '>'
                    continue

    return relation
