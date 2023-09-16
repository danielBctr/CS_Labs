def caesar_cipher(text, key, operation, alphabet):
    alphabet_length = len(alphabet)
    result = []

    for char in text:
        if char.isalpha():  # Check if the character is alphabetic
            char = char.upper()
            index = alphabet.index(char)
            if operation == 'encryption':
                new_index = (index + key) % alphabet_length
            else:
                new_index = (index - key) % alphabet_length
            new_char = alphabet[new_index]
            if char.islower():
                new_char = new_char.lower()
            result.append(new_char)
        else:
            result.append(char)

    return ''.join(result)

def main():
    custom_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while True:
        print("\n\t#############Menu##############")
        operation = input("Enter 'e' for encryption or 'd' for decryption (q to quit): ").lower()

        if operation == 'q':
            break

        if operation not in ['e', 'd']:
            print("Invalid operation. Please enter 'e' for encryption or 'd' for decryption.")
            continue

        text = input("Enter the text: ").replace(" ", "")

        if not text.isalpha():
            print("Text should only contain alphabetic characters.")
            continue

        key = int(input("Enter the key (1-25): "))

        if not (1 <= key <= 25):
            print("Key should be between 1 and 25 inclusive.")
            continue

        if operation == 'e':
            result = caesar_cipher(text, key, 'encryption', custom_alphabet)
            print(f"Encrypted message: {result}")
            new_alphabet = caesar_cipher(custom_alphabet, key, 'encryption', custom_alphabet)

        else:
            result = caesar_cipher(text, key, 'decryption', custom_alphabet)
            print(f"Decrypted message: {result}")
            new_alphabet = caesar_cipher(custom_alphabet, key, 'decryption', custom_alphabet)


if __name__ == "__main__":
    main()

