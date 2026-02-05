morse_code = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
    'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',
    'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',

}


def morse_to_text():
    user_input = input("Enter your text: ").upper()

    converted_text = []
    for char in user_input:
        if char in morse_code:
            converted_text.append(morse_code[char])
        else:
            converted_text.append(char)

    final_text = "".join(converted_text)
    print(f"Your converted text is: {final_text}")


morse_to_text()
