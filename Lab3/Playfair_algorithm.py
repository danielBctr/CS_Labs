import random
#Ă, Â, Ș, Ț, Î
def playfair_encrypt(pair, matrix):
    encrypted_pair = ""
    letter1, letter2 = pair
    row1, col1 = None, None
    row2, col2 = None, None
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == letter1:
                row1, col1 = row, col
            elif matrix[row][col] == letter2:
                row2, col2 = row, col
    if row1 != row2 and col1 != col2:
        encrypted_pair = matrix[row1][col2] + matrix[row2][col1]
    elif row1 == row2:
        encrypted_pair = matrix[row1][(col1 + 1) % len(matrix[row1])] + matrix[row2][(col2 + 1) % len(matrix[row2])]
    elif col1 == col2:
        encrypted_pair = matrix[(row1 + 1) % len(matrix)][col1] + matrix[(row2 + 1) % len(matrix)][col2]

    return encrypted_pair

def playfair_decrypt(pair, matrix):
    decrypted_pair = ""
    letter1, letter2 = pair
    row1, col1 = None, None
    row2, col2 = None, None

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == letter1:
                row1, col1 = row, col
            elif matrix[row][col] == letter2:
                row2, col2 = row, col

    if row1 != row2 and col1 != col2:
        decrypted_pair = matrix[row1][col2] + matrix[row2][col1]
    elif row1 == row2:
        decrypted_pair = matrix[row1][(col1 - 1) % len(matrix[row1])] + matrix[row2][(col2 - 1) % len(matrix[row2])]
    elif col1 == col2:
        decrypted_pair = matrix[(row1 - 1) % len(matrix)][col1] + matrix[(row2 - 1) % len(matrix)][col2]

    return decrypted_pair

def insert_when_repeating(message):
    for i in range(len(message) - 1):
        if message[i] == message[i + 1]:
            message = message[:i + 1] + random.choice(["Q", "X", "Z"]) + message[i + 1:]
    return message

def prepare_text(message):
    message = insert_when_repeating(message.replace(" ", "").upper().replace("J", "I"))
    message += "Z" * (len(message) % 2)
    return [message[i:i+2] for i in range(0, len(message), 2)]


def prepare_key(key):
    key = key.replace(" ", "").upper().replace("J", "I")
    return ''.join(sorted(set(key), key=key.find))


def create_matrix(key):
    alphabet = [char for char in 'AĂÂBCDEFGHIÎKLMNOPQRSȘTȚUVWXYZ' if char not in key]
    matrix = [[None] * 5 for _ in range(6)]
    key_index = 0

    for row in range(6):
        for column in range(5):
            if key_index < len(key):
                matrix[row][column] = key[key_index]
                key_index += 1


    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(' '.join(row))

def validate_input(prompt, valid_characters):
    while True:
        user_input = input(prompt).upper()
        if all(char in valid_characters or char.isspace() for char in user_input):
            return user_input
        else:
            print("Invalid input. Please enter only characters from the Romanian alphabet and spaces.")


def main():
    valid_characters = 'AĂÂBCDEFGHIÎKLMNOPQRSȘTȚUVWXYZ'

    while True:
        print("Playfair Cipher")
        print("1. Encryption")
        print("2. Decryption")
        print("3. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            msg = validate_input("Enter your message: ", valid_characters)
            key = validate_input("Enter key: ", valid_characters)

            if len(msg) == 0:
                print("Your message should not be empty")
                continue
            if len(key) < 7:
                print("Your key should contain 7 or more characters")
                continue

            msg = insert_when_repeating(msg)
            msg = prepare_text(msg)
            key = prepare_key(key)
            matrix = create_matrix(key)

            print("\nMatrix:")
            print_matrix(matrix)

            encrypted_text = [playfair_encrypt(pair, matrix) for pair in msg]
            encrypted_message = "".join(encrypted_text)
            print("\nEncrypted message:", encrypted_message)

        elif choice == 2:
            msg = validate_input("Enter your message: ", valid_characters)
            key = validate_input("Enter key: ", valid_characters)

            if len(msg) == 0:
                print("Your message should not be empty")
                continue
            if len(key) < 7:
                print("Your key should contain 7 or more characters")
                continue

            msg = prepare_text(msg)
            key = prepare_key(key)
            matrix = create_matrix(key)

            print("\nMatrix:")
            print_matrix(matrix)

            decrypted_text = [playfair_decrypt(pair, matrix) for pair in msg]
            decrypted_message = "".join(decrypted_text)
            print("\nDecrypted message:", decrypted_message)

        elif choice == 3:
            break

        else:
            print("Unknown choice")


if __name__ == '__main__':
    main()

