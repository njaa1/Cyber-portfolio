def caesar_encrypt(message, shift):
    result = ""
    
    for char in message:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char
    
    return result


def caesar_decrypt(message, shift):
    result = ""
    
    for char in message:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            result += char
    
    return result


def main():
    print("=" * 50)
    print("Caesar Cipher")
    print("=" * 50)
    
    choice = input("\n1. Encrypt\n2. Decrypt\n\nChoose (1 or 2): ")
    
    if choice == "1":
        message = input("\nEnter message to encrypt: ")
        try:
            shift = int(input("Enter shift (1-25): "))
            if 1 <= shift <= 25:
                encrypted = caesar_encrypt(message, shift)
                print(f"\nEncrypted: {encrypted}")
            else:
                print("Shift must be between 1 and 25!")
        except ValueError:
            print("Enter a valid number!")
    
    elif choice == "2":
        message = input("\nEnter message to decrypt: ")
        try:
            shift = int(input("Enter shift (1-25): "))
            if 1 <= shift <= 25:
                decrypted = caesar_decrypt(message, shift)
                print(f"\nDecrypted: {decrypted}")
            else:
                print("Shift must be between 1 and 25!")
        except ValueError:
            print("Enter a valid number!")
    
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()