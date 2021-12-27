morse_lib = {
    "a": "._ ",
    "b": "_... ",
    "c": "_._. ",
    "d": "_.. ",
    "e": ". ",
    "f": ".._. ",
    "g": "__. ",
    "h": ".... ",
    "i": ".. ",
    "j": ".___ ",
    "k": "_._ ",
    "l": "._.. ",
    "m": "__ ",
    "n": "_. ",
    "o": "___ ",
    "p": ".__. ",
    "q": "__._ ",
    "r": "._. ",
    "s": "... ",
    "t": "_ ",
    "u": ".._ ",
    "v": "..._ ",
    "w": ".__ ",
    "x": "_.._ ",
    "y": "_.__ ",
    "z": "__.. ",
    " ": "/ ",
}


def morse_encoder(words):
    code_list = []
    words_lower = words.lower()
    words_list = list(words_lower)
    for char in words_list:
        try:
            code_list.append(morse_lib[char])
        except KeyError:
            code_list.append("?")
    code = "".join(code_list)
    return code


print("Welcome to the Morse Code Converter!")
words_input = input("Input your word: \n")
coded = morse_encoder(words_input)
print(coded)
