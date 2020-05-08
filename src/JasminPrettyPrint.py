import re
from queue import SimpleQueue as sq
def jasmin_pretty_print(jasmin_code):
    pretty_jasmin = []
    indentations = 0
    for c in jasmin_code:
        if c == '{':
            indentations += 1
        elif c == '}':
            pretty_jasmin.pop()
            indentations -= 1
        elif c == '\n':
            pretty_jasmin.append(c)
            for _ in range(indentations):
                pretty_jasmin.append('\t')
            continue
        pretty_jasmin.append(c)
    pretty_jasmin = ''.join(pretty_jasmin)
    return pretty_jasmin