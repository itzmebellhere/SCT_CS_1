def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    print("=== Caesar Cipher Tool ===")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().lower()

    if choice not in ['e', 'd']:
        print("❌ Invalid choice. Use 'E' for Encrypt or 'D' for Decrypt.")
        return

    message = input("Enter your message: ")
    try:
        shift = int(input("Enter the shift value (e.g., 3): "))
    except ValueError:
        print("❌ Shift must be a number.")
        return

    if choice == 'e':
        result = caesar_encrypt(message, shift)
        print("🔐 Encrypted Message:", result)
    else:
        result = caesar_decrypt(message, shift)
        print("🔓 Decrypted Message:", result)

if __name__ == "__main__":
    main()
