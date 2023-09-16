def shuffle_alphabet(key, alphabet):
    if len(key) < 7:
        raise ValueError("Key2 must be at least 7 characters!")

    key = ''.join(sorted(set(key.upper()), key=lambda x: key.upper().index(x)))
    shuffled_alphabet = key + ''.join(sorted(set(alphabet) - set(key)))
    print(shuffled_alphabet)
    alphabet_dict = {}
    for i, letter in enumerate(shuffled_alphabet):
        alphabet_dict[letter] = i

    return alphabet_dict


def caesar_cipher(text, main_key, permutation_key, action):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_dict = {}
    for i, letter in enumerate(alphabet):
        alphabet_dict[letter] = i

    shuffled_dict = shuffle_alphabet(permutation_key, alphabet)
    text = text.replace(" ", "").upper()
    result_text = ''

    for char in text:
        if char in alphabet:
            if action == 'e' or action == 'encrypt':  # Check for 'e' or 'encrypt'
                tmp = alphabet_dict[char]
                shifted_index = (tmp + main_key) % 26
                encrypted_char = list(shuffled_dict.keys())[list(shuffled_dict.values()).index(shifted_index)]
                result_text += encrypted_char
            elif action == 'd' or action == 'decrypt':
                tmp = shuffled_dict[char]
                shifted_index = (tmp - main_key) % 26
                encrypted_char = list(alphabet_dict.keys())[list(alphabet_dict.values()).index(shifted_index)]
                result_text += encrypted_char
        else:
            result_text += char

    return result_text


while True:
    text1 = input("Enter the text for encryption (or 'q' to exit): ")

    if text1.lower() == 'q':
        break

    key1 = int(input("Enter key1 (integer): "))
    key2 = input("Enter key2 (at least 7 characters): ").upper()
    choose = input("Choose action ('e' for encrypt or 'd' for decrypt): ").lower()

    if choose not in ['e', 'd']:
        print("Please enter 'e' for encrypt or 'd' for decrypt.")
    else:
        try:
            result_text = caesar_cipher(text1, key1, key2, choose)

            if choose == 'e':
                print("Encrypted:", result_text)
            else:
                print("Decrypted:", result_text)
        except ValueError as e:
            print(e)

