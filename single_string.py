# class dictionary
# class dicionary keys
# class dictionary items
# class dictionary values

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

    morse_list = []
    for key in word:
        if key in morse_dict:
            morse_list.append(morse_dict[key])
    morse_string = " ".join(morse_list)
    return morse_string
