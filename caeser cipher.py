def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    # Define the shift direction
    if mode == 'decrypt':
        shift = -shift
    
    # Loop through each character in the text
    for char in text:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')
            # Perform the shift
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char
        else:
            # If it's not an alphabetical character, don't change it
            result += char

    return result

def main():
    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt? Enter 'q' to quit: ").lower()
        if choice == 'q':
            break
        if choice not in ('e', 'd'):
            print("Invalid choice. Please choose 'e' for encrypt, 'd' for decrypt, or 'q' to quit.")
            continue

        message = input("Enter your message: ")
        try:
            shift = int(input("Enter the shift value: "))
        except ValueError:
            print("Invalid shift value. Please enter an integer.")
            continue

        if choice == 'e':
            encrypted_message = caesar_cipher(message, shift, mode='encrypt')
            print(f"Encrypted Message: {encrypted_message}")
        elif choice == 'd':
            decrypted_message = caesar_cipher(message, shift, mode='decrypt')
            print(f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()
