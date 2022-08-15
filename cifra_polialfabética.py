from unicodedata import normalize

key_ = "cifra"


def generate_alphabet() -> dict:
    letter_list = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers_list = [i for i in range(1, 27)]
    return dict(zip(letter_list, numbers_list))


def generate_sequence(key_word: str) -> list[int]:
    alphabet = generate_alphabet()
    return [
        alphabet[letter]
        for letter in key_word
        if letter in alphabet
    ]


SEQUENCE = generate_sequence(key_.upper())


def encrypt_text(text: str) -> str:
    new_text = normalize_text(text)
    encrypted_message = []
    alphabetic_value = generate_alphabet()
    len_sequence = len(SEQUENCE) - 1
    aux_len_sequence = 0
    for letter in new_text:
        if aux_len_sequence > len_sequence:
            aux_len_sequence = 0

        if not letter in alphabetic_value:
            encrypted_message.append(letter)
            continue

        letter_value = alphabetic_value.get(letter)
        key_value = SEQUENCE[aux_len_sequence]

        letter_value += key_value

        if letter_value > 26:
            letter_value -= 26
            encrypted_message.append(
                [
                    key
                    for key in alphabetic_value
                    if alphabetic_value[key] == letter_value
                ][0]
            )
        else:
            encrypted_message.append(
                [
                    key
                    for key in alphabetic_value
                    if alphabetic_value[key] == letter_value
                ][0]
            )
        aux_len_sequence += 1

    return "".join(encrypted_message)


def decrypted_message(message) -> str:
    new_message = message.strip().upper()
    real_message = []
    alphabetic_value = generate_alphabet()
    len_sequence = len(SEQUENCE) - 1
    aux_len_sequence = 0

    for letter in new_message:
        if aux_len_sequence > len_sequence:
            aux_len_sequence = 0

        if not letter in alphabetic_value:
            real_message.append(letter)
            continue

        letter_value = alphabetic_value.get(letter)
        key_value = SEQUENCE[aux_len_sequence]

        letter_value -= key_value

        if letter_value < 1:
            new_value = abs(letter_value)
            letter_value = 26 - new_value
            real_message.append(
                [
                    key
                    for key in alphabetic_value
                    if alphabetic_value[key] == letter_value
                ][0]
            )
        else:
            real_message.append(
                [
                    key
                    for key in alphabetic_value
                    if alphabetic_value[key] == letter_value
                ][0]
            )

        aux_len_sequence += 1
    return "".join(real_message)


def normalize_text(text: str) -> str:
    return normalize("NFKD", text).encode("ASCII", "ignore").decode("ASCII").upper()


if __name__ == '__main__':
    print(encrypt_text("Tẽxto cártão com muíta açêntuáçãõ"))  # WNDLP FJXLBR LUE NXRZS BFNTLVDLGG

    print(decrypted_message("WNDLP FJXLBR LUE NXRZS BFNTLVDLGG"))  # TEXTO CARTAO COM MUITA ACENTUACAO

