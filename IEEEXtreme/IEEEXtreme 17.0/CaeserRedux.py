import re
n = int(input())

def main():
    for _ in range(n):
        shift = int(input())
        text = input()
        # print(text)
        if any(re.search(r'\b{}\b'.format(re.escape(substring)), text) for substring in ["the"]):
            # print("not")
            print(encrypt(text, shift))
        else:
            # print("called")
            print(decrypt(text, shift))

def encrypt(text, shift):
    encrypted_text = ''
    for char in text:
        if char.isalpha() and char.islower():
            new_code = (ord(char) - 97 - shift) % 26 + 97
            encrypted_text += chr(new_code)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ''
    for char in text:
        if char.isalpha() and char.islower():
            new_code = (ord(char) - 97 + shift + 26) % 26 + 97  # Adding 26 to ensure the result is positive
            decrypted_text += chr(new_code)
        else:
            decrypted_text += char
    return decrypted_text

main()