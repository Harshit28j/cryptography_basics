import math

# Caesar Cipher decryption function
def caesar_decrypt(ciphertext, shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            decrypted_char = chr((ord(char) - shift - ascii_offset) % 26 + ascii_offset)
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext

# Transposition Cipher decryption function
def trans_decrypt(en_msg, k):
    message = en_msg
    key = k
    numOfColumns = int(math.ceil(len(message) / float(key)))
    numOfRows = k
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
    plaintext = [''] * numOfColumns
    column = 0
    row = 0
    for symbol in message:
        plaintext[column] += symbol
        column += 1  # Point to the next column.
        if (column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            column = 0
            row += 1
    return ''.join(plaintext)

# Main program
def main():
    print("Welcome to the Encryption Decryption Program!")

    # Prompt user for encryption method
    method = int(input("Which encryption method would you like to decrypt?\nChoose number\n1) Caesar\n2) Substitution\n3) Transposition\n>"))

    # Prompt user for ciphertext
    ciphertext = input("Enter the ciphertext to decrypt: ")
    don_know = "[If you don't know the shift just press enter; the script will try all possible combinations then]"

    # Decrypt based on chosen method
    if method == 1:
        shift = input(f"Enter the shift value used in the Caesar cipher:\n{don_know}\n>")

        if shift == '':
            for i in range(1, 26):
                plaintext = caesar_decrypt(ciphertext, i)
                print(plaintext)

        elif shift.isnumeric():
            shift = int(shift)
            plaintext = caesar_decrypt(ciphertext, shift)
            print(plaintext)

        else:
            print('Invalid Command')

    elif method == 2:
        key = input(f"Enter the key used in the transposition cipher:\n{don_know}\n>")
        if key == '':
            for i in range(1, 26):
                plaintext = den(ciphertext, i)
                print(plaintext)

        elif key.isnumeric():
            key = int(key)
            plaintext = den(ciphertext, key)
            print(plaintext)

        else:
            print('Invalid Command')

    else:
        print("Invalid encryption method specified.")
        return

# Run the program
if __name__ == "__main__":
    main()
