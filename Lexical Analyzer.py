GoLangForSyntax = """for i := 1 ; i < 5 ; i ++ { a = b + c }"""

# Regular expressions for token matching
REGEX_FOR = ["for"]
REGEX_VAR = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
REGEX_ANGKA = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
REGEX_CREMENT = ["++", "--"]
REGEX_OPERATOR = ["+", "-", "*", "/"]
REGEX_OPERATORPEMBANDING = [">=", "<=", "<", ">"]

# Token definition
TOKENS = [
    ("FOR", REGEX_FOR),
    ("VAR", REGEX_VAR),
    ("ANGKA", REGEX_ANGKA),
    ("CREMENT", REGEX_CREMENT),
    ("OPERATOR", REGEX_OPERATOR),
    ("OPERATORPEMBANDING", REGEX_OPERATORPEMBANDING),
    ("{", ["{"]),
    ("}", ["}"]),
    (";", [";"]),
    (":=", [":="]),
    ("=", ["="])
]

GoLangForSyntax = GoLangForSyntax.replace(" ", "")  # Remove whitespace from the input string

tokens = []

while GoLangForSyntax:
    found_token = False
    for token_type, regex_list in TOKENS:
        for regex in regex_list:
            if GoLangForSyntax.startswith(regex):
                tokens.append((GoLangForSyntax[:len(regex)], token_type))
                GoLangForSyntax = GoLangForSyntax[len(regex):]
                found_token = True
                break
        if found_token:
            break
    if not found_token:
        print(f"Error: Invalid token '{GoLangForSyntax[0]}'")
        break

for token, token_type in tokens:
    print(f"Token: {token:15} Type: {token_type}")
