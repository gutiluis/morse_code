# return a single string with the word apple translated into morse code
def morse_code(word):
    morse_dict = {
        "a": "dot-dash",
        "b": "dash-dot-dot-dot",
        "c": "dash-dot-dash-dot",
        "d": "dash-dot-dot",
        "e": "dot",
        "f": "dot-dot-dash-dot",
        "g": "dash-dash-dot",
        "h": "dot-dot-dot-dot",
        "i": "dot-dot",
        "j": "dot-dash-dash-dash",
        "k": "dash-dot-dash",
        "l": "dot-dash-dot-dot",
        "m": "dash-dash",
        "n": "dash-dot",
        "o": "dash-dash-dash",
        "p": "dot-dash-dash-dot",
        "q": "dash-dash-dot-dash",
        "r": "dot-dash-dot",
        "s": "dot-dot-dot",
        "t": "dash",
        "u": "dot-dot-dash",
        "v": "dot-dot-dot-dash",
        "w": "dot-dash-dash",
        "y": "dash-dot-dash-dash",
        "z": "dash-dash-dot-dot"
    }

    var = morse_dict["a"] + "-" + morse_dict["p"] + "-" + morse_dict["p"] + "-" + morse_dict["l"] + "-" + morse_dict["e"]
    return var

