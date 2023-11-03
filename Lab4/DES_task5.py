import random
# Finding all 16 round keys with 48 bits each.
# Initial permutation (PC-1) table
pc1_table = [57, 49, 41, 33, 25, 17, 9, 1,
             58, 50, 42, 34, 26, 18, 10, 2,
             59, 51, 43, 35, 27, 19, 11, 3,
             60, 52, 44, 36, 63, 55, 47, 39,
             31, 23, 15, 7, 62, 54, 46, 38,
             30, 22, 14, 6, 61, 53, 45, 37,
             29, 21, 13, 5, 28, 20, 12, 4]

# Key rotation schedule for left circular shifts
key_rotation_schedule = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

# Permutation for selecting 48 bits from the 56-bit key (PC-2)
pc2_table = [14, 17, 11, 24, 1, 5, 3, 28,
             15, 6, 21, 10, 23, 19, 12, 4,
             26, 8, 16, 7, 27, 20, 13, 2,
             41, 52, 31, 37, 47, 55, 30, 40,
             51, 45, 33, 48, 44, 49, 39, 56,
             34, 53, 46, 42, 50, 36, 29, 32]

# Function to perform the initial permutation (PC-1)
def initial_permutation(key):
    return [key[bit - 1] for bit in pc1_table]
# Function to perform the left circular shift on a 28-bit key half
def left_circular_shift(key_half, shift):
    return key_half[shift:] + key_half[:shift]
# Function to perform the key schedule to generate all 16 round keys
def generate_round_keys(original_key):
    round_keys = []
    key = initial_permutation(original_key)
    left_half, right_half = key[:28], key[28:]

    for i in range(16):
        left_half = left_circular_shift(left_half, key_rotation_schedule[i])
        right_half = left_circular_shift(right_half, key_rotation_schedule[i])
        round_key = left_half + right_half
        round_keys.append([round_key[bit - 1] for bit in pc2_table])

    return round_keys

# Function to generate a random 64-bit key
def generate_random_key():
    return [random.randint(0, 1) for _ in range(64)]

# Function to display a binary list as a formatted string
def binary_list_to_string(binary_list):
    return ''.join(map(str, binary_list))

# Main menu
def main():
    print("DES Round Key Generation")
    print("1. Enter a manual 64-bit key")
    print("2. Generate a random 64-bit key")
    choice = input("Select an option (1/2): ")

    if choice == "1":
        key_str = input("Enter the 64-bit key (binary string): ")
        original_key = [int(bit) for bit in key_str]
    elif choice == "2":
        original_key = generate_random_key()
        print("Randomly generated 64-bit key:", binary_list_to_string(original_key))
    else:
        print("Invalid choice. Please select 1 or 2.")
        return

    round_keys = generate_round_keys(original_key)
    print("\nGenerated Round Keys:")
    for i, key in enumerate(round_keys):
        print(f"K{i + 1}: {binary_list_to_string(key)}")

if __name__ == "__main__":
    main()
#1010101010111100110011001100110011001100110011001100110011001100
