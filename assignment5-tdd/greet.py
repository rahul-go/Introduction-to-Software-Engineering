
def greet(names):
    if names is None:
        return "Hello, my friend."

    if type(names) != list:
        names = [names]
    return greet_multi(split_names(names))

def split_names(names):
    split = []
    for name in names:
        if name[0] == "\"" and name[len(name) - 1] == "\"":
            split += [name[1:len(name) - 1]]
        else:
            split += name.split(", ")
    return split

def greet_multi(names):
    lower = [name for name in names if not name.isupper()]
    upper = [name for name in names if     name.isupper()]
    _and_ = " AND " if len(lower) != 0 and len(upper) != 0 else ""

    return (
        greet_styled(lower, "Hello,", "and", ".")
        + _and_ +
        greet_styled(upper, "HELLO" , "AND", "!")
    )

def greet_styled(names, hello, conj, punc):
    if len(names) == 0:
        return ""
    if len(names) == 1:
        return f"{hello} {names[0]}{punc}"
    if len(names) == 2:
        return f"{hello} {names[0]} {conj} {names[1]}{punc}"

    result = f"{hello} "
    for i in range(len(names) - 1):
        result += f"{names[i]}, "
    result += f"{conj} {names[len(names) - 1]}{punc}"
    return result
